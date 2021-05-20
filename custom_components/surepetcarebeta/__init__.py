"""The surepetcare integration."""
from __future__ import annotations

import logging

from datetime import timedelta
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_PASSWORD, CONF_TOKEN, CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval
from surepy import Surepy
from surepy.enums import LockState
from surepy.exceptions import SurePetcareAuthenticationError, SurePetcareError

# pylint: disable=import-error
from .const import (
    ATTR_FLAP_ID,
    ATTR_LOCK_STATE,
    DOMAIN,
    SERVICE_SET_LOCK_STATE,
    SPC,
    SURE_API_TIMEOUT,
    TOPIC_UPDATE,
)


_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["binary_sensor", "sensor"]
SCAN_INTERVAL = timedelta(minutes=3)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            vol.All(
                {vol.Required(CONF_USERNAME): cv.string, vol.Required(CONF_PASSWORD): cv.string}
            )
        )
    },
    extra=vol.ALLOW_EXTRA,
)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up."""

    hass.data.setdefault(DOMAIN, {})

    try:
        surepy = Surepy(
            entry.data[CONF_USERNAME],
            entry.data[CONF_PASSWORD],
            auth_token=entry.data[CONF_TOKEN] if CONF_TOKEN in entry.data else None,
            api_timeout=SURE_API_TIMEOUT,
            session=async_get_clientsession(hass),
        )
    except SurePetcareAuthenticationError:
        _LOGGER.error("Unable to connect to surepetcare.io: Wrong credentials!")
        return False
    except SurePetcareError as error:
        _LOGGER.error("Unable to connect to surepetcare.io: %s", error)
        return False

    spc = SurePetcareAPI(hass, entry, surepy)
    hass.data[DOMAIN][SPC] = spc

    return await spc.async_setup()


class SurePetcareAPI:
    """Define a generic Sure Petcare object."""

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, surepy: Surepy) -> None:
        """Initialize the Sure Petcare object."""

        self.hass = hass
        self.config_entry = config_entry
        self.surepy = surepy
        self.states: dict[int, Any] = {}

    async def async_update(self, _: Any = None) -> None:
        """Get the latest data from Sure Petcare."""

        try:
            self.states = await self.surepy.get_entities(refresh=True)
            _LOGGER.debug("🐾 successfully updated states of %d entities", len(self.states))
        except SurePetcareError as error:
            _LOGGER.error("Unable to fetch data: %s", error)

        async_dispatcher_send(self.hass, TOPIC_UPDATE)

    async def set_lock_state(self, flap_id: int, state: str) -> None:
        """Update the lock state of a flap."""

        # https://github.com/PyCQA/pylint/issues/2062
        # pylint: disable=no-member
        if state == LockState.UNLOCKED.name.lower():
            await self.surepy.sac.unlock(flap_id)
        elif state == LockState.LOCKED_IN.name.lower():
            await self.surepy.sac.lock_in(flap_id)
        elif state == LockState.LOCKED_OUT.name.lower():
            await self.surepy.sac.lock_out(flap_id)
        elif state == LockState.LOCKED_ALL.name.lower():
            await self.surepy.sac.lock(flap_id)

    async def async_setup(self) -> bool:
        """Set up the Sure Petcare integration."""

        _LOGGER.info("")
        _LOGGER.info("----------------------------------------------------------")
        _LOGGER.info(" 🐾 meeowww..! to the beta of the surepetcare integration!")
        _LOGGER.info("    code: https://github.com/benleb/surepetcare")
        _LOGGER.info("----------------------------------------------------------")
        _LOGGER.info("")

        await self.async_update()

        async_track_time_interval(self.hass, self.async_update, SCAN_INTERVAL)

        self.hass.async_add_job(
            self.hass.config_entries.async_forward_entry_setup(self.config_entry, "binary_sensor")
        )

        self.hass.async_add_job(
            self.hass.config_entries.async_forward_entry_setup(self.config_entry, "sensor")
        )

        async def handle_set_lock_state(call: Any) -> None:
            """Call when setting the lock state."""
            await self.set_lock_state(call.data[ATTR_FLAP_ID], call.data[ATTR_LOCK_STATE])
            await self.async_update()

        lock_state_service_schema = vol.Schema(
            {
                vol.Required(ATTR_FLAP_ID): vol.All(cv.positive_int, vol.In(self.states.keys())),
                vol.Required(ATTR_LOCK_STATE): vol.All(
                    cv.string,
                    vol.Lower,
                    vol.In(
                        [
                            # https://github.com/PyCQA/pylint/issues/2062
                            # pylint: disable=no-member
                            LockState.UNLOCKED.name.lower(),
                            LockState.LOCKED_IN.name.lower(),
                            LockState.LOCKED_OUT.name.lower(),
                            LockState.LOCKED_ALL.name.lower(),
                        ]
                    ),
                ),
            }
        )

        self.hass.services.async_register(
            DOMAIN,
            SERVICE_SET_LOCK_STATE,
            handle_set_lock_state,
            schema=lock_state_service_schema,
        )

        return True

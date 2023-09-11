# Home Assistant

My Home Assistant Configuration for reference and restorative purposes.

## Integrations

- [ ] Alexa
  - Voice assistant of choice
  - Planning on setting up once enough devices are implemented in Home Assistant
- [x] Duck DNS
  - Dynamic DNS utility
- [ ] ESPHome
  - Planned for local control of smart devices such as NSPanels
- [x] FontAwesome
  - Additional entity icons
- [x] HACS
  - Community extensions
- [x] HomeKit Bridge
  - Outbound integration to expose Home Assistant devices/entities to Apple mobiles
- [x] Homewhiz
  - Used by Beko dishwasher
- [x] Honeywell Home Total Comfort Connect
  - evohome heating control application
  - *YAML configuration only*
- [x] Hyundai/Kia Connect
  - Read details frm my Kia Sorento
- [ ] LocalTuya
  - Local control of Tuya devices
  - Installed but not yet configured - Additional research needed
- [x] Meross Cloud IoT
  - Smart plugs
  - Used for table laps, office heater & christmas tree
- [ ] Meross LAN
  - Local control of Meross smart plugs
  - Transitioning from Meross Clout IoT
- [x] Meteorologisk institutt (Met.no)
  - Weather forecasts
- [x] Mobile app
  - Used on iPhones
- [x] MQTT
  - Local Mosquitto broker
- [x] Octopus Energy
  - Home energy monitoring
  - Awaiting delivery of Octopus Home Mini
- [x] Open Hardware Monitor
  - Used to monitor the server which hosts PLEX along with VMs for Home Assistant, Pi-Hole etc
  - *YAML configuration only*
- [x] Pi-hole
  - Network wide ad-blocker
  - Also using as DHCP server
- [x] Plex Media Server
  - Monitoring of Plex server
- [x] Radarr
  - Monitoring of Radarr media getter
- [x] Ring
  - Integration with Ring doorbell
- [ ] Rotospa
  - Quatrospa with "SpaNet Mini 1" controls. SpaNet have a 1st party WiFi module that connects to the control system however it's *very* expensive for what it is and doesn't seem to have much in terms of an API.
  - Some research suggests that it might be easier/cheaper to build a custom solution using an ESP32 (eg; [sn_eps32](https://github.com/wayne-love/sn_esp32))
- [x] Samsung Smart TV
  - Control/monitoring of TVs & soundbars
- [x] Shelly
  - Local control of Shelly devices
  - Currently limited usage but planning to add Shelly devices to most light switches over time
- [x] Sky Q
  - Local control/monitoring of Sky Q boxes
- [x] Sonoff
  - Local control of Sonoff devices
  - Currently disabled as my only Sonoff devices isn't working!
  - Intending to replace with Shelly devices anyway
- [x] SpeedTest
  - Automated internet speed monitoring/reporting
- [x] Sun
  - Out of box monitoring of sun rise/sun set
- [x] Sure Petcare
  - Monitoring of smart cat flap and its hub
- [x] Tautulli
  - Detailed telemetry for Plex server
- [ ] TrueNAS
  - Planned new home server OS
- [x] Tuya
  - Office light switch (planned to be replaced with a Shelly Dimmer)
  - RGB light bulbs that can't/haven't been flashed with ESPHome/Tasmota/wled
- [x] UniFi Network
  - Monitoring of local network devices, switches & access points
- [x] UniFi Protect
  - Planned CCTV camera solution
- [x] UPnP/IGD
  - Router monitoring
  - Internet connection uptime
- [x] WireGuard
  - VPN server to provide local access while on the go

## Former Integrations

- [x] Hot Tub
  - Lay-Z-Spa, replaced by Rotospa but retained in this repository for historical purposes.

## HACS Add-ins

- mini-graph-card
- Sonoff LAN
- Local Tuya
- button-card
- layout-card
- card-mod
- Meross Integration
- Weather Card
- Octopus Energy
- Kia Uvo/Hyundai Bluelink
- Meross LAN
- fontawesome
- Home Assistant Swipe Navigation
- Room Card
- Kiosk Mode
- TrueNAS
- SkyQ
- HomeWhiz

## YAML Dashboards

- [x] Main UI
- [ ] Sky Q Remotes:
  - [ ] Master Bedroom
  - [ ] Lounge

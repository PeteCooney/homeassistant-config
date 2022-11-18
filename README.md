# Home Assistant

My Home Assistant Configuration for reference and restorative purposes.

## Completed Integrations

- [x] Sure Petcare
  - Cat Flap & Hub
- [x] Ring
- [x] Meross
  - Smart plugs. Used for table laps, office heater & christmas tree
- [x] Sky Q
- [x] Pi-Hole
- [x] Home Bridge
  - For Apple HomeKit
- [x] Plex Server
- [x] Honeywell Home Total Comfort Connect
  - evohome heating control application
- [x] Kia Uvo
  - Integration for my Kia Sorento
- [x] Open Hardware Monitor
  - Used to monitor the server which hosts PLEX along with VMs for Home Assistant, Pi-Hole etc
- [x] Sonoff
  - Temporary solution for lights in Master Bedroom until I roll out Shelly devices
- [x] Samsung Smart TV
  - TVs throughout the house
- [x] Octopus Energy
- [x] SpeedTest
  - Automated internet speed monitoring/reporting
- [x] Tuya
  - Office light switch (to be replaced with a Shelly)
  - RGB light bulbs that can't/haven't been flashed with ESPHome/Tasmota/wled
- [x] UPnP/IGD
  - Router monitoring

## Incomplete Integrations

- [ ] Shelly
  - Gradually replacing light switches with Shelly devices
- [ ] Home networking
  - Probably UniFi
- [ ] CCTV cameras
  - Probably UniFi Protect
- [ ] Homewhiz
  - Used by Beko dishwasher. Seems like a pretty crappy ecosystem as you have to re-enable remote control every time you turn the dishwasher on!
- [ ] Alexa
- [ ] Rotospa
  - Quatrospa with "SpaNet Mini 1" controls. SpaNet have a 1st party WiFi module that connects to the control system however it's *very* expensive for what it is and doesn't seem to have much in terms of an API.
  - Some research suggests that it might be easier/cheaper to build a custom solution using an ESP32 (eg; [sn_eps32](https://github.com/wayne-love/sn_esp32))
- [ ] TuyaLocal
  - Replacement/alternative to Tuya Cloud because local control > cloud control!

## Former Integrations

- [x] Hot Tub
  - Lay-Z-Spa, replaced by Rotospa but retained in this repository for historical purposes.

## YAML Dashboards Setup

- [x] Main UI
- [ ] Sky Q Remotes:
  - [ ] Master Bedroom
  - [ ] Lounge

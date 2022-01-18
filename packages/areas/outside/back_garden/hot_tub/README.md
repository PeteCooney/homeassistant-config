# Hot Tub Setup

Control for Lay-Z-Spa Milan with Wi-Fi enabled pump.

Credit to [Bruce Hartley](https://github.com/B-Hartley) on who's work much of this was based.

## Automations

* Initialise Target Temperature Input Number - Sets the Target Temperature input number on Home Assistant startup or if this gets changed externally to Home Assistant (eg; from the control panel on the hot tub it self)
* Turn Off at 23:00 - Automatically turns the heater & pump off at 23:00
* Turn On at 07:00 - Automatically turns the heater & pump back on at 07:00
* Set Target Temperature - Sends a request to the "Set Temperature" API endpoint when the Target Temperature input number is changed

## Input Numbers

* Target Temp - Used to report/adjust the target temperature of the hot tub via Home Assistant

## REST Commands

* Command - Send a command to the hut tub as an HTTP POST request accepting the command, api_did token and an optional payload

## REST

* Login - Simple REST request that logs into the Lay-Z-Spa API and obtains a session token

## Sensors

### REST Sensors

* API Status - REST request to gather current status information (temperature, heater/pump status etc)
* Online - REST request to check if the hot tub is connected to the internet

### Template Sensors

These sensors consume the "API Status" REST Sensor

* Error - Indicates if the Hot Tub is in an error state
* Status Summary - Displays the current status of the tub (Offline, Error, Bubbling, Heating, Filtering, Switched Off, Unknown)
* Current Temperature - Displays the current temperature of the water
* Target Temperature - Displays the target temperature of the water

## Switches

* Bubbles - Turn the bubbles on and off
* Filter - Turn the filter on and off (Turning off the filter also turns off the heater)
* Heater - Turn the heater on and off (Turning on the heater also turns on the filter)
* Power - Turn the power on and off (turns everything off)







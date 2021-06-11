# Hot Tub Setup

Control for Lay-Z-Spa Milan with Wi-Fi enabled pump.

Credit to [Bruce Hartley](https://github.com/B-Hartley) on who's work much of this was based.

## Sensors etc

* Online - REST request to check if the hot tub is connected to the internet
* Status - REST request to gather current status information (temperature, heater/pump status etc)
* Error - Template sensor to display error message(s)
* Status Summary - Template sensor to display the current status of the tub (Offline, Error, Bubbling, Heating, Filtering, Switched Off, Unknown)
* Current Temperature - Template sensor to display the current temperature of the water
* Target Temperature - Template sensor to display the target temperature of the water
* Target Temperature - Input number to adjust the target temperature

## Switches

* Bubbles - Turn the bubbles on and off
* Filter - Turn the filter on and off (also turns off the heater)
* Heater - Turn the heater on and off
* Power - Turn the power on and off (turns everything off)

## REST Commands

* Command - Send a command to the hut tub as an HTTP POST request accepting the command, api_did token and an optional payload

## Automations

* Set Target Temperature - Triggers the "Set Temperature" command when the Target Temperature input number is changed
* Switch Heater Off Over Night - Turns the heater off between 23:00 and 07:00
  * This will likely be inverted once switch to Octopus Energy completes to take advantage of off-peak electricity prices
* Initialise Target Temperature Input Number - Sets the Target Temperature input number on Home Assist startup or if it's changed externally to Home Assit (eg; from the tub it self)

# Raspi-pwm-fancontrol

A Script that lets one use a [Raspberry Pi](https://www.raspberrypi.com/) to control a pwm fan based on temperatue readings from a temperature sensor.

In my setup i use an SHT31-D sensor and Be quiet Silent Wings pro 4, but the script should be pretty easily adaptable to many hardware setups.

To see the Ideas i tested and realized: [Ideas-Tests](./idea-tests/idea-tests.md)

All those parts put together then make the fancontrol script: [fancontrolscript.py](fancontrolscript.py)

I also put this together in a Docker container (Coming soon once i have the time to remove sensitive Info)

And i also added support to query a Server via IPMI to find out its internal temperature and change the fan speed according to it (Coming soon once i have the time to remove sensitive Info)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

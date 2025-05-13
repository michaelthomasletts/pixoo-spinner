![logo](https://raw.githubusercontent.com/michaelthomasletts/pixoo-spinner/refs/heads/main/pixoo-spinner.png)

## Description

A basic Python app for spinning an image and gradiating its color on a Pixoo 64 LED display device via Raspberry Pi -- if, for whatever reason, you would rather not use the mobile app.

## Background

First of all, the Divoom app is fantastic. It's fun. You can create custom images, load animations and graphics created by others onto your Pixoo 64 device, display weather or financial or sports data, and more. But I want to control the Divoom Pixoo 64 _independently_ -- because why not? Interfacing with the Pixoo 64 is quite simple: find the IPv4 address on your network for the Pixoo 64 and send HTTP requests to it. But there are already multiple Python packages available for doing exactly that, so I decided not to reproduce that code myself (yet). I have always wanted to work with a Raspberry Pi; this project, albeit superfluous due to the fact there's already a mobile app available for interfacing with a Pixoo 64 LED display device, gave me an excuse to finally learn about Raspberry Pi hands-on. Anyway, one critical thing you should know: **I don't recommend using this code for any images except those containing a basic symbol**, e.g. peace sign, crucifix, shield of David, etc. You will be sorely disappointed if you pass through an image of, say, Luigi or Mario or whatever. That's not what this package is for. In those cases, just use the Divoom app instead!

## Requirements

- A Raspberry Pi
- Python >= 3.13 (installed on a Raspberry Pi)
- [poetry](https://python-poetry.org/) (installed on a Raspberry Pi)
- A [Divoom Pixoo 64 device](https://a.co/d/7WVaibw)
- The IPv4 address for your Divoom Pixoo 64 device
- A .png image

## Installation

```bash

git clone https://github.com/michaelthomasletts/pixoo-spinner.git
pip install poetry  # if you don't have poetry already
cd <wherever you saved this repo locally>/pixoo-spinner
poetry install
poetry build  # build the wheel file
pip install <wherever you saved this repo locally>/ # optionally include the --user flag
pixoo-spinner/dist/<the wheel file name>
```

## CLI

There are other parameters available than just `--imageloc`, also called `-il`, and `--ip`. Check `cli.py` to learn more about those. Check out the `-t` parameter for local testing!

```bash

pixoo-spinner --imageloc <yourfolder/yourimage.png> --ip <your pixoo 64's IPv4>
```
#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install python-rpi.gpio python3-rpi.gpio
sudo apt install python3-pip
sudo apt-get install python-setuptools

# ws281x leds
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel

sudo apt-get install libi2c-dev i2c-tools libffi-dev python3-smbus

# mopidy

sudo apt-get install libxml2-dev libxslt1-dev

sudo apt-get install python-pip
wget -q -O - https://apt.mopidy.com/mopidy.gpg | sudo apt-key add -
sudo wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/jessie.list
sudo apt-get update
sudo apt-get install mopidy

sudo apt-get install libffi6 libffi-dev
sudo pip install -U Mopidy-WebSettingst Mopidy-MusicBox-Webclient Mopidy-Mopify mopidy-gmusic Mopidy-TuneIn
sudo pip install -U Mopidy-YouTube Mopidy-Local-SQLite Mopidy-Local-Images Mopidy-API-Explorer
pip install Mopidy-TuneIn

sudo apt-get install mopidy-soundcloud


# fot mopidy on ~/.config/mopidy/mopidy.conf at [audio] output = alsasink device=hw:1,0

## mopidy pulseaudio
#sudo nano /etc/pulse/default.pa
#add load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1
#nano ~/.config/mopidy/mopidy.conf
#[audio] output = pulsesink server=127.0.0.1
#
## also need to start pulse $server pulseaudio --start
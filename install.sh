#!/usr/bin/env bash


# ws281x leds
sudo apt-get update
sudo apt-get install gcc make build-essential python3-dev git scons swig
git clone https://github.com/jgarff/rpi_ws281x
cd rpi_ws281x/
sudo scons
cd python
sudo python3 setup.py build
sudo python3 setup.py install

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

sudo apt-get install mopidy-soundcloud


# fot mopidy on ~/.config/mopidy/mopidy.conf at [audio] output = alsasink device=hw:1,0
## mopidy pulseaudio
#sudo nano /etc/pulse/default.pa
#add load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1
#nano ~/.config/mopidy/mopidy.conf
#[audio] output = pulsesink server=127.0.0.1
#
## also need to start pulse $server pulseaudio --start

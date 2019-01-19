#!/usr/bin/env bash


mopidy &

cd /home/pi/amp_iot && sudo python3.5 run.py &
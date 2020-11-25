#!/bin/bash

#sleep 20

cd /home/pi/Desktop/cat_Feeder

export DISPLAY=":0"
xhost +
sudo python3 /home/pi/Desktop/Cat_Feeder/catFeeder.py & /home/pi/Desktop/Cat_Feeder/catFeeder.log 2>&1
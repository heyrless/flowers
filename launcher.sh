#!/bin/bash

source /home/pi/flo/bin/activate
nohup jupyter notebook &>/dev/null &
python3 pop_db.py &
python3 flowers_bot.py &
python3 humidity_relay.py &
python3 webcam_timelapse.py &

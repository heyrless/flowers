#!/bin/bash

cd /home/pi/flowers
source /home/pi/.venv/jns/bin/activate
nohup jupyter lab &>/dev/null &
python3 flowers_bot.py &
python3 webcam_timelapse.py &
python3 control_humidity.py &


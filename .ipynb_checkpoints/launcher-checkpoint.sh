#!/bin/bash

cd /home/pi/flowers
source /home/pi/.venv/jns/bin/activate
nohup jupyter lab &>/dev/null &
python3 flowers_bot.py &
python3 webcam_timelapse.py &
python3 control_humidity.py &
#sudo -u pi python3 flowers_bot.py &
#sudo -u pi python3 humidity_relay.py &
#sudo -u pi python3 webcam_timelapse.py &

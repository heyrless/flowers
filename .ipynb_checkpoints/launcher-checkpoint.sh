#!/bin/bash

cd /home/pi/flowers
source /home/pi/.venv/jns/bin/activate
nohup jupyter lab &>/dev/null &
#sudo -u pi python3 pop_db.py &
#sudo -u pi python3 flowers_bot.py &
#sudo -u pi python3 humidity_relay.py &
#sudo -u pi python3 webcam_timelapse.py &

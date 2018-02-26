#!/bin/bash

sudo -u pi source /home/pi/flo/bin/activate
sudo -u pi nohup jupyter notebook &>/dev/null &
sudo -u pi python3 pop_db.py &
sudo -u pi python3 flowers_bot.py &
sudo -u pi python3 humidity_relay.py &
sudo -u pi python3 webcam_timelapse.py &

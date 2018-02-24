#!/bin/sh
# launcher.sh

cd /home/pi/PiHome/
sudo -u pi python3 pop_db.py &
sudo -u pi python3 thbot.py &
sudo -u pi python3 humidity_relay.py &
sudo -u pi python3 webcam_timelapse.py &

#!/bin/bash
# launcher.sh

cd /home/pi/Flowers/
sudo -u pi source /home/pi/.venv/jns/bin/activate &
sudo -u pi jupyter lab &
#sudo -u pi python3 pop_db.py &
#sudo -u pi python3 flowers_bot.py &
#sudo -u pi python3 humidity_relay.py &
#sudo -u pi python3 webcam_timelapse.py &

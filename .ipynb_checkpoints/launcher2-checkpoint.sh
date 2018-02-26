#!/bin/bash
sudo -u pi source /home/pi/.venv/jns/bin/activate
sudo -u pi nohup jupyter lab &>/dev/null &

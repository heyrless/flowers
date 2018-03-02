#!/bin/bash

cd /home/pi/flowers
source /home/pi/.venv/jns/bin/activate
python3 control_airflow.py &
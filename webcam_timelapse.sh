#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")
#DATE=$(date +"%image_%H%M")
fswebcam -S 60 /home/pi/PiHome/webcam/timelapse/$DATE.jpg

#fswebcam -S 60 --no-banner /home/pi/PiHome/webcam/timelapse/$DATE.jpg

#fswebcam -r 640x480 --no-banner /home/pi/PiHome/webcam/pic.jpg

#fswebcam -S 60 /home/pi/PiHome/webcam/pic.jpg
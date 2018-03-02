#!/bin/bash

DAYSAGO=$1
FRAMERATE=$2

STAMP=`date --date="$DAYSAGO day ago" +%Y-%m-%d`

cd /home/pi/flowers/webcam/movie
find . -type f -iname \*.mp4 -delete
find . -type f -iname \*.jpg -delete

cd /home/pi/flowers/webcam/timelapse

a=1
for i in $STAMP*.jpg; do
  new=$(printf "/home/pi/flowers/webcam/movie/%04d.jpg" "$a")
  cp -i "$i" "$new"
  let a=a+1
done

cd /home/pi/flowers/webcam/movie

#avconv -r $FRAMERATE -i %04d.jpg timelapse.mp4
#ffmpeg -r $FRAMERATE -f image2 -i %04d.jpg timelapse.mp4
ffmpeg -framerate $FRAMERATE -i %04d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p timelapse.mp4

#find . -type f -iname \*.jpg -delete
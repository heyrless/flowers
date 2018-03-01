import subprocess
import time
import datetime

while True:
    
    hour_now = datetime.datetime.now().time().hour
    
    if hour_now >= 6 and hour_now <= 23:
        subprocess.run(["sh","/home/pi/flowers/webcam_timelapse.sh"])
        
    time.sleep(120)
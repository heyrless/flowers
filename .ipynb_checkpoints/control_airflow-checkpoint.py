#from apscheduler.schedulers.blocking import BlockingScheduler
#from apscheduler.scheduler import Scheduler
import time
import RPi.GPIO as GPIO

def relay_on_off(pin_in=1,status=0):
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)

    if pin_in == 1:
        pin = 17
    elif pin_in == 2:
        pin = 27

    if status:
        GPIO.output(pin, GPIO.LOW)
    else:
        GPIO.output(pin, GPIO.HIGH)

    
def get_status(pin_in=1):
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)

    if pin_in == 1:
        pin = 17
    elif pin_in == 2:
        pin = 27
    
    status = GPIO.input(pin)

    return not status #status inverted since GPIO in on when LOW and viceversa
    

#sched = Scheduler()

#@sched.cron_schedule(minute=20)
#def timed_job():
relay_on_off(2,1)  
time.sleep(300)
relay_on_off(2,0)
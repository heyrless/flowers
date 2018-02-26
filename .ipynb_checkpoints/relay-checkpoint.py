import RPi.GPIO as GPIO

def relay_on_off(pin_in=1,status=0):
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    if pin_in == 1:
        pin = 18
    elif pin_in == 2:
        pin = 23

    if status:
        GPIO.output(pin, GPIO.LOW)
    else:
        GPIO.output(pin, GPIO.HIGH)

    
def get_status(pin_in=1):
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    if pin_in == 1:
        pin = 18
    elif pin_in == 2:
        pin = 23
    
    status = GPIO.input(pin)

    return not status #status inverted since GPIO in on when LOW and viceversa
    
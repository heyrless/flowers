import Adafruit_DHT
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
    
relay_on_off(1,0)
relay_on_off(2,0)
flag = 0
while True:
    humidity, temperature = Adafruit_DHT.read_retry(22, 4)
    if humidity < 60:
        relay_on_off(1,1)
        #print('Humidity at {0:0.1f}: Pin 1 on.'.format(humidity))
    else:
        relay_on_off(1,0)
        #print('Humidity at {0:0.1f}: Pin 1 off.'.format(humidity))
        
    if not get_status(2) and not flag and (humidity > 70 or temperature > 27):
        relay.relay_on_off(2,1)
        flag = 1
        #print('Humidity at {0:0.1f}% and Temperature at {1:0.1f}*: Pin 2 on.'.format(humidity, temperature))
    elif flag and humidity < 65 and temperature <= 26:
        relay_on_off(2,0)
        flag = 0
    
    print('Humidity at {0:0.1f}% and Temperature at {1:0.1f}*:\n Pin 1 is {2:}, Pin 2 is {3:}.'.format(humidity, temperature, get_status(1), get_status(2)))
        
    time.sleep(5)
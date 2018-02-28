import relay
import Adafruit_DHT
import time

#relay_on_off(pin_in=1,status=0):
#get_status(pin_in=1):

while True:
    humidity, temperature = Adafruit_DHT.read_retry(22, 4)
    if humidity < 55:
        relay_on_off(1,1)
    else:
        relay_on_off(1,0)
        
    if not get_status(2) and (humidity > 75 or temperature > 27):
        relay_on_off(2,1)
    else:
        relay_on_off(2,0)
        
    time.sleep(5)

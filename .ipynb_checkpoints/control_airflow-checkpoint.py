import relay
import Adafruit_DHT
import time

#relay_on_off(pin_in=1,status=0):
#get_status(pin_in=1):

while True:
    humidity, temperature = Adafruit_DHT.read_retry(22, 4)
    while temperature > 26:
        relay_on_off(2,1)
        time.sleep(60)
        
    relay_on_off(2,0)
        
    if humidity > 75:
        relay_on_off(2,1)
        time.sleep(60)
        relay_on_off(2,0)
        
    time.sleep(5)
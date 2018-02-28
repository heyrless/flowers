import relay
import time

#relay_on_off(pin_in=1,status=0):
#get_status(pin_in=1):

while True:
    relay_on_off(2,1)  
    time.sleep(300)
    relay_on_off(2,0)
    time.sleep(3300)
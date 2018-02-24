import Adafruit_DHT
import time
import relay
import datetime

humidity, temperature = Adafruit_DHT.read_retry(22, 4)

while True:
    
    humidity, temperature = Adafruit_DHT.read_retry(22, 4)
    hour_now = datetime.datetime.now().time().hour
    status1 = relay.get_status(1)
    status2 = relay.get_status(2)
    
    print("Pin 1 - {}".format(status1))
    print("Pin 2 - {}".format(status2))
     
    if humidity and temperature:
        
        print("Humidity {}\t Temperature {}".format(humidity,temperature))
          
        if humidity > 65 and status1:
            print("Pin 1 - set off")
            relay.relay_on_off(1,0)
        elif humidity < 50 and not status1:
            print("Pin 1 - set on")
            relay.relay_on_off(1,1)
        
    if hour_now >= 22 or hour_now < 7 and status2:
        relay.relay_on_off(2,0)
        print("Pin 2 - set off")
        
    elif hour_now >= 7 and hour_now < 22 and not status2:
        relay.relay_on_off(2,1)
        print("Pin 2 - set on")
           
    time.sleep(60)

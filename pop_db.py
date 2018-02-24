#!/usr/bin/python

import time
import datetime
import Adafruit_DHT

from sqlite3 import dbapi2 as sq3

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT22
# Example of sensor connected to Raspberry Pi pin 23
DHT_PIN  = 4

db = sq3.connect("box_temp.db")

def insert_into_db(db,temp,hum):
    db.execute("INSERT INTO temphum VALUES (?,?,?)",(datetime.datetime.now(), temp, hum))
    db.commit()
    #print("Inserted: {}, {}".format(temp, hum))

# Populate db
def populate_db():
    while True:
        hum, temp = (None,None)

        while not hum and not temp:
            hum, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
            print(hum, temp)

        hum, temp = (round(hum,1), round(temp,1))

        insert_into_db(db,temp,hum)
        
        time.sleep(60)
        

populate_db()
#!/usr/bin/python
import time
import telepot
import Adafruit_DHT
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os
import sys
#import thplot as dz

print("*******New session*******")
print(datetime.datetime.now())
print("*************************")


from sqlite3 import dbapi2 as sq3
import os
PATHSTART="."
def get_db(dbfile):
    sqlite_db = sq3.connect(os.path.join(PATHSTART, dbfile))
    return sqlite_db


def get_plot(bhours,hmin=30,hmax=90,tmin=15,tmax=35):
    
    db = get_db("box_temp.db")
    
    def make_query(sel):
        c=db.cursor().execute(sel)
        return c.fetchall()

    def make_frame(list_of_tuples):
        legend = [e[1] for e in make_query("PRAGMA table_info(temphum);")]
        framelist=[]
        for i, cname in enumerate(legend):
            framelist.append((cname,[e[i] for e in list_of_tuples]))
        return pd.DataFrame.from_items(framelist)

    def insert_into_db(db,temp,hum):
        db.execute("INSERT INTO temphum VALUES (?,?,?)",(datetime.datetime.now(), temp, hum))


    def get_dates(bhours):
        # select how many hours back you wanna go
        today = datetime.datetime.now()
        first = today - datetime.timedelta(hours=bhours)
    #     print(today,first)
        return str(first), str(today)

    first, today = get_dates(bhours)

    # query_date = "SELECT * FROM temphum WHERE date >= "+'2017-02-28 18:00:00.000' AND date <= '2017-02-28 19:00:00.000'"
    query_date = "SELECT * FROM temphum WHERE date >= '"+ first +"' AND date <= '" + today + "'"

    
    out = make_query(query_date)
    
    
    df = make_frame(out)

    x = df.date.tolist()
    
    try:
        plt.plot_date(x, df.temperature.as_matrix(), 'b')
        plt.ylim(tmin,tmax)
        plt.grid(True)
        plt.xlabel('Date')
        plt.ylabel('Temperature °C')
        plt.title('Temperature')
        plt.gcf().autofmt_xdate() 
        plt.savefig("/home/pi/PiHome/temperature.png")

     
        plt.plot_date(x, df.humidity.as_matrix(), 'm')
        plt.ylim(hmin,hmax)
        plt.grid(True)
        plt.xlabel('Date')
        plt.ylabel('Humidity %')
        plt.title('Humidity')
        plt.gcf().autofmt_xdate()
        plt.savefig("/home/pi/PiHome/humidity.png")
        
        print("No problem plotting...")
    except:
        print("Problem plotting...")

        
    db.close()

bhours = int(sys.argv[1])



if len(sys.argv) == 6:
    
    get_plot(bhours,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])) #save plots
else:
    get_plot(bhours)
    
#db initialization    

'''
ourschema="""
DROP TABLE IF EXISTS "temphum";
CREATE TABLE "temphum" (
    "date" DATETIME,
    "temperature" REAL,
    "humidity" REAL
);
"""

def init_db(dbfile, schema):
    """Creates the database tables."""
    db = get_db(dbfile)
    db.cursor().executescript(schema)
    db.commit()
    return db

#db=init_db("box_temp.db", ourschema)

#db = get_db("box_temp.db")
'''

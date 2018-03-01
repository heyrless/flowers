#!/usr/bin/python
import time
import telepot
import Adafruit_DHT
import datetime
import os
import subprocess
import relay

print("*******New session*******")
print(datetime.datetime.now())
print("*************************")


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)
        
    if command[:5] == '/plot':
        
        if len(command)==5:
            bhours = 24
        else:       
            bhours = int(command[5:])
            
        bot.sendMessage(chat_id, 'Generating plot of the last {} hours.'.format(bhours))
        
        subprocess.run(["python3","/home/pi/flowers/make_th_plot.py",str(bhours)])
        #get_plot(bhours)
        
        print("Plot generated...")
        #bot.sendMessage(chat_id, 'Temp={0:0.1f}*'.format(temperature))
        f = open('/home/pi/flowers/temperature.png', 'rb')  # some file on local disk
        response = bot.sendPhoto(chat_id, f)
        f = open('/home/pi/flowers/humidity.png', 'rb')  # some file on local disk
        response = bot.sendPhoto(chat_id, f)
        #print("Image sent...")
        
    elif command == '/th':
        
        humidity, temperature = Adafruit_DHT.read_retry(22, 4)
        
        if humidity and temperature:
            bot.sendMessage(chat_id, 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            bot.sendMessage(chat_id, 'Sensor seems offline...')
            
    elif command == '/h':
        bot.sendMessage(chat_id, 'SUKA!')
        
    elif command[:8] == '/ltrange':
        delta = 8
        bhours = command[delta:delta+2]
        hmin = command[delta+2:delta+4]
        hmax = command[delta+4:delta+6]
        tmin = command[delta+6:delta+8]
        tmax = command[delta+8:delta+10]
        
        
        bot.sendMessage(chat_id, 'Generating plot of the last {} hours.'.format(bhours))
        bot.sendMessage(chat_id, 'hmin = {} hmax = {} tmin = {} tmax = {}'.format(hmin,hmax,tmin,tmax))
        subprocess.run(["python3","/home/pi/flowers/make_th_plot.py",str(bhours),str(hmin),str(hmax),str(tmin),str(tmax)])
        #get_plot(bhours)
        
        print("Plot generated...")
        #bot.sendMessage(chat_id, 'Temp={0:0.1f}*'.format(temperature))
        f = open('/home/pi/flowers/temperature.png', 'rb')  # some file on local disk
        response = bot.sendPhoto(chat_id, f)
        f = open('/home/pi/flowers/humidity.png', 'rb')  # some file on local disk
        response = bot.sendPhoto(chat_id, f)
        #print("Image sent...")
    
    elif command[:2] == '/r':
        pin = command[2]
        status = command[3]
        bot.sendMessage(chat_id, 'Pin: {} - Status: {}'.format(pin,status))
        relay.relay_on_off(int(pin),int(status))
    
    elif command == '/pic':
        bot.sendMessage(chat_id, 'Sending picture...')
        subprocess.run(["sh","/home/pi/flowers/webcam.sh"])
        f = open('/home/pi/flowers/webcam/pic.jpg', 'rb')
        response = bot.sendPhoto(chat_id, f)

    elif command[:4] == '/vid':
        days_ago = command[4]
        frame_rate = command[5:]
        bot.sendMessage(chat_id, 'Generating timelapse of {} days ago at {} FPS'.format(days_ago,frame_rate))
        subprocess.call(["/bin/bash","/home/pi/flowers/webcam_build_mp4.sh",str(days_ago),str(frame_rate)])
        
        f = open('/home/pi/flowers/webcam/movie/timelapse.mp4', 'rb')
        bot.sendVideo(chat_id, f)
        
    else:
        bot.sendMessage(chat_id, 'Command not recognized - type /help or /h for info.')

        
        
TOKEN = open('/home/pi/flowers/bot_token.config')
bot = telepot.Bot(TOKEN.read())
TOKEN.close()  

bot.message_loop(handle)
print('I am listening ...')

#print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

while True:
    time.sleep(1)
    #sys.stdout.flush()
    
    

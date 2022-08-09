#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
import Adafruit_CharLCD as LCD
import socket
import commands
import datetime
import shutil
import urllib
from gpiozero import CPUTemperature


datetime.datetime.now()
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)


# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

cpu = CPUTemperature()

def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address


while True:
    
    try:
        lcd.message('Pi IP:-\n'+get_ip_address())
    except:
        lcd.message('Not Connected:-\n'+'To the Internet')
        time.sleep(1.0)
        lcd.clear()
        lcd.message('Net Rider:-\n@1AM8OSS')
                   

    time.sleep(1.0)
    lcd.clear()
    lcd.message(time.ctime()+'\n')
    lcd.message('Sys.Temp:- ')
    lcd.message(str(cpu.temperature)+'\n')
    time.sleep(2.0)
    lcd.clear()
    
    #lcd.message("Time:%s" %time.strftime("%H:%M:%S")+'\n')
    #lcd.cursor_pos = (1, 0)
    #lcd.message("Date:%s" %time.strftime("%d-%m-%Y"))
  
  

  
   #lcd.message('Techivagant')
   #time.sleep(2.0)
   #lcd.clear()
 


#time.sleep(20.0)
#lcd.clear()
#lcd.message('Give The Input To The Terminal')
#lcd.clear()
#text = raw_input("Type Something to be displayed: ")
#lcd.message(text)
#Wait 5 seconds
#time.sleep(20.0)
#lcd.clear()
#lcd.message('Goodbye\nWorld!')

#!/usr/bin/python
#Python program for FL-480 water flow sensor
#Working range : 1-30 L/min
#Water Pressure: <=1.75 Mpa
#Import all of the library
import pandas as pd
import requests
from datetime import datetime
import RPi.GPIO as GPIO
import time, sys
import os
import Adafruit_CharLCD as LCD
import csv

#name csv file as "WaterFlowData"
csvfile = "WaterFlowData.csv"

#referring to the pins by the "Broadcom SOC channel" number
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# for light bulb
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)


# for LCD screen, Raspberry Pi pin setup
lcd_rs = 7
lcd_en = 8
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

#variables for water flow sensor
GPIO.setmode(GPIO.BCM)
# set input pin as 27
#GPIO.setup(inpt, GPIO.IN)
inpt = 27
GPIO.setup(inpt, GPIO.IN)

rate_cnt =0                     #Revolution counts(r/min)
tot_cnt=0                       #total count
time_zero = 0.0                 #start up time
time_start = 0.0                #keep measurement begin time and end time
time_end = 0.0
gpio_last =0                    #Was last state 0 or 1 or other
pulses = 0                      #0-5 pulese
constant= 1.79                  #The hall-effect flow sensor outputs approximately 1.79 pulses per second per flow rate

time_zero = time.time()
# set a loop and let it run forever
while True:
    rate_cnt = 0    #reset rate counter
    pulses =0
    time_start = time.time()  #keep start time
    while pulses <= 5:          #6 pulses per revolution
        gpio_cur = GPIO.input(inpt)
        if gpio_cur != 0 and gpio_cur != gpio_last:
            pulses +=1
        gpio_last = gpio_cur   #keep last input
        try:
            #None
            if (round((tot_cnt * constant) / 100,2)) <= 50:
                GPIO.output(16,GPIO.HIGH)
                GPIO.output(12,GPIO.LOW)
            else:
                GPIO.output(12,GPIO.HIGH)
                GPIO.output(16,GPIO.LOW)
        except KeyboardInterrupt:
            print('\nCTRL C -Exiting')
            GPIO.cleanup()   #cleanup the output
            print('Done')
            sys.exit() #exit

    rate_cnt +=1            #Revolutions / time
    tot_cnt +=1             #Total revolutions since program start
    time_end = time.time()  #end od measurement time
    
    flowRate = round((rate_cnt * constant) / (time_end - time_start),2)  #flowRate(L/min)
    totalMilliLitres = round((tot_cnt * constant) /100,2)            #total Millilitres
    now_str = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')          #e.g. 2016-04-18T06:12:25.877Z

    lcd.message("Total MilliLitres:\n"+str(totalMilliLitres)+"L\n")
    
    #store the water usage data in the local Raspberry pi
    data = [now_str, flowRate, totalMilliLitres]
    with open(csvfile, "a") as output:
        writer = csv.writer(output, delimiter = ",", lineterminator = '\n')
        writer.writerow(data)
   
   # publish the sensor date into Power BI dataset.
    REST_API_URL = 'https://api.powerbi.com/beta/eb1c9d1a-e6e8-4097-87fe-bb01690935b7/datasets/002569fb-d54b-4fdf-b0c4-e1ce04571822/rows?key=BjabD7GeJIqHajemX3cHiXZttSKo4wR4lzBRGigb1aWhlFw6KWwA0VhTjRPxysJi%2FRWqdiHQMVWkNFQ3FHtqqA%3D%3D'
    
    HEADER = ["DateTime", "flowRate", "totalMilliLitres"]
    data_row =[]
    data_row.append(data)
    print("Raw data - ", data_row)
    data_df = pd.DataFrame(data_row, columns=HEADER)
    data_json = bytes(data_df.to_json(orient='records').encode('utf-8'))
    print("JSON dataset", data_json)
     
    # Post the data on the Power BI API
    req = requests.post(REST_API_URL, data_json)

    print("Data posted in Power BI API")

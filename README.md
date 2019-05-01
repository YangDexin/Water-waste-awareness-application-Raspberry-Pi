# Real-time Water Waste Awareness Application-Raspberry Pi
## Introduction: 

In this project, I need to set up the Raspberry Pi, water flow sensors and wirelessly collect water usage data. Then, based on the usage data the light bulb should change the lighting colour. The changing light colour will reflect the water usage for that day, which will make the residents aware and more responsible for their usages.
After that, I will show you how to create a Power BI Streaming Real Time Dashboards.

## Why we need to Conserve Water?
https://www.youtube.com/watch?v=paVt_WZJ0B8 [1]

It minimizes the effects of drought and water shortages. Even though our need for fresh water sources is always increasing because of population and industry growth, the supply we have stays constant. Even though water eventually returns to Earth through the water cycle, it's not always returned to the same spot, or in the same quantity and quality. By reducing the amount of water we use, we can better protect against future drought years.It helps to preserve our environment. Water conservation requires forethought and effort, but every little bit helps. Don't think that what you do does not matter. We can all make changes in our lifestyles to reduce our water usage.[2]

## How to use this project?
Track you water usage for you kitchen, washroom, yard or office.
Give the people a warning when the usage is too high.

## A basic design diagram:
<p align="center">
<img width="653" alt="screen shot 2019-03-05 at 5 43 26 pm" src="https://user-images.githubusercontent.com/18043807/53911363-07baa080-400b-11e9-9e14-9e8d38eafb2f.png">
</p>

## Step 1:
#### Get all the equimpent for Amazon:

1. CanaKit Raspberry Pi 3 B+ (B Plus) Starter Kit:
https://www.amazon.ca/gp/product/B07BCC8PK7/ref=ppx_yo_dt_b_asin_title_o02_s01?ie=UTF8&psc=1

2. DIGITEN G1/2" Water Flow Hall Sensor:
https://www.amazon.ca/gp/product/B00VKATCRQ/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1

3. Elegoo Upgraded Electronics Fun Kit (you may not need all of them, but it is a good deal):
https://www.amazon.ca/Electronics-Precision-Potentiometer-tie-points-Breadboard/dp/B01ERPEMAC/ref=sr_1_27_sspa?crid=3PHLP7VQ5GIU6&keywords=breadboard&qid=1551905109&s=industrial&sprefix=bread%2Cindustrial%2C199&sr=1-27-spons&th=1

4. 16x2 LCD Screen: 
https://www.amazon.ca/RoboJax-LCD1602-Screen-Character-Interface/dp/B071WJ2S4K/ref=sr_1_1?crid=3P5U9CNM194MP&keywords=lcd+1602&qid=1551905724&refinements=p_85%3A5690392011&rnid=5690384011&rps=1&s=industrial&sprefix=lcd%2Cindustrial%2C429&sr=1-1

###### You may not need this:
~~5. 120pcs Breadboard Jumper:
https://www.amazon.ca/gp/product/B01C84WKN0/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1~~

## Step 2:
#### Set up the Raspberry Pi:
There is a detailed video shows how to set up a Raspberry Pi:[3] 
https://www.youtube.com/watch?v=juHoJYX86Dg

When you start to buy a new Raspberry Pi, I do recommend using an SD card with a minimum capacity of 8GB. Then Using a computer with an SD card reader, visit [this page](https://www.raspberrypi.org/downloads/) to download Raspbian which is the Raspberry Pi official operating system

<p align="center">
<img width="653" alt="screen shot 2019-03-05 at 5 43 26 pm" src=https://user-images.githubusercontent.com/18043807/53994990-9c470080-40e8-11e9-8cb9-208ffc056e68.jpeg>
</p>

## Step 3[4]:
#### Set up [VNC server](https://www.raspberrypi.org/documentation/remote-access/vnc/) :
Sometimes it is not convenient to work directly on the Raspberry Pi. Maybe you would like to work on it from another device by remote control.
**VNC** is a graphical desktop sharing system that allows you to remotely control the desktop interface of one computer (running VNC Server) from another computer or mobile device (running VNC Viewer).

##### Enabling VNC Server
On your Raspberry Pi, run the following commands to make sure you have **the latest version of VNC Connect**:
```ruby
sudo apt-get update

sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
```
Now enable VNC Server. You can do this graphically or at the command line.

##### Enabling VNC Server graphically: Ensure VNC is Enabled.
<p align="center">
<img width="677" alt="screen shot 2019-03-08 at 10 24 38 am" src="https://user-images.githubusercontent.com/18043807/54047692-90147f00-418c-11e9-83be-e485c5c788cd.png">
</p>

On your Raspberry Pi, run the following commands to find **your IP address**:
```ruby
sudo ifconfig
```

<p align="center">
<img width="392" alt="screen shot 2019-03-08 at 10 30 39 am" src="https://user-images.githubusercontent.com/18043807/54048008-69a31380-418d-11e9-8c67-3c5336c7649b.png">
</p>

For testing, you can connect to Raspberry Pi by using your IP address to see whether it works or not.
<p align="center">
<img width="577" alt="screen shot 2019-03-08 at 10 36 35 am" src="https://user-images.githubusercontent.com/18043807/54048276-2e551480-418e-11e9-80d8-3c027a1a3f12.png">
</p>

##### If it works properly, just go ahead to [download VNC Server](https://www.realvnc.com/en/connect/download/vnc/).Then you can start to connect the VNC server.
<p align="center">
<img width="925" alt="screen shot 2019-03-08 at 10 40 43 am" src="https://user-images.githubusercontent.com/18043807/54048534-f4384280-418e-11e9-9035-1fe9754da139.png">
</p>

## Step 4:
###### Make sure water flow sensor works properly (include code[5]):
Before we statr to build this project, you should know each of the 40-pins of the GPIO port. 
<p align="center">
<img width="925" alt="screen shot 2019-03-08 at 10 40 43 am" src="https://user-images.githubusercontent.com/18043807/54049429-52febb80-4191-11e9-9f67-edd5f0d62c6c.png">
</p>

Then follow this diagram to connect your water flow sensor to Raspberry Pi:

<p align="center">
<img width="925" alt="screen shot 2019-03-08 at 10 40 43 am" src="https://user-images.githubusercontent.com/18043807/54054735-d2938700-419f-11e9-8bee-8c94f2ba633c.jpeg">
</p>

**Coding part**:

```ruby
#!/usr/bin/python
#Python program for FL-480 water flow sensor
#Working range : 1-30 L/min
#Water Pressure: <=1.75 Mpa
#Import GPIO,time, sys and csv library
import RPi.GPIO as GPIO
import time, sys
from datetime import datetime
import csv

#name csv file as "WaterFlowData"
csvfile = "WaterFlowData.csv"

#referring to the pins by the "Broadcom SOC channel" number
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
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
            None
        except KeyboardInterrupt:
            print('\nCTRL C -Exiting')
            GPIO.cleanup()   #cleanup the output
            print('Done')
            sys.exit() #exit
        
    rate_cnt +=1            #Revolutions / time
    tot_cnt +=1             #Total revolutions since program start
    time_end = time.time()  #end od measurement time
    
    flowRate = round((rate_cnt * constant) / (time_end - time_start),2)  #flowRate(L/min)
    totalLitres = round((tot_cnt * constant) /100,2)        #total Litres
    now_str = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ') #e.g. 2016-04-18T06:12:25.877Z
    
    print('\n',flowRate , 'Liters / min')
    print('totalLitres:',totalLitres)
    print('Current Time:' , '\t', now_str,'\n')

    #store the water usage data in the local Raspberry pi 
    data = [flowRate, totalLitres]
    with open(csvfile, "a") as output:
        writer = csv.writer(output, delimiter = ",", lineterminator = '\n')
        writer.writerow(data)
```

**Output:**
<p align="center">
<img width="353" alt="Screen Shot 2019-03-08 at 11 40 35 AM" src="https://user-images.githubusercontent.com/18043807/54052131-7b3de880-4198-11e9-8c63-1b81424a7811.png">
</p>

## Step 5:
###### Make sure light bulb works properly (include code):
After water flow sensor works well, we will start to add light bulb in the project.

**Accessories:**

1. Breadboard
2. Jumper Cable
3. LED’s red-green Ø 5mm
4. Resistors (2 * 220 Ω)

Then follow this diagram to connect Light bulb to Raspberry Pi:

<p align="center">
<img width="607" alt="Screen Shot 2019-03-08 at 5 29 53 PM" src="https://user-images.githubusercontent.com/18043807/54064307-e521b680-41c7-11e9-848c-2e95e301e427.png">
</p>

**Coding part**:

```ruby
# set pin 16 to control Green light bulb
# set pin 12 to control Red light bulb
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
```

```ruby
# If the total usage is over 50 Liter, the lighting color will be changed to red.
# you can set any number you want.
if (round((tot_cnt * constant) / 100,2)) <= 50:
                GPIO.output(16,GPIO.HIGH)
                GPIO.output(12,GPIO.LOW)
                    #time.sleep(1)
            else:
                GPIO.output(12,GPIO.HIGH)
                GPIO.output(16,GPIO.LOW)
```

## Step 6:
###### Make sure LCD screen works properly (include code):

**Required Library:**
In this example, I am going to install and use the library from Adafruit. It’s designed for Adafruit LCD boards but will also work with other brands as well. If your display board uses an HD44780 controller, then it should work with no issues at all.

First, clone the required git directory to the Raspberry Pi by running the following command.
```ruby
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
```
Next change into the directory we just cloned and run the setup file.
```ruby
cd ./Adafruit_Python_CharLCD
sudo python setup.py install
```
Once it’s finished installing you can now call the Adafruit library in any Python script on the Pi. To include the library just add the following line at the top of the python script. You can then initialize the board and perform actions with it.
```ruby
import Adafruit_CharLCD as LCD
```
**Accessories:**

1. Resistors (10K Ω)
2. 16×2 LCD with header pins
3. Breadboard
4. Jumper Cable

Then follow this diagram to connect 16 * 2 LCD to Raspberry Pi:

<p align="center">
<img width="722" alt="Screen Shot 2019-03-08 at 10 26 33 PM" src="https://user-images.githubusercontent.com/18043807/54067149-56299400-41f1-11e9-8810-ef36c0029999.png">
</p>

**Coding part**:
It’s important that before you run any of these examples that you update the pin variables at the top of the file. If you followed my circuit the values below are the correct ones.
```ruby
# Raspberry Pi pin setup
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
```

Then the LCD screen will display the total Litres:
```ruby
lcd.message("Total Litres:\n"+str(totalLitres)+"L\n")
            #lcd.message("Usage:"+str(totalLitres)+"L"+"     ")
```
**The output should look like this picture**
<p align="center">
<img width="319" alt="Screen Shot 2019-03-08 at 10 56 00 PM" src="https://user-images.githubusercontent.com/18043807/54067940-43b45800-41fb-11e9-88c4-b2dc832c5095.jpeg">
</p>

## Step 7:
###### Clean up the data every midnight (include code):
The easy way to do this is to **[Scheduling tasks with Cron]**(https://www.raspberrypi.org/documentation/linux/usage/cron.md)[7]

**Cron GUI**
A graphical application for Cron is available by installing the **gnome-schedule** package:
```ruby
sudo apt-get install gnome-schedule
```
You can then launch the program Scheduled Tasks from the main menu.

**Editing crontab**
Run **crontab** with the **-e** flag to edit the cron table:
```ruby
crontab -e
```
**Add a scheduled task**
The layout for a cron entry is made up of six components: minute, hour, day of month, month of year, day of week, and the command to be executed.
```ruby
# m h  dom mon dow   command
```

```ruby
# * * * * *  command to execute
# ┬ ┬ ┬ ┬ ┬
# │ │ │ │ │
# │ │ │ │ │
# │ │ │ │ └───── day of week (0 - 7) (0 to 6 are Sunday to Saturday, or use names; 7 is Sunday, the same as 0)
# │ │ │ └────────── month (1 - 12)
# │ │ └─────────────── day of month (1 - 31)
# │ └──────────────────── hour (0 - 23)
# └───────────────────────── min (0 - 59)
```
For example:
It will reboot the Raspberry Pi every midnight.
```ruby
0 0 * * * sudo reboot
```

For this project, we need to record the water usage data **per day**, it means we should **restart and clean up the data every midnight**. So reboot Raspberry Pi at midnight and re-run the program after 2 minutes.
<p align="center">
<img width="576" alt="Screen Shot 2019-03-08 at 10 41 19 PM" src="https://user-images.githubusercontent.com/18043807/54067319-680c3680-41f3-11e9-9e19-6f8ca7b17ebd.png">
</p>

## Step 8:
###### Sending data into Power BI dataset and create a real-time bashboard (include code):[8]
1. Go to the [Power BI](https://powerbi.microsoft.com/en-us/) and create your own account.
2. Sign to create a **streaming dataset** by using **API**.

<p align="center">
<img width="319" alt="Screen Shot 2019-03-08 at 10 56 00 PM" src="https://user-images.githubusercontent.com/18043807/54067523-d94ce900-41f5-11e9-86d5-1863f58ce1db.png">
</p>

<p align="center">
<img width="541" alt="Screen Shot 2019-03-08 at 10 56 07 PM" src="https://user-images.githubusercontent.com/18043807/54067529-dfdb6080-41f5-11e9-9a03-b715b2a6338b.png">
</p>

3. Enter a name for the streaming dataset, the name of the columns and data type.
**Make sure the datatype of the values is correct and turn on the "Historic data analysis" because we want to store the data into dataset**
<p align="center">
<img width="549" alt="Screen Shot 2019-04-30 at 4 37 13 PM" src="https://user-images.githubusercontent.com/18043807/57000011-97418300-6b66-11e9-8c35-569308e9acf5.png">
</p>

4. Copy the **Publish URL** becasue Power BI would provides an API tp publish the data.
<p align="center">
<img width="537" alt="Screen Shot 2019-03-08 at 11 13 20 PM" src="https://user-images.githubusercontent.com/18043807/54067697-08fcf080-41f8-11e9-8712-b2a127ec8ee7.png">
</p>


5. Install pandas and requests python library in your Raspberry Pi.

```ruby
sudo apt-get install python-pip
sudo pip install pandas
sudo pip install requests
```

6. Add the URL into the Python code.

```ruby
# import library.
import pandas as pd
import requests

    # Add your own URL to publish data into your dataset.
    REST_API_URL = 'Your own URL'
    
    HEADER = ["DateTime", "flowRate", "totalLitres"]
    data_row =[]
    data_row.append(data)
    print("Raw data - ", data_row)
    data_df = pd.DataFrame(data_row, columns=HEADER)
    data_json = bytes(data_df.to_json(orient='records').encode('utf-8'))
    print("JSON dataset", data_json)
     
    # Post the data on the Power BI API
    req = requests.post(REST_API_URL, data_json)

    print("Data posted in Power BI API")
```
7. Create a bashboard 
<p align="center">
<img width="942" alt="Screen Shot 2019-03-08 at 11 25 37 PM" src="https://user-images.githubusercontent.com/18043807/54067968-942bb580-41fb-11e9-85e1-5abfd235909d.png">
</p>

8. Add title and choose your dataset to create a streaming data diagram such as line chart, car, column chart and so on.
<p align="center">
<img width="524" alt="Screen Shot 2019-03-08 at 11 43 25 PM" src="https://user-images.githubusercontent.com/18043807/54068021-58452000-41fc-11e9-80d1-2d0e32925e0b.png">
</p>

# Congratulations!!! we have finished all of the steps, let's make it works.

**Real-time Bashboard**
<p align="center">
<img width="524" alt="Screen Shot 2019-03-08 at 11 43 25 PM" src="https://user-images.githubusercontent.com/18043807/57001034-6748ae80-6b6b-11e9-861f-caa45e39a11e.gif">
</p>

**All data is in the dataset**
<p align="center">
<img width="583" alt="54077029-bf4bee80-4267-11e9-90b4-baaac703728d" src="https://user-images.githubusercontent.com/18043807/57000871-85fa7580-6b6a-11e9-98e2-52c93598d436.png">
</p>

**Mobile version of Power BI**
<p align="center">
<img width="583" alt="Screen Shot 2019-03-09 at 12 28 44 PM" src="https://user-images.githubusercontent.com/18043807/57000989-19cc4180-6b6b-11e9-9e9a-3907f3b893d3.png">
</p> 

**After one week, one month or one year, you are able to create your own weekly, monthly or yearly report:**
<p align="center">
<img width="766" alt="Screen Shot 2019-03-26 at 8 02 08 PM" src="https://user-images.githubusercontent.com/18043807/55047480-2c020f80-5002-11e9-991d-37a54b762ea2.png">
</p>    


# Reference:
###### [1] Short Film For Save Water: https://www.youtube.com/watch?v=paVt_WZJ0B8
###### [2] Benefits of Water Conservation: https://www.thebalancesmb.com/conservation-efforts-why-should-we-save-water-3157877
###### [3] Getting Started with Raspberry Pi 3: https://www.youtube.com/watch?v=juHoJYX86Dg
###### [4] VNC (Virtual Network Computing): https://www.raspberrypi.org/documentation/remote-access/vnc/
###### [5] RPi 23.1 - YF-S201 Water Flow Meter/Sensor, Polling, IMPULSE Trigge: https://www.youtube.com/watch?v=0fqoq1jWlts&t=345s
###### [6] 16×2 LCD Module Control Using Python: https://www.raspberrypi-spy.co.uk/2012/07/16x2-lcd-module-control-using-python/
###### [7] Scheduling tasks with Cron: https://www.raspberrypi.org/documentation/linux/usage/cron.md
###### [8] Power BI Streaming Real Time Dashboards https://www.youtube.com/watch?v=dXpFciYOVsc&index=41&list=PLyD1XCIRA3gT0Yg9RrKhPE30hSEKTVZWL

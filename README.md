# Water waste awareness application-Raspberry Pi
## Introduction: 

In this project, I need to set up the Raspberry Pi, water flow sensors and wirelessly collect water usage data. Then, based on the usage data the light bulb should change the lighting colour. The changing light colour will reflect the water usage for that day, which will make the residents aware and more responsible for their usages.
After that, I will show you how to create a Power BI Streaming Real Time Dashboards.

## Why we need to Conserve Water?
https://www.youtube.com/watch?v=paVt_WZJ0B8 [1]

It minimizes the effects of drought and water shortages. Even though our need for fresh water sources is always increasing because of population and industry growth, the supply we have stays constant. Even though water eventually returns to Earth through the water cycle, it's not always returned to the same spot, or in the same quantity and quality. By reducing the amount of water we use, we can better protect against future drought years.It helps to preserve our environment. Water conservation requires forethought and effort, but every little bit helps. Don't think that what you do does not matter. We can all make changes in our lifestyles to reduce our water usage.[2]

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
###### Make sure water flow sensor works properly (include coding[5]):
Before we statr to build this project, you should know each of the 40-pins of the GPIO port. 
<p align="center">
<img width="925" alt="screen shot 2019-03-08 at 10 40 43 am" src="https://user-images.githubusercontent.com/18043807/54049429-52febb80-4191-11e9-9f67-edd5f0d62c6c.png">
</p>

Then follow this diagram to connect your water flow sensor to Raspberry Pi:



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
    totalMilliLitres = round((tot_cnt * constant) /100,2)        #total Millilitres
    now_str = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ') #e.g. 2016-04-18T06:12:25.877Z
    
    print('\n',flowRate , 'Liters / min')
    print('totalMilliLitres:',totalMilliLitres)
    print('Current Time:' , '\t', now_str,'\n')

    #store the water usage data in the local Raspberry pi 
    data = [flowRate, totalMilliLitres]
    with open(csvfile, "a") as output:
        writer = csv.writer(output, delimiter = ",", lineterminator = '\n')
        writer.writerow(data)
```

**Output:**
<p align="center">
<img width="353" alt="Screen Shot 2019-03-08 at 11 40 35 AM" src="https://user-images.githubusercontent.com/18043807/54052131-7b3de880-4198-11e9-8c63-1b81424a7811.png">
</p>

## Step 5:
###### Make sure light bulb works properly (include coding):

## Step 6:
###### Make sure LCD screen works properly (include coding):

## Step 7:
###### clearning up the data every minight (include coding):


## Step 8:
###### Sending data into Power BI dataset and create a real-time bashboard (include coding):










# Reference:
###### [1] Short Film For Save Water: https://www.youtube.com/watch?v=paVt_WZJ0B8
###### [2] Benefits of Water Conservation: https://www.thebalancesmb.com/conservation-efforts-why-should-we-save-water-3157877
###### [3] Getting Started with Raspberry Pi 3: https://www.youtube.com/watch?v=juHoJYX86Dg
###### [4] VNC (Virtual Network Computing): https://www.raspberrypi.org/documentation/remote-access/vnc/
###### [5] RPi 23.1 - YF-S201 Water Flow Meter/Sensor, Polling, IMPULSE Trigge: https://www.youtube.com/watch?v=0fqoq1jWlts&t=345s

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


## Step 4:
###### Make sure water flow sensor works properly (include coding):

## Step 5:
###### Make sure light bulb works properly (include coding):

## Step 6:
###### Make sure LCD screen works properly (include coding):

## Step 7:
###### clearning up the data every minight (include coding):


## Step 8:
###### Sending data into Power BI dataset and create a real-time bashboard (include coding):










#Reference:
[1] Short Film For Save Water: https://www.youtube.com/watch?v=paVt_WZJ0B8
[2] Benefits of Water Conservation: https://www.thebalancesmb.com/conservation-efforts-why-should-we-save-water-3157877
[3] Getting Started with Raspberry Pi 3: https://www.youtube.com/watch?v=juHoJYX86Dg
[4] VNC (Virtual Network Computing): https://www.raspberrypi.org/documentation/remote-access/vnc/

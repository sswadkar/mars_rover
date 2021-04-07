<html>
<p align="center">
<img src="https://user-images.githubusercontent.com/63820563/112520863-3f235380-8d72-11eb-8887-e8e97a85b63a.png" width="220" height="200">
</p>
</html>

# Mars Environmental Meteorological Sensor
Using Arduino to measure temperature, humidity, and wind speed; uploading that data to a MongoDB connected to Docker; and reading that data in Python and turning into an interactive map with data collection points.

## Methods

1. Although not integrated into MEMS, the rover should have a speedometer that the program can access to determine whether the rover is moving

2. If the rover is moving, MEMS will turn on and start collecting data periodically: every one second

3. Every second MEMS will collect 4 different things
  * Measures wind speed separately (does the following steps over the course of a second)
    * Regardless of whether there is wind or not, the photoresistor creates an array of light values over a second
    * MEMS measures the number of times the wind turbine passes over the photoresistor to count rotations
    * Compares the number of rotations to a calibrated wind speed ratio that’s predetermined
    * Creates an output of wind speed in miles per hour
  * The temperature and Humidity sensor collects two pieces of instantaneous data
    * Temperature reading
    * Humidity value
  * RTC Clock Module collects time at which the data was collected
  * At the end of the second, the Arduino outputs the time the data was collected, the temperature, the humidity, and the wind speed in mph
  * MEMS has its own designated database that is connected to the rover’s Linux-based system
    * The Arduino directly outputs the temperature, humidity, wind speed, and time into the database so that once MEMS isn’t in use the data isn’t lost

4. After MEMS has sent the data to its local database the process repeats itself (go back to step 3) until the end condition has been met

5. Once the rover stops moving, MEMS will stop collecting data as the rover is now stationary
  * This is to preserve the sensors and not unnecessarily collect data when unneeded

## Materials

1. Arduino
2. Photoresistor
3. Temperature Sensor
4. RTC Clock Module
5. Breadboard
6. 8 male-to-male wires
7. 5 male-to-female wires
8. 1 resistor
9. 8.5 x 11 in. paper
10. Crab hammer
11. Elevated base

### Arduino Sensors

The code is in the files and this [Tinkercad](https://www.tinkercad.com/things/3Bx4iry3SNl-glorious-juttuli-waasa/editel?sharecode=aK2YVIqy-7f960M9g8wX9HleBGZAU93_4haH3hX_W7Y) link should explain how to wire the temperature module and the photoresistor so that it works with the code. The code won't run without the dependencies (linked below).

###### Sensors used (and wiring):
1. [Temperature Module](https://www.tinkercad.com/things/3Bx4iry3SNl-glorious-juttuli-waasa/editel?sharecode=aK2YVIqy-7f960M9g8wX9HleBGZAU93_4haH3hX_W7Y)
2. [Photoresistor](https://www.tinkercad.com/things/3Bx4iry3SNl-glorious-juttuli-waasa/editel?sharecode=aK2YVIqy-7f960M9g8wX9HleBGZAU93_4haH3hX_W7Y)
3. [RTC Clock Module](https://www.instructables.com/Arduino-Nano-DS1302-Real-Time-ClockRTC-With-Visuin/)

## Build Instructions

### Step 1. Windmill base
* Create an origami windmill base: Instructions obtained from this [link](https://www.origami-resource-center.com/windmill-base.html)
 * Cut the rectangular sheet of paper into a square sheet of paper
 * Take a square sheet of paper and fold it in half left-to-right, and then unfold.
 * Fold in half again (top-to-bottom), and unfold.
 * Fold the left-edge and right-edge of the paper towards the center to align with the vertical crease. Unfold.
 * Fold the top-edge and bottom-edge of the paper towards the center to align with the horizontal crease. Unfold.
 * Fold the paper along the diagonal in both directions to form a X-shaped crease. Unfold. Flip the paper over.
 * Perform the blintz fold (fold the four corners towards the center of the paper). Unfold.
 * Turn the paper over: step 5a shows the crease pattern. You are now ready to collapse the paper into a windmill base;
 * Refold the crease located ¼ of the distance from the bottom edge of the paper. At the same time, refold the crease located ¼ of the way from the right edge of the paper.
 * An extra flap of paper will be formed. Swivel this extra flap of paper towards the right. Alternatively, you can swivel the flap downwards, but you have to be consistent as to which direction to fold subsequent flaps.
 * Rotate the paper clockwise 90 degrees.
 * Repeat the process by refolding the crease ¼ from the right edge of the paper. A second flap will be formed: swivel it towards the right.
 * Rotate the paper clockwise 90 degrees.
 * Repeat the process one last time: valley fold the bottom layer ¼ from the right edge of the paper. This forms two more flaps, swivel the lower flap towards the  right and top flap upwards.
* Take your crab hammer and dot the middle of the hammer with a pen/marker
* Poke a hole through the center of your origami turbine and hammer the tack into the point you marked on your crab hammer
* Attach your crab hammer to a base of your choice as long as the windmill base is hovering over the ground and the hammer is perpendicular to your base

### Step 2. Wiring terminals
* Connect 1 male-to-male wire from 5V to one positive terminal
* Connect 1 male-to-male wire from 3.3V to the other positive terminal
* Connect 1 wire from GND to any ground terminal

### Step 3. Setting up the Temperature Module
* Place the temperature module onto the breadboard.
* Connect 1 male-to-male wire from the positive (+) port of the Temperature Module to the 5.5V red terminal.
* Connect 1 male-to-male wire from out port to digital port 8 on the Arduino.
* Connect 1 male-to-male wire from the ground (-) port of the Temperature Module to the ground port.

### Step 4. Setting up the Photoresistor
* Place the photoresistor onto the breadboard.
* Connect 1 male-to-male wire from the cathode to the 3.3V red terminal.
* Connect 1 resistor from the anode to another terminal
* Connect 1 male-to-male wire from the resistor to analog pin A0.
* Connect 1 male-to-male wire from the resistor to GND black terminal.

### Step 5: Setting up the RTC Clock Module
* Place the Clock Module onto the breadboard
* Connect 1 male-to-female wire from VCC to 5V red terminal.
* Connect 1 male-to-female wire from GND to GND black terminal.
* Connect 1 male-to-female wire from CLK to port 7 on the Arduino.
* Connect 1 male-to-female wire from TAD to port 6 on the Arduino.
* Connect 1 male-to-female wire from RSD to port 5 on the Arduino.

## Dependencies
1. Node.js
2. Docker
3. Python pymongo
4. Python matplotlib
5. Arduino DHTLib *(Temperature Sensor)*
6. Arduino DS3231 *(RTC Clock Module)*

**Fork this repository into a folder called `mars_rover`**

## JavaScript

#### Node.js

In the JavaScript file, change the SerialPort usbmodem to the one specific to your computer (when you click Serial Monitor the numbers and letters in the top middle of the Serial Monitor and replace it with what's currently in the file)


In the app folder, you need to download all the dependencies that come with the Arduino program

```cd app```

```npm install```


That should download all the Javascript modules that `server.js` uses.

## Docker

#### Docker Installation

[Docker](https://www.docker.com/get-started) is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.

To download docker
1. [Mac OS](https://docs.docker.com/docker-for-mac/install/)
2. [Windows](https://docs.docker.com/docker-for-windows/install-windows-home/)

Once you have Docker downloaded open up terminal and type in

```docker-compose up --detach```

This will start the containers in the `docker-compose.yml` in the background and leave them running.

To test whether they're running type in

```docker ps```

It should result in (or something similar)

```
CONTAINER ID   IMAGE           COMMAND                  CREATED      STATUS        PORTS                      NAMES
c2b3587af792   mongo-express   "tini -- /docker-ent…"   2 days ago   Up 13 hours   0.0.0.0:8080->8081/tcp     mars_rover_mongo-express_1
1ab49fd629e6   mongo           "docker-entrypoint.s…"   2 days ago   Up 13 hours   0.0.0.0:27017->27017/tcp   mars_rover_mongodb_1
```

#### MongoDB set-up

Type in `localhost:8080` and it should take you to a MongoDB Express webpage that's a user interface for MongoDB

Add a database called `mars_data` and click on that database

Then add a collection called `time`

Then plug in your Arduino and type in 

```node server.js```

If all goes well, it should display data from the Arduino and if you refresh the MongoDB express page it'll update the database every second with new data.

## Python

#### Pymongo

Go into terminal and type in

```pip install pymongo```

#### Matplotlib

Go into terminal and type in

```pip install matplotlib```

## Arduino

#### Arduino DHTLib

Download the [DHTLib](https://www.circuitbasics.com/wp-content/uploads/2015/10/DHTLib.zip) library and export it into Arduino

#### Arduino DS3231

Download the [DS3231](https://github.com/msparks/arduino-ds1302) library and export it into Arduino

Go into File->Examples->arduino_ds3231_master->set_clock

And set the RTC Clock to the current time (explained in file) so that the RTC Clock Module is up to date

## Directions for Operating the Instrument

Connect the Arduino via the USB cable and upload the Arduino code to your Arduino. Lines 24 and 25 will need to be changed for calibration (line 24 is a known wind speed you've measured and line 25 is the max amount of rotations you've seen your windmill produce).

Then, in terminal, type in 

```node server.js```

This will begin the data collection process

You can start simulating a Mars rover moving on the surface, and the data will automatically be collected every second.

**The Python Mapping Program will not update with every new addition to the database so run it at the end**

Once you're done collecting the data, press Ctrl+C in the terminal that's running `server.js`

In the same terminial, type in 

```python backend.py``` 

A new window should pop-up. This window is the MatPlotLib map that the program generated. You can pan/zoom around in order to access specific data points. When you click a certain data point, the time, temperature, humidity, and wind speed for that specific point will be displayed in your terminal.





## Known Issues

1. RTC Clock Module reverts to original time (1/1/2000 @ 00:00:00)

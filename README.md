<html>
<p align="left">
<img src="https://user-images.githubusercontent.com/63820563/112520863-3f235380-8d72-11eb-8887-e8e97a85b63a.png" width="220" height="200">
</p>
</html>

# Mars Environmental Meteorological Sensor
Using Arduino to measure temperature, humidity, and wind speed; uploading that data to a MongoDB connected to Docker; and reading that data in Python and turning into an interactive map with data collection points.

## Scientific Objective

The Mars Environmental and Meteorological Sensor (MEMS) 's primary objective is to analyze Mars' temperature, humidity, and wind speed to determine the possibility of human exploration and colonization on Mars. Rovers are limited and require abstractions, whereas humans can adapt and receive instructions/debug; hence, human space exploration is vital to understanding Mars better. In order to send humans to Mars, we need to evaluate the habitability of Mars. To determine this, MEMS will measure temperature, humidity, and wind speed to determine what we will need to build to help humans survive on Mars. Measuring temperature allows us to gauge the temperature ranges on Mars, a crucial factor in determining the habitability of a planet. Measuring humidity is vital in collecting information on the amount of water in the air and the potential for agriculture on Mars. Finally, wind speeds allow us to determine seasonal wind patterns to understand better how the passage of time works on Mars and associating certain meteorological phenomena with the time of the year.

## Background Research (Previous Missions)

In 2010, NASA conducted The Genesis and Rapid Intensification Processes (GRIP) experiment to better understand how tropical storms form and develop into major hurricanes. From August 15th to September 30th, 2010, the GRIP deployment was capitalized on a number of ground networks, airborne science platforms, and space-based assets. NASA collected satellite and aircraft field campaign data to conduct research on problems related to the formation and intensification of hurricanes.
One of the devices that NASA used in the GRIP experiment was an expendable weather reconnaissance device called dropsondes to measure atmospheric state parameters such as temperature, humidity, wind speed/direction, and pressure. The dropsonde is designed to be dropped out of an aircraft, and during the descent, the GPS dropsonde collects data of the surrounding atmosphere and sends data back to the aircraft by radio transmission. The dropsonde uses a GPS receiver to detect wind speed and wind direction through analysis of the GPS latitude and longitude points. The dropsonde also contains pressure, temperature, and humidity sensors that capture vertical profiles of atmospheric thermodynamic data. The dropsonde has an advantage over other data collection methods because it is great at capturing vertical profile data during severe weather. Similar to how GRIP was used to better understand the weather, MEMS will also analyze the temperature, humidity, and wind speed of Mars in order to study the weather and determine the possibility of future human exploration on Mars.

The Mars Science Laboratory mission was created in order to determine the habitability of Mars. The Curiosity rover was created to carry out this mission. The mission began on November 26th, 2011. At that point, the Curiosity rover carried the most advanced scientific instruments ever sent to the surface of Mars. It brought along advanced technology to fulfill its task, such as a radioisotope battery, which generates power from the decay of plutonium. It landed in the Gale Crater on August 6, 2012. Its general mission is also to determine if Mars ever had the right environmental conditions to support microscopic life. 


One sensor that was included in Curiosity was REMS. REMS measures a plethora of data about the weather on Mars. Some of the data measures atmospheric pressure, temperature, humidity, and wind speeds. It was designed to survive in very hot and cold conditions. REMS also contains sensors that monitor the ultraviolet radiation at the Martian surface. Using this, REMS can correlate the radiation in relation to changes in other variables, granting further insight into the environment of the Martian surface. The main science objectives of REMS are to find out more about the general circulation of Mars, its micro-scale weather systems, its Subsurface habitability, the destructive capabilities of UV radiation, and the local water cycle(diurnal water vapor). The overarching purpose of these measurements is to learn more about the weather on Mars, in order to learn more about the viability of habitation. REMS relates to our MEMS sensor, because our sensor will also measure temperature, humidity, and wind speed in order to collect data as REMS does, so we can draw our own conclusions about the viability of habitation on the Martian surface.

The final mission conducted by NASA that uses similar sensors like the ones MEMS is planning to use is the Mars 2020 mission. NASA announced that they would be conducting another Mars mission by sending a new rover, Perseverance, to the red planet on July 30th, 2020. On February 18th, 2021, Perseverance successfully landed in the Jezero Crater and started collecting data. As the NASA mission website highlights, there are four main purposes of the Mars 2020 mission. To look for habitability, seek biosignatures, caching samples, and eventually prepare for humans. The Perseverance rover carries out the Mars 2020 mission by identifying past environments that are/were capable of supporting microbial life, seeking signs for post microbial life -- particularly in rocks designed to preserve life, collect soil samples that are crucial to analyzing the environment, and testing oxygen levels in the Martian atmosphere.

A sensor that plays a key role in this process is The Mars Environmental Dynamics Analyzer, also known as MEDA. MEDA measures temperature, humidity, wind speed and direction, and the amount and size of dust particles in the Martian atmosphere. Specifically, MEMS aims to focus on three of the five things that MEDA measures, temperature, humidity, and wind speed. MEDA measures temperature on Mars to help astronauts know what weather conditions they'll face on Mars. Their safety depends on accurate weather predictions. MEDA measures humidity on Mars to determine how water vapor is exchanged between the "soil" and atmosphere on Mars. Finally, MEDA measures wind patterns in order to help identify weather patterns that are crucial to understanding if NASA wishes to send humans to Mars one day. These three measurements are what MEMS will also measure as some, not all, of the vital factors in determining the logistics and practicality of human exploration on Mars.

## Materials and Methods

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
* Connect 1 male-to-male wire from the positive (+) port of the Temperature Module to the 5V red terminal.
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

## Data Collection Analysis

There are four key measurements that MEM’s will be collecting every second. Wind speed, temperature, humidity, and time at which the measurement was taken. 

First, on collecting wind speed, the windmill base is placed above the photoresistor and during data collection every second it collects an array of light values. After collecting that array of light values over the second, the instrument measures the number of times the light value increased/decreased a set amount. If there is no wind, then the windmill base wouldn’t move at all and so the light value would be constant throughout the second and the oscillations of the windmill base would be 0. If there is wind, the light values would change multiple times over the second as the windmill base would switch between covering and not covering the photoresistor. The instrument then takes the number of times the light values jumped a certain threshold in a consecutive measurement and then applies a formula that is obtained from calibration (number of revolutions multiplied by the maximum set wind speed in miles per hour divided by the maximum number of revolutions measured). After applying this formula, the Mars rover is able to determine the wind speed at a given second.

Next on collecting temperature and humidity, the temperature module is used for collecting the temperature in celsius and relative humidity. The relative humidity is the amount of water in the air in relation to the maximum amount of water vapor. The temperature does not require any additional calculations and returns a value between 0 to 50 degrees celsius. Humidity also does not require any additional calculations and the range is from 20 to 90%. 

Finally, on collecting time, the RTC Clock Module is used for collecting time and date data for other information collected from the sensor, in order to identify trends and other insights over time. Data is recorded every second, which is determined using the Arduino’s internal timer. The internal clock within the Arduino resets when the Arduino shuts off, but the RTC Clock Module is powered by a separate battery, which guarantees uptime in order to collect more accurate results.

Since Mars is a foreign environment with a different climate altogether, MEMs plans to use wind speed and current knowledge about the martian climate to better understand how to predict weather patterns. Wind sends sediment into the martian atmosphere creating dust storms, which have an effect on surface albedo and temperatures. Analyzing wind speeds also increase scientists’ understanding of heat, aerosols, dust particles, and other natural phenomena as stronger/faster winds can be used to identify circulation patterns (similar to the Hadley circulation on Earth), trade winds, and weather patterns. Having similar wind patterns (when looking at speed) to Earth would enable scientists to determine the proper location/technology that humans would need for human exploration/habitation. Analyzing temperature readings would allow scientists to understand temperature fluctuations throughout the day and night cycle in order to find out how to design technology in order for humans to sustain life on Mars during human exploration. Measuring and analyzing humidity would allow scientists to understand the water cycle on Mars in order to consider the future of agriculture or even human habitability on Mars. If temperature fluctuations are drastic with temperatures changing from large positive values to large negative values in celsius then scientists could disregard the possibility of human habitability and might just focus on human exploration. On the contrary, seeing similar temperature and humidity patterns to Earth might encourage scientists to further investigate the possibility of human habitation.

## Citations

* "Complete Guide for DHT11/DHT22 Humidity and Temperature Sensor With Arduino" ["Complete Guide for DHT11/DHT22 Humidity and Temperature Sensor With Arduino"]. Random Nerd Tutorials, 25 Apr. 2019, randomnerdtutorials.com/complete-guide-for-dht11dht22-humidity-and-temperature-sensor-with-arduino/. Accessed 15 Apr. 2021.
Earth Observing Laboratory. "What is a Dropsonde?" UCAR, www.eol.ucar.edu/content/what-dropsonde. Accessed 21 Mar. 2021.

* Global Hydrology Resource Center. "Genesis and Rapid Intensification Processes (GRIP)." NASA, ghrc.nsstc.nasa.gov/home/field-campaigns/grip. Accessed 21 Mar. 2021.

* Guzewich, Scott, et al. "Measuring Mars Atmospheric Winds from Orbit" ["Measuring Mars Atmospheric Winds from Orbit"]. arXiv, edited by Scott Guzewich, 15 July 2020, arxiv.org/ftp/arxiv/papers/2007/2007.05412. Accessed 19 Apr. 2021. 

* "How to Use a Real-Time Clock Module." Arduino Project Hub, create.arduino.cc/projecthub/MisterBotBreak/how-to-use-a-real-time-clock-module-ds3231-bc90fe. Accessed 19 Apr. 2021.

* Jet Propulsion Laboratory. "Mars Science Laboratory Curiosity Rover." NASA, www.jpl.nasa.gov/missions/mars-science-laboratory-curiosity-rover-msl. Accessed 21 Mar. 2021.

* NASA. "Aircraft and Instruments." NASA, www.nasa.gov/mission_pages/hurricanes/missions/grip/instruments/index.html#dc8. Accessed 21 Mar. 2021.

* ---. "GRIP Hurricane Mission." NASA, www.nasa.gov/mission_pages/hurricanes/missions/grip/overview/. Accessed 21 Mar. 2021.

* ---. "Mars Exploration Program." NASA, mars.nasa.gov/mars-exploration/missions/mars-science-laboratory/. Accessed 21 Mar. 2021.

* ---. "Mars 2020 Mission Perseverance Rover." NASA, mars.nasa.gov/mars2020/. Accessed 21 Mar. 2021.

* ---. "MEDA." NASA, mars.nasa.gov/mars2020/spacecraft/instruments/meda/. Accessed 21 Mar. 2021.

* Origami Resource Center. "Origami Windmill Base." origami-resource-center.com, 2020, www.origami-resource-center.com/windmill-base.html. Accessed 19 Apr. 2021.



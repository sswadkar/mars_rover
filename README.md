# Arduino Weather Collector
Using Arduino to measure temperature, humidity, and wind speed; uploading that data to a MongoDB connected to Docker; and reading that data in Python and turning into an interactive map with data collection points.

## Arduino Sensors

The code is in the files and this [Tinkercad](https://www.tinkercad.com/things/3Bx4iry3SNl-glorious-juttuli-waasa/editel?sharecode=aK2YVIqy-7f960M9g8wX9HleBGZAU93_4haH3hX_W7Y) link should explain how to wire the temperature module and the photoresistor so that it works with the code. The code won't run without the dependencies (linked below).

###### Sensors used (and wiring):
1. [Temperature Module](https://www.tinkercad.com/things/3Bx4iry3SNl-glorious-juttuli-waasa/editel?sharecode=aK2YVIqy-7f960M9g8wX9HleBGZAU93_4haH3hX_W7Y)
2. [Photoresistor](https://www.tinkercad.com/things/3Bx4iry3SNl-glorious-juttuli-waasa/editel?sharecode=aK2YVIqy-7f960M9g8wX9HleBGZAU93_4haH3hX_W7Y)
3. [RTC Clock Module](https://www.instructables.com/Arduino-Nano-DS1302-Real-Time-ClockRTC-With-Visuin/)

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
2. [Windows](https://docs.docker.com/docker-for-windows/install/)

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

## Running the programs

Connect the Arduino via the USB cable and in one terminal type in 

```node server.js```

This will begin the data collection process

**The Python Mapping Program will not update with every new addition to the database so run it at the end**

Once you're done collecting the data, Ctrl C in the terminal that's running `server.js`

In the same terminial, type in 

```python backend.py``` 

A new window should pop-up. This window is the MatPlotLib map that the program generated. You can pan/zoom around in order to access specific data points. When you click a certain data point, the time, temperature, humidity, and wind speed for that specific point will be displayed in your terminal.

## Known Issues

1. RTC Clock Module reverts to original time (1/1/2000 @ 00:00:00)

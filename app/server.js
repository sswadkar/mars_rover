const PORT = 5000;
let express = require('express');
let path = require('path');
let fs = require('fs');
let MongoClient = require('mongodb').MongoClient;
let bodyParser = require('body-parser');
let app = express();

app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(bodyParser.json());

let mongoUrlLocal = "mongodb://admin:password@localhost:27017";

let mongoUrlDocker = "mongodb://admin:password@mongodb";

let mongoClientOptions = { useNewUrlParser: true, useUnifiedTopology: true };

//database name is "mars_data"
//database collection name is "time"
let databaseName = "mars_data";

const SerialPort = require('serialport');
const Readline = require('@serialport/parser-readline');
const port = new SerialPort('/dev/cu.usbmodem144401', { baudRate: 9600 });
const parser = port.pipe(new Readline({ delimiter: '\n' }));

parser.on('data', data => {
    MongoClient.connect(mongoUrlLocal, mongoClientOptions, function (err, client) {
        if (err) throw err;
        let db = client.db(databaseName);
        db.collection("time").insertOne(stringToJSON(data), function(err, res) {
            if (err) throw err;
            client.close();
          });
    });
    console.log('got word from arduino:', data);
    sleep(1000);
});

function stringToJSON(str){
    var info = str.replace(/(\r\n|\n|\r)/gm, "").split(" ");
    return JSON.parse('{ "dayOfWeek":"' + info[0] + '", "date":"' + info[1] + '", "time":"' + info[2] + '", "temp":"' + info[3] + '", "humidity":"' + info[4] + '", "wspeed":"' + info[5] + '"}');
}
const sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
  }

app.listen(PORT, function () {
  console.log(`app listening on port ${PORT}!`);
});
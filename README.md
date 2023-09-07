# MQTT_DataSensors
This code used for transmit data sensors to server or other devices that needs data sensors to display. It can used for protocol data transfer to remote control machine. 

## Prerequisites
* Sqlite 3, we need store our data sensors to database, we used sqlite3 because it's free. Install using command `sudo apt-get install sqlite3`
* Paho MQTT, to provides a client class which enable applications to connect to an MQTT broker to publish messages, and to subscribe to topics and receive published messages, for source [link](https://pypi.org/project/paho-mqtt/). Install using command `pip install paho-mqtt`
* Python Serial, to built connection from Arduino to our devices, we used python serial for detected Arduino interface. Install using command `pip install pyserial`


import sqlite3
import paho.mqtt.client as mqtt
import datetime
import serial
import time
import random 

broker_addr = "[IP_TARGET]"
serial_port = "[ARDUINO_PORT]"
DBname      = "[DATABASE_NAME].dB"


def DB_Connections():
    connect = sqlite3.connect(DBname)
    return connect

def Check_Table():
    try:
        connect = DB_Connections()
        print("\n\nDatabase '", DBname, "' was Successfull to Connect...")
        MyScheme = """
        CREATE TABLE IF NOT EXISTS LDR_Sensor(
        id integer primary key autoincrement,
        ID_Sensor text,
        Times timestamp,
        Data text
        );
        """
        connect.execute(MyScheme)
        connect.close()
    except:
        print("Failed to CREATE a TABLE!")

def InputDataSensor(serial_port,count,ID_Sensor):
    Check_Table()
    try:
        ser = serial.Serial(serial_port, 9600)
        print("Connect to Serial Monitor was Success...") 
        try:
            DBconnect = DB_Connections()
            try:
                client = mqtt.Client("[TARGET_NAME]")
                client.connect(broker_addr)
                time.sleep(2)

                for i in range(count):
                    load = ser.readline()
                    Decoder = load.decode(errors='ignore')
                    Data = Decoder.rstrip()
                    inputData = (ID_Sensor, datetime.datetime.now(), str(Data))
                    DBconnect.execute("INSERT INTO LDR_Sensor (ID_Sensor, Times, Data) VALUES (?,?,?)", inputData)
                    DBconnect.commit()
                    time.sleep(0.01)
                    client.publish("[MQTT_TOPIC]", Data)
                    print("\nSending ", Data, " to MQTT Broker")
                DBconnect.close()
                ser.close()
            except:
                print("Cannot Connect to MQTT Broker...")    
        except:
            print("Cannot Connect to Database...")
    except:
        print("Cannot Find Serial Monitor...")




InputDataSensor(serial_port,[NUMBER_OF_DATA],[ID_SENSOR_NAME])
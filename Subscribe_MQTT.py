# Import semua library yang dibutuhkan
import sqlite3
import paho.mqtt.client as mqtt
import datetime

# Inisialisasi variabel
DBname = "[].db"
broker_address = "202.46.3.87"
client = mqtt.Client("Gateway")
client.connect(broker_address)

# Fungsi untuk membuat koneksi ke database 
def DB_Connections():
    Myconn = sqlite3.connect(DBname)
    return Myconn
   
# Cek tabel untuk menyimpan data sensor
def Check_Table():
    try:
        connect = DB_Connections()
        print("\n\nDatabase '", DBname, "' was Successfull to Connect...")
        MyScheme = """
        create table if not exists LDR_Sensor(
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

Check_Table()
# Input data sensor yang telah diambil dari publisher ke database
def on_message(client, userdata, message):
    connect = DB_Connections()

    ID_Sensor = "LDR@2023"
    Data = str(message.payload.decode("utf-8"))
    inputData = (ID_Sensor, datetime.datetime.now(), Data)
    print("Input ", Data, " to database")

    connect.execute(" INSERT INTO LDR_Sensor (ID_Sensor, Times, Data) VALUES (?,?,?)", inputData)
    connect.commit()
    connect.close()

# Proses pengiriman data dari publisher ke subsciber
while True:
    client.subscribe("ldr/cond")
    client.on_message = on_message
    client.loop_forever()

# To be run on Mu 1.2.0 editor, CircuitPython.

# -------------------------------------------------------------------------------
# Import statements
# -------------------------------------------------------------------------------

import pandas as pd
from bm_serial import BristlemouthSerial
import board
import digitalio
import time
from utils.utils import TempSensor
from utils.machine import Pin
from utils.onewire import OneWire
from utils.ds18x20 import DS18X20

# -------------------------------------------------------------------------------
# Set up pins for the DS18B20
# -------------------------------------------------------------------------------

p12 = Pin(12, Pin.OUT)  # Pin 12 is power supplied to the DS18B20, V+
p12.value(1)            # set Pin 12 to 3V

ow = OneWire(Pin(13))   # Pin 13 is the data pin for the DS18B20
ds = DS18X20(ow)        # Initialize a ds18b20 object

# -------------------------------------------------------------------------------
# LED initialization
# -------------------------------------------------------------------------------

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
bm = BristlemouthSerial()

# -------------------------------------------------------------------------------
# Set up save file
# -------------------------------------------------------------------------------

file_name = "/data.csv"

if file_name not in os.listdir("/"):
    with open(file_name, "w") as f:
        f.write("Timestamp,Sensor1,Details\n")

# -------------------------------------------------------------------------------            
# Get continuous temperature measurements
# -------------------------------------------------------------------------------

last_send = time.time()

while True:
    now = time.time()
    if now - last_send > 60:
        led.value = True
        last_send = now
        roms = ds.scan()    # Repeat the scan, in case we've added or removed a temp sensor (we won't be doing this)
        ds.convert_temp()   # Obtain a temperature reading
        temp_info = ds.read_temp(rom)
        print("publishing", now)
        print("temp info", temp_info)
        #bm.spotter_tx(b"sensor1: 1234.56, binary_ok_too: \x00\x01\x02\x03\xff\xfe\xfd")
        bm_serial.spotter_log(
            "any_file_name.log",
            "Sensor 1: 1234.56. More detailed human-readable info for the SD card logs.",
        )
        
        with open(file_name, "a") as f:
            f.write(f"{now},{temp_info},{details}\n")
            
        led.value = False
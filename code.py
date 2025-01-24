# To be run on Mu 1.2.0 editor, CircuitPython.

# Write your code here :-)
import pandas as pd
from bm_serial import BristlemouthSerial
import board
import digitalio
import time
from utils import TempSensor

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
bm = BristlemouthSerial()
last_send = time.time()

file_name = "/data.csv"

if file_name not in os.listdir("/"):
    with open(file_name, "w") as f:
        f.write("Timestamp,Sensor1,Details\n")

while True:
    now = time.time()
    if now - last_send > 60:
        led.value = True
        last_send = now
        print("publishing", now)
        #bm.spotter_tx(b"sensor1: 1234.56, binary_ok_too: \x00\x01\x02\x03\xff\xfe\xfd")
        bm.spotter_log(
            "any_file_name.log",
            "Sensor 1: 1234.56. More detailed human-readable info for the SD card logs.",
        )
        
        with open(file_name, "a") as f:
            f.write(f"{now},{sensor1_value},{details}\n")
            
        led.value = False
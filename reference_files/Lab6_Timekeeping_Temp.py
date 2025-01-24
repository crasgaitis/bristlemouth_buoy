# This script prints temperature readings from a DS18B20 sensor

from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms
from ustruct import unpack

datafile = open("TempTime.csv", "a")

# -------------------------------------------------------------------------------
# Set up pins for the DS18B20
# -------------------------------------------------------------------------------

p12 = Pin(12, Pin.OUT)  # Pin 12 is power supplied to the DS18B20, V+
p12.value(1)            # set Pin 12 to 3V

ow = OneWire(Pin(13))   # Pin 13 is the data pin for the DS18B20
ds = DS18X20(ow)        # Initialize a ds18b20 object

# -------------------------------------------------------------------------------
# Set up the clock
# -------------------------------------------------------------------------------

import urtc
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda = Pin(4))
rtc = urtc.DS3231(i2c)

# -------------------------------------------------------------------------------            
# Get continuous temperature measurements
# -------------------------------------------------------------------------------

while(True):            # This will repeat in a loop, until we terminate with a ctrl-c
    roms = ds.scan()    # Find all the DS18B20 sensors that are attached (we only have one)
    ds.convert_temp()   # Obtain temp readings from each of those sensors

    for rom in roms:    # Loop through all the temp sensors attached (again, for our purposes we only have 1)

        # get the current time for the measurement
        t = rtc.datetime()
        
        # save time as a string with format YYYY/MM/DD/ HH:MM:SS
        time = str(str(t.year) + '/' + str(t.month) + '/' + str(t.day) +  ' ' +
                  str(t.hour) + ':' + str(t.minute) + ':' + str(t.second))
        
        print(time, ",", ds.read_temp(rom)) # print the sample number and temperature
        
        datafile.write(str(time) + ',' + str(ds.read_temp(rom)) + "\n")
        
        sleep_ms(1000)  # Sleep for 1 sec
        
datafile.close() #if you terminate the loop, you'll need to run this command to close the csv file
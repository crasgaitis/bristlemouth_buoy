# This script prints temperature readings from a DS18B20 sensor

from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms
from ustruct import unpack


# -------------------------------------------------------------------------------
# Set up pins for the DS18B20
# -------------------------------------------------------------------------------

p12 = Pin(12, Pin.OUT)  # Pin 12 is power supplied to the DS18B20, V+
p12.value(1)            # set Pin 12 to 3V

ow = OneWire(Pin(13))   # Pin 13 is the data pin for the DS18B20
ds = DS18X20(ow)        # Initialize a ds18b20 object

# -------------------------------------------------------------------------------            
# Get continuous temperature measurements
# -------------------------------------------------------------------------------

seconds=0            # Start sampling at 0 seconds

while(True):            # This will repeat in a loop, until we terminate with a ctrl-c
    seconds+=1       # Increment the sample number for each reading
    roms = ds.scan()    # Repeat the scan, in case we've added or removed a temp sensor (we won't be doing this)
    ds.convert_temp()   # Obtain a temperature reading

    for rom in roms:    # Loop through all the temp sensors attached (again, for our purposes we only have 1)

        #print(sample_num, ',', ds.read_temp(rom)) # print the sample number and temperature
        print(ds.read_temp(rom)) # print the sample number and temperature
        sleep_ms(1000)  # Sleep for 1 second (1000 milliseconds)
        
from bm_serial import BristlemouthSerial
import board
import digitalio
import time
import adafruit_bmp280
import adafruit_tsl2591
i2c = board.I2C()
sensorL = adafruit_tsl2591.TSL2591(i2c)


from adafruit_onewire.bus import OneWireBus
import adafruit_ds18x20
ow_bus = OneWireBus(board.D5)
devices = ow_bus.scan()
ds18b20 = adafruit_ds18x20.DS18X20(ow_bus, devices[0])
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
bm = BristlemouthSerial()
last_send = time.time()

i2c = board.I2C()
sensorAP = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

while True:
    now = time.time()
    if now - last_send > 15:
        led.value = True
        last_send = now
        print("publishing", now)

        #bm.spotter_tx(b"sensor1: 1234.56, binary_ok_too: \x00\x01\x02\x03\xff\xfe\xfd")
        bm.spotter_log(
            "Temperature_test.log",
            "Sensor 1:"+'Temperature: {0:0.3f} °C'.format(ds18b20.temperature)+ " 'Temperature: {} degrees C'".format(sensorAP.temperature)+'Pressure: {}hPa'.format(sensorAP.pressure)+'Light: {0}lux'.format(sensorL.lux)
        )
        led.value = False

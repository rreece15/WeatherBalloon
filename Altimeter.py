import time, datetime
import board
import adafruit_bme280.advanced as adafruit_bme280
import csv

#creating sensor object from board's i2c bus
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

#TODO: change this before flight!!!
bme280.sea_level_pressure = 1033.31
bme280.mode = adafruit_bme280.MODE_NORMAL
bme280.standby_period = adafruit_bme280.STANDBY_TC_500
bme280.iir_filter = adafruit_bme280.IIR_FILTER_X16
bme280.overscan_pressure = adafruit_bme280.OVERSCAN_X16
bme280.overscan_humidity = adafruit_bme280.OVERSCAN_X1
bme280.overscan_temperature = adafruit_bme280.OVERSCAN_X2

time.sleep(1)

filename = "PATH TO CSV FILE"

with open(filename, 'w') as csvfile: #closes independently
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Time', 'Temperature', 'Humidity', 'Pressure', 'Altitude'])
    while True:
        csvwriter.writerow([datetime.datetime.now(), bme280.temperature, bme280.relative_humidity, bme280.pressure, bme280.altitude])
        time.sleep(10)

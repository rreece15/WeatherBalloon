import time
import board
import busio

import adafruit_gps

import csv

uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=10)

gps = adafruit_gps.GPS(uart, debug=False)

gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")

last_time = time.monotonic()
with open('gps_data.csv', dialect='excel', newline='') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while True:
        gps.update()
        current = time.monotonic()
        if current - last_time >= 1.0:
            last_time = current
            if not gps.has_fix:
                print("waiting for fix...")
                continue
            print("=" * 40)
            print(
                "Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(
                    gps.timestamp_utc.tm_mon,
                    gps.timestamp_utc.tm_mday,
                    gps.timestamp_utc.tm_year,
                    gps.timestamp_utc.tm_hour,
                    gps.timestamp_utc.tm_min,
                    gps.timestamp_utc.tm_sec,
                )
            )
            print("Latitude: {0:.6f} degrees".format(gps.latitude))
            print("Longitude: {0:.6f} degrees".format(gps.longitude))
            print("Fix quality: {}".format(gps.fix_quality))
            datawriter.writerow([gps.timestamp_utc.tm_mon,
                    gps.timestamp_utc.tm_mday,
                    gps.timestamp_utc.tm_year,
                    gps.timestamp_utc.tm_hour,
                    gps.timestamp_utc.tm_min,
                    gps.timestamp_utc.tm_sec,
                    float({0:.6f}.format(gps.latitude)),
                    float({0:.6f}.format(gps.longitude))])

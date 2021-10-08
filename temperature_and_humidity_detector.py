import RPi.GPIO as GPIO
import dht11
import time
from datetime import datetime
import csv

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=17)

try:
	result = instance.read()
	if result.is_valid():
		datafile = open('data/temperate_and_humidity.csv', 'a+', newline='')
		with datafile:
			header = ['year', 'month', 'day', 'hour', 'minutes', 'seconds', 'temperature', 'humidity']
			now = datetime.now()
			writer = csv.DictWriter(datafile, fieldnames = header)
			writer.writerow(
				{
					'year' : now.strftime("%Y"), 
					'month': now.strftime("%m"), 
					'day': now.strftime("%d"),
					'hour': now.strftime("%H"),
					'minutes': now.strftime("%M"),
					'seconds': now.strftime("%S"),
					'temperature': result.temperature,
					'humidity': result.humidity, 
				}
			)

except KeyboardInterrupt:
		print("Cleanup")
		GPIO.cleanup()

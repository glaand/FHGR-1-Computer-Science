import RPi.GPIO as GPIO
import dht11
import time
from datetime import datetime
import csv
import sqlite3 

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=17)

try:
	result = instance.read()
	if result.is_valid():
		conn = sqlite3.connect('data.db')
		now = datetime.now()
		row = {
			'year' : now.strftime("%Y"), 
			'month': now.strftime("%m"), 
			'day': now.strftime("%d"),
			'hour': now.strftime("%H"),
			'minutes': now.strftime("%M"),
			'seconds': now.strftime("%S"),
			'temperature': result.temperature,
			'humidity': result.humidity, 
		}
		conn.execute("INSERT INTO temp_and_humi (year,month,day,hour,minutes,seconds,temperature,humidity) \
		VALUES ({year}, {month}, {day}, {hour}, {minutes}, {seconds}, '{temperature}', '{humidity}')".format(**row))
		conn.commit()
		conn.close()
except KeyboardInterrupt:
		print("Cleanup")
		GPIO.cleanup()

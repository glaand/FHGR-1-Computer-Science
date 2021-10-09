import RPi.GPIO as GPIO
import time as t
from datetime import datetime, time
import os
import csv
import sqlite3

def detect_sound():
    GPIO.setmode(GPIO.BCM)
    SOUND_PIN = 16
    GPIO.setup(SOUND_PIN, GPIO.IN)

    def DETECTED(SOUND_PIN):
        now_time = datetime.now().time()
        start_time = time(23, 0)
        end_time = time(8, 0)

        if now_time < start_time or now_time > end_time:
            return

        conn = sqlite3.connect("{0}/data.db".format(os.getcwd()))
        now = datetime.now()
        row = {
			'year' : now.strftime("%Y"), 
			'month': now.strftime("%m"), 
			'day': now.strftime("%d"),
			'hour': now.strftime("%H"),
			'minutes': now.strftime("%M"),
            'sound_cnt': 1
		}
        conn.execute("UPDATE sound SET sound_cnt = sound_cnt + 1 WHERE year = {year} AND month = {month} AND day = {day} AND hour = {hour} AND minutes = {minutes}".format(**row))
        conn.commit()
        conn.execute("INSERT OR IGNORE INTO sound (year,month,day,hour,minutes,sound_cnt) VALUES ({year}, {month}, {day}, {hour}, {minutes}, {sound_cnt})".format(**row))
        conn.commit()
        conn.close()

    try:
        GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, callback=DETECTED)
        while True:
            t.sleep(1000)
    except KeyboardInterrupt:
        print(" Quit")
        GPIO.cleanup()

detect_sound()

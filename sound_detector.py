import RPi.GPIO as GPIO
import time
from datetime import datetime
import os
import daemon
import lockfile
import csv

def detect_sound():
    GPIO.setmode(GPIO.BCM)
    SOUND_PIN = 16
    GPIO.setup(SOUND_PIN, GPIO.IN)

    def DETECTED(SOUND_PIN):
        datafile = open('data/sound.csv', 'a+', newline='')
        with datafile:
            header = ['year', 'month', 'day', 'hour', 'minutes', 'seconds', 'sound_cnt']
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
                    'sound_cnt': 1,
                }
            )

    try:
        GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, callback=DETECTED)
        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        print(" Quit")
        GPIO.cleanup()

#with daemon.DaemonContext(pidfile=lockfile.FileLock('./sound_detector.pid')):
detect_sound()

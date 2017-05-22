#!/usr/bin/env python
import schedule
from os import system
import time

schedule.every().hour.do(system("/usr/src/app/retweet.py")

while True:
    schedule.run_pending()
    time.sleep(1)

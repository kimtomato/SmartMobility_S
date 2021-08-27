#!/usr/bin/python3

import Jetson.GPIO as GPIO
import time

led = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT, initial=GPIO.HIGH)

print("Start blink demo now, press CTRL + C to exit")
value = GPIO.HIGH

try:
    while True:
        time.sleep(1)
        print(f"Outputting {value} to pin {led}")
        GPIO.output(led, value)
        value ^= GPIO.HIGH
finally:
    GPIO.cleanup()

#!/usr/bin/python3

import subprocess, datetime, time
from RPLCD.i2c import CharLCD

cmd = "hostname -I | awk '{print $1}'"
res = subprocess.check_output(cmd, shell=True)
ip = res.decode().strip()

lcd = CharLCD('PCF8574', 0x27)
lcd.write_string(ip)
while True:
    lcd.cursor_pos = (1,0)
    now= datetime.datetime.now()
    lcd.write_string(f'{now: %m/%d %H:%M:%S}')
    time.sleep(1)
    

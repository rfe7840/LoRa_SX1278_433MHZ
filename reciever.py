#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from serial import Serial


port = 'COM4'
s = Serial(port, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.001, xonxoff=0, rtscts=0)
while True:
    res = s.read()
    print(res)
    sleep(1)
	
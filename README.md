# LoRa_SX1278_433MHZ
Serial communication with LoRa_SX1278 chip in Python

## Required Parts

* Two LoRa_Sx1278 chips (https://de.aliexpress.com/item/32791728376.html?spm=a2g0s.9042311.0.0.27424c4dq19rAK) 
* Two Antennas (https://de.aliexpress.com/item/32998198933.html?spm=a2g0s.9042311.0.0.27424c4dq19rAK)
* Several Jumper Wires
* Two Devices which are able to communicate over UART Level (Raspberry Pi3, ESP32, etc.)
* For using the lora device on a windows device i used this USB zu TTL Seriell Adapter Konverter with FTDI FT232RL (https://www.amazon.de/gp/product/B07BBPX8B8/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1)

## Wiring

For easy serial communication just cross out TX and RX line and put M0 and M1 Pin to GND and do as follow:
![alt text](https://github.com/rfe7840/LoRa_SX1278_433MHZ/blob/main/1_lora_sx1278_433mhz.jpg)

## Example Code

I had the test programm only on a windows device.(on ESP32[with micropython] and Raspberry code will follow soon) I used therefore the FTDI FT232RL chip. I used two short programms. 
One program for sending and one for recieving.
Reciever Programm:
```
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

```
Sender Programm:
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from serial import Serial

port = 'COM3'
s = Serial(port, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.001, xonxoff=0, rtscts=0)

while True:
  s.write('testdata')
  sleep(1)

```






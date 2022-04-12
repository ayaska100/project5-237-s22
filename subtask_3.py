#!/usr/bin/env python3
from movement import tank237
from ev3dev2.sensor import Color_Sensor
import time

tank = tank237('outA', 'outD')  # left/right motors

colorsensor = Color_Sensor()

# start near front of box
# TODO: insert whatever needs to be inserted to get the robot relatively (~6inches)
# in front of the box. the only consequnces besides overshooting (very bad. fail)
# is that the robot will slowly approach the box.

correct_barcode = 3

print("CORRECT BARCODE: " + correct_barcode)
print("SCANNED BARCODE: " + tank.c_scan_barcode())

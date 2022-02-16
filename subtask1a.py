#!/usr/bin/env python3
from ev3dev2.motor import MoveTank
from time import sleep
from movement import move_cm

tank = MoveTank('outA', 'outD')

# subtask values given at demo
y = 50  # distance to move
n = 4  # laps to run (one lap is y cm forward and y cm back)

for i in range(n):
    move_cm(tank, y)
    sleep(0.2)
    move_cm(tank, -y)
    sleep(0.2)

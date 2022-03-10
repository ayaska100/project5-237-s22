#!/usr/bin/python3
from movement import tank237
from time import sleep
from ev3dev2.sensor.lego import GyroSensor
# from ev3dev2 import SpeedPercent

# initialization
tank = tank237('outA', 'outD')  # left/right motors

tank.c_move_cm(2.54 * 12)
tank.c_turn_degrees(-90)
tank.c_move_cm(2.54 * 84)

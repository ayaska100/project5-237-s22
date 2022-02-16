#!/usr/bin/env python3
from ev3dev2.motor import MoveTank
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
from movement import move_cm, turn_180

tank = MoveTank('outA', 'outD')

move_cm(tank, 50)
move_cm(tank, -50)
sleep(2)
move_cm(tank,30)
turn_180(tank)
move_cm(tank,30)
turn_180(tank)

# # grab the gyrosensor and assign it to the tank, calibrate to initialize angle
# tank.gyro = GyroSensor()
# tank.gyro.calibrate()

# def turn_180_gyro():  # experimental: uses gyro sensor
#     tank.turn_degrees(speed=30, target_angle=180)

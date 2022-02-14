#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor

DEF_SPEED = 50  # default speed

tank = MoveTank(OUTPUT_A, OUTPUT_D)

tank.on_for_seconds(DEF_SPEED, DEF_SPEED, 2)
tank.on_for_seconds(-DEF_SPEED, -DEF_SPEED, 2)


def move_cm(distance): # move x cm
    # this NEEDS to be calibrated TODO TODO TODO TODO
    # essentially. a coefficient of 1 would mean 1 second takes you 1 centimeter
    # time = distance/5 means 5 cm per second
    time = distance / 5

    # this also impacts the distance
    # leave it alone if device is calibrated, touch only if needed
    rspeed = lspeed = 50

    tank.on_for_seconds(rspeed, lspeed, time)


def turn_180(): # manual function
    speed = 80
    time = 1 # TODO CALIBRATE
    tank.on_for_seconds(speed, -speed, time) #turns clockwise

# grab the gyrosensor and assign it to the tank, calibrate to initialize angle
tank.gyro = GyroSensor()
tank.gyro.calibrate()

def turn_180_gyro(): # experimental: uses gyro sensor
    tank.turn_degrees(speed=30, target_angle=180)

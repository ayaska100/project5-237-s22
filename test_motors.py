#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor

tank = MoveTank(OUTPUT_A, OUTPUT_D)


def move_cm(distance):  # move a certain amount of cm
    # this impacts the distance - we set it to 50 and calibrate the time around it
    abs_speed = 40

    # the motors can't move for a negative time, but they
    # can move for a positive time at a negative speed
    if (distance > 0):  # if positive
        speed = abs_speed
    elif (distance < 0):  # if negative
        speed = -abs_speed

    # this coefficient was taken through emperical testing
    # NOTE!!!!! this is also dependent on the motor speed!
    # it must be changed if a new speed is chosen
    cm_per_second = 19.6

    # take the absolute value because we cannot have negative time
    time = abs(distance / cm_per_second)

    # on_for_seconds arguments:
    # left speed (0-100), right speed (0-100), time (s)
    tank.on_for_seconds(speed, speed, time)


def turn_180():  # manual function
    # from experience it's easier to calibrate turning on a lower speed
    # plus it leads to a more consistent turn because less jerk
    speed = 30
    time = 1.3  # TODO CALIBRATE
    tank.on_for_seconds(speed, -speed, time)  # turns clockwise


move_cm(20)
turn_180()
move_cm(20)
turn_180()

# # grab the gyrosensor and assign it to the tank, calibrate to initialize angle
# tank.gyro = GyroSensor()
# tank.gyro.calibrate()

# def turn_180_gyro():  # experimental: uses gyro sensor
#     tank.turn_degrees(speed=30, target_angle=180)

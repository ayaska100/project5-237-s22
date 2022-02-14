#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor.lego import GyroSensor

DEFAULT_POWER = 30

# create tank object
# all (?) movement commands are a method on this
tank = MoveTank(OUTPUT_A, OUTPUT_B)



# moving forward is negative due to motors setup
tank.on_for_seconds(-DEFAULT_POWER, -DEFAULT_POWER, 2)
tank.on_for_seconds(DEFAULT_POWER, DEFAULT_POWER, 2)


tank.on_for_seconds(20, 70, 1)
tank.on_for_seconds(70, 20, 1)

# # grab the gyrosensor and assign it to the tank
# tank.gyro = GyroSensor()

# # calibrate the gyro to eliminate drift, and to initialize angle
# tank.gyro.calibrate()

# # pivot 30 degrees
# tank.turn_degrees(
#     speed=SpeedPercent(5),
#     target_angle=30
# )

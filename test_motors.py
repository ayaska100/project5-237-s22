from movement import tank237
from time import sleep
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2 import SpeedPercent

# initialization
tank = tank237('outA', 'outD')

# Initialize the tank's gyro sensor; calibrate gyro sensor and reset position to 0
tank.gyro = GyroSensor()
tank.gyro.calibrate()
tank.gyro.reset()

# Pivot 30 degrees
tank.turn_right(
    speed=SpeedPercent(5),
    degrees=30
)

# movement.turn_180_manual(tank)

# movement.move_cm(50)

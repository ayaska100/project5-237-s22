#!/usr/bin/python3
from ev3dev2.motor import MoveTank


class tank237(MoveTank):
    # extend MoveTank class into custom class
    # prefix new functions with c_ for custom

    def c_move_cm_time(self, distance):
        '''Depricated (use c_move_cm instead).
        Move a certain distance (cm) forward (positive) or backwards (negative).'''
        # this impacts the distance - calibrate the time around it
        speed = 30

        # the motors can't move for a negative time, but they
        # can move for a positive time at a negative speed
        if (distance < 0):  # if negative
            speed *= -1

        # this coefficient was taken through emperical testing
        # NOTE!!!!! this is also dependent on the motor speed!
        # it must be changed if a new speed is chosen
        seconds_per_cm = 0.063

        # take the absolute value because we cannot have negative time
        # extra bit because. robot undershot short distances but overshot large distances
        time = seconds_per_cm * abs(distance) + 0.0075

        # on_for_seconds arguments:
        # left speed (0-100), right speed (0-100), time (s)
        self.on_for_seconds(speed, speed, time)

    # wheel diameter 5.6cm = about 17.6 cm circumference - tune to reality
    def c_move_cm(self, distance):
        # this function is speed indepenendent bc it track the rotation of the
        # wheel which is inherently tied to distance traveled.
        speed = 35

        if (distance < 0):  # if negative
            speed *= -1

        rotations = distance / 17.565
        self.on_for_rotations(speed, speed, rotations)

    def c_turn_degrees(self, degrees):
        '''Manual (hand-tuned) function:
        turns x degrees to the right (negative for left).'''
        # problem: this function is inherently a bit inaccurate because
        # the servos resist movement but have a small wiggle room
        # TODO: use smaller wheels?

        # from experience it's easier to calibrate turning on a lower speed
        # plus it leads to a more consistent turn because less jerk
        speed = 25

        # reverse speed if negative degrees (left turn)
        if degrees < 0:
            speed *= -1

        # constant for converting degrees of turn to seconds of motor runtime
        # units: seconds per full rotation
        coefficient = 2.69  # edit this line

        # abs bc time cannot be negative
        time = coefficient * abs(degrees / 360)

        # aligned to speed. if speed is positive then robot turns clockwise.
        self.on_for_seconds(speed, -speed, time)

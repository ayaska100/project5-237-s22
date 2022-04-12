#!/usr/bin/env python3
from ev3dev2.motor import MoveTank
import time


class tank237(MoveTank):
    # extend MoveTank class into custom class
    # prefix user accessible functions with c_ for custom
    # internal (custom) functions use _ at the beginning for private

    # current x, y coordinates
    # IMPORTANT COORDINATES
    # BASE A: (6, -6)
    # TODO: FILL MORE
    # coordinates are measured to be the point directly between the two front wheels
    _position = (0, 0)

    def c_set_initial_position(self, x, y):
        self._position = (x, y)

    # 0 1 2 3
    # n e s w
    # default orientation is north, unless otherwise given
    _orientation = 0

    def c_set_initial_orientation(self, o):
        assert(0 <= o and o <= 3), "orientation must be in range 0123 (nesw)"

        self._orientation = o

    # update orientation
    # adding 1 means a rotation of 90 deg to the right
    # mod 4 means that turning north from west makes a 0 and not 5
    def _orientation_update_right_turn(self):
        _orientation = (_orientation + 1) % 4

    # same logic as above
    def _orientation_update_left_turn(self):
        _orientation = (_orientation - 1) % 4

    # wheel diameter 5.6cm = about 17.6 cm circumference - tune to reality
    # this is left in becuase its the original implementation. if we need to
    # recalibrate it then just calibrate the inches function instead
    def _move_cm(self, distance):
        # this function is speed indepenendent bc it track the rotation of the
        # wheel which is inherently tied to distance traveled.
        speed = 35

        if (distance < 0):  # if negative
            speed *= -1

        rotations = distance / 17.565
        self.on_for_rotations(speed, speed, rotations)

    # for convenience
    def c_move_in(self, distance):
        self._move_cm(2.54*distance)

    def _turn_degrees(self, degrees):
        # private because every time we turn we HAVE to update the orientation
        # we can't call this manually

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

    def c_turn_right(self):
        self._turn_degrees(90)
        # self._orientation_update_right_turn()

    def c_turn_left(self):
        self._turn_degrees(-90)
        # self._orientation_update_left_turn()

    def c_turn_180(self):
        self._turn_degrees(180)
        # self._orientation_update_right_turn()
        # self._orientation_update_right_turn()

    def c_wait_secs(self, seconds):
        time.sleep(seconds)

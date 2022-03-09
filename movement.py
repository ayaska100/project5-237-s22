from ev3dev2.motor import MoveTank

# extend MoveTank class into custom class
class tank237(MoveTank):
    def move_cm(self, distance):  # move a certain amount of cm
        # this impacts the distance - calibrate the time around it
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
        cm_per_second = 17.2

        # take the absolute value because we cannot have negative time
        time = abs(distance / cm_per_second)

        # on_for_seconds arguments:
        # left speed (0-100), right speed (0-100), time (s)
        self.on_for_seconds(speed, speed, time)

    def turn_180_manual(self):  # manual function
        # from experience it's easier to calibrate turning on a lower speed
        # plus it leads to a more consistent turn because less jerk
        speed = 25
        time = 1.32
        self.on_for_seconds(speed, -speed, time)  # turns clockwise

    def turn_gyro(self, degrees): # turns x degrees cw
        self.turn_degrees(speed=30, target_angle=degrees)


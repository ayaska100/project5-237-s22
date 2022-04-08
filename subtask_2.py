#!/usr/bin/env python3
from movement import tank237

tank = tank237('outA', 'outD')  # left/right motors

# tank.c_set_initial_position(6, -6)

# pull out
tank.c_turn_180()
tank.c_move_in(12)

# go longways
tank.c_turn_left()
tank.c_move_in(96)

# pull in
tank.c_turn_left()
tank.c_move_in(12)

# reorient
tank.c_turn_180()

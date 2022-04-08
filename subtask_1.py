#!/usr/bin/env python3
from movement import tank237

tank = tank237('outA', 'outD')  # left/right motors

# tank.c_set_initial_position(6, -6)

# box 7 to 12
box = 7

tank.c_move_in(36)
tank.c_turn_right()

tank.c_move_in(40)
tank.c_wait_secs(5)
tank.c_move_in(56)

tank.c_turn_right()
tank.c_move_in(36)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from utils.teleop_lib import Teleop


if __name__ == "__main__":
    print("Teleop joy - class version")

    # Defining the max values for velocities
    lin = float(sys.argv[1])
    ang = float(sys.argv[2])

    # Creating the object
    joy = Teleop()
    joy.set_max(max_lin=lin, max_ang=ang)

    joy.run()

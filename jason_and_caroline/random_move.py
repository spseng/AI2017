# Python

import sys
import vex
import random

# Configurations
left_wheels = vex.Motor(10)
right_wheels = vex.Motor(1)

"""Main loop

Picks two random integers from -100 to 100 every
two seconds and run the motors with those numbers
as the power value.
"""
while True:
    left_wheels.run(random.randint(-100, 100))
    right_wheels.run(random.randint(-100, 100))
    sys.sleep(0.5)

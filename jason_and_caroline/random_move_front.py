# Python

import sys
import vex
import random

class RandomMoveBot():
    # Globals
    RAND_DELAY = 2
    BACK_DELAY = 2
    TURN_DELAY = 2
    TICK_TIME = 0.1

    # Number of ticks before setting a new set of random numbers
    RAND_TICK = RAND_DELAY / TICK_TIME
    BACK_TICK = BACK_DELAY / TICK_TIME
    TURN_TICK = TURN_DELAY / TICK_TIME

    """Main loop

    Picks two random integers from -100 to 100 every
    two seconds and run the motors with those numbers
    as the power value. If the bump sensor is
    activated, the robot backs.
    """

    def __init__(self):
        # Configurations
        self.left_wheels = vex.Motor(10)
        self.right_wheels = vex.Motor(1)
        self.bump_front = vex.DigitalInput(1)
        self.bump_back = vex.DigitalInput(2)

        # State
        # Can be one of:
        # - loop
        # - back
        # - forward
        # - left
        # - right
        self.state = "loop"

        # Time Variables
        self.tick_count = 0
        self.back_start = 0
        self.left_start = 0

        self.random_gen()

    def random_gen(self):
        self.left_power = random.randint(20, 100)
        self.right_power = random.randint(20, 100)

    def back(self, power):
        self.left_wheels.run(-power)
        self.right_wheels.run(-power)

    def turn_left(self):
        self.left_wheels.run(30)
        self.right_wheels.run(60)

    def time_since(self, time_variable):
        return self.tick_count - time_variable

    def execute_state(self):
        if self.tick_count % self.RAND_TICK == 0:
            self.random_gen()

        if self.state == "loop":
            self.left_wheels.run(self.left_power)
            self.right_wheels.run(self.right_power)
        elif self.state == "back":
            self.back(80)
            if self.time_since(self.back_start) >= self.BACK_TICK:
                self.state = "right"
                self.right_start = self.tick_count
        elif self.state == "left":
            self.turn_left()
            if self.time_since(self.left_start) >= self.TURN_TICK:
                self.state = "loop"

    def check_inputs(self):
        if self.bump_front.is_on():
            self.state = "back"
            self.back_start = self.tick_count

    def loop(self):
        self.execute_state()
        self.check_inputs()

        self.tick_count += 1
        sys.sleep(self.TICK_TIME)

robot = RandomMoveBot()
while True:
    robot.loop()

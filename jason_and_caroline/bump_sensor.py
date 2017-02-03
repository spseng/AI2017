# Python

import sys
import vex

class SquareBot():
    # Globals
    TOTAL_POWER = 70

    # Configurations
    """Assumes the following:

    Left motor is connected to motor pin 1.
    Right motor is connected to motor pin 10.
    Bump sensor is connected to digital pin 1.
    """
    left_wheels = vex.Motor(1)
    right_wheels = vex.Motor(10)
    bump_sensor = vex.DigitalInput(1)

    def main(self):
        while True:
            self.left_wheels.run(self.TOTAL_POWER)
            self.right_wheels.run(self.TOTAL_POWER)

            if self.bump_sensor.is_on():
                self.back_and_turn()

            print("I was here!")
            sys.sleep(1)

    def back_and_turn(self):
        # Back
        self.left_wheels.run(-self.TOTAL_POWER)
        self.right_wheels.run(-self.TOTAL_POWER)
        sys.sleep(3)

        # Turn right
        self.left_wheels.run(self.TOTAL_POWER)
        self.right_wheels.run(self.TOTAL_POWER/2)
        sys.sleep(2)

myBot = SquareBot()
myBot.main()

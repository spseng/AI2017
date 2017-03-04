# Python
import sys
import vex
import random

class sensor_bot():
    
    #configurations
    
    def __init__(self):
        # Globals
        self.TOTAL_POWER = 30
        
        self.left_wheels = vex.Motor(10)
        self.right_wheels = vex.Motor(1)
        self.bump_sensor = vex.DigitalInput(1)
        self.right_line_tracker = vex.LineTracker(1)
        self.left_line_tracker = vex.LineTracker(2)
        self.serial = vex.Serial(1, 9600)
        self.serial.write("begin")
        sys.sleep(2)
    
    def main(self):
        while (self.left_line_tracker.line_tracker_percent() > 69
                and self.left_line_tracker.line_tracker_percent() > 69):
            self.drive_forward()
        if (self.left_line_tracker.line_tracker_percent() > 69 
                and self.right_line_tracker.line_tracker_percent() < 69):
            self.turn_left()
        elif (self.left_line_tracker.line_tracker_percent() < 69 
                and self.right_line_tracker.line_tracker_percent() > 69):
            self.turn_right()
        elif (self.left_line_tracker.line_tracker_percent() < 69 
                and self.right_line_tracker.line_tracker_percent() < 69):
            self.random_move()
    
    def turn_left(self):
        self.left_wheels.run(self.TOTAL_POWER)
        self.right_wheels.run(-self.TOTAL_POWER)
        
    def turn_right(self):
        self.left_wheels.run(-self.TOTAL_POWER)
        self.right_wheels.run(self.TOTAL_POWER)
        
    def drive_forward(self):
        self.left_wheels.run(self.TOTAL_POWER)
        self.right_wheels.run(self.TOTAL_POWER)
        
    def random_move(self):
        while True:
            left_val = random.randint(-30, 30)
            right_val = random.randint(-30, 30)
            self.left_wheels.run(left_val)
            self.right_wheels.run(right_val)
            sys.sleep(1.5)
            if not (self.left_line_tracker.line_tracker_percent() < 69 
                and self.right_line_tracker.line_tracker_percent() < 69):
                    break
        
    def detect(self):
        self.serial.write("left")
        sys.sleep(0.5)
        self.serial.write(str(self.left_line_tracker.line_tracker_percent()))
        sys.sleep(1)
        
        self.serial.write("right")
        sys.sleep(0.5)
        self.serial.write(str(self.right_line_tracker.line_tracker_percent()))
        sys.sleep(1)

bot = sensor_bot()
while True:
    bot.detect()
    bot.main()

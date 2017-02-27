# Python
import sys
import vex

class sensor_bot():
    #globals
    TOTAL_POWER = 70
    
    #configurations
    
    def __init__(self):
        self.left_wheels = vex.Motor(10)
        self.right_wheels = vex.Motor(1)
        self.bump_sensor = vex.DigitalInput(1)
        self.right_line_tracker = vex.LineTracker(1)
        self.left_line_tracker = vex.LineTracker(2)
        self.serial = vex.Serial(1, 9600)
        self.serial.write("begin")
        sys.sleep(2)
    
    def turn_left(self):
        self.left_wheels.run(self.TOTAL_POWER)
        self.right_wheels.run(-self.TOTAL_POWER)
        
    def turn_right(self):
        self.left_wheels.run(-self.TOTAL_POWER)
        self.right_wheels.run(self.TOTAL_POWER)
        
    def drive_forward(self):
        self.left_wheels.run(self.TOTAL_POWER)
        self.right_wheels.run(self.TOTAL_POWER)
        
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
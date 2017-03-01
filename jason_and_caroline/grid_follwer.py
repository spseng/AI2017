# Python

import sys
import vex
import timer

class Vector():
    """Simple vector with x and y components"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        """Returns string in the form of (x, y)"""
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class GridFollower():
    """A robot that traverses a 3 x 4 grid.
    
    Each cell is bounded by black tape
    """
    
    def __init__(self):
        # Initialize hardware
        self.left_wheels = vex.Motor(10)
        self.right_wheels = vex.Motor(1)
        self.lline_track = vex.LineTracker(2)
        self.rline_track = vex.LineTracker(1)
        self.serial = vex.Serial(1, 9600)
        self.serial.write("begin")

        # Default power
        self.TOTAL_POWER = 60

        # State can be one of [forward, on_tape, off_tape]
        self.state = "forward"
        
        self.lon_tape = False
        self.ron_tape = False

        # Keep track of coordinates
        self.square = Vector(0, 0)

        # Going to the right
        self.direction = Vector(1, 0)

        # Class timer object
        self.timer = timer.Timer()

    def lcd_print(self, content):
        """Helper Function
        
        Prints [content] to the lcd"""
        self.serial.write(content)

    def turn_left(self):
        self.direction.x = 0
        self.direction.y = 1
        
        # Motor turning
        self.left_wheels.run(30)
        self.right_wheels.run(80)
        sys.sleep(1)

    def turn_right(self):
        self.direction.x = 0
        self.direction.y = 1
        
        # Motor turning
        self.left_wheels.run(80)
        self.right_wheels.run(30)
        sys.sleep(1)
    
    def forward(self):
        self.left_wheels.run(self.TOTAL_POWER)
        self.right_wheels.run(self.TOTAL_POWER)

    def stop(self):
        self.left_wheels.off()
        self.right_wheels.off()
    
    def execute_state(self):
        if self.state == "forward":
            self.forward()
            if lon_tape and ron_tape:
                self.state = "on_tape"
        elif self.state == "on_tape":
            self.forward()
            if not lon_tape and not ron_tape:
                self.state = "off_tape"
        elif self.state == "off_tape":
            if self.square.x > 2:
                self.turn_left()
            elif self.square.x < 1:
                self.turn_right()
            elif self.square.x == 3 and self.square.y == 4:
                self.state = "done"
            self.square += self.direction
            self.lcd_print(str(self.square))
            self.state = "forward"
        elif self.state == "done":
            self.stop()
    
    def print_sensor_val(self):
        """Prints out sensor values on the lcd screen
        
        Uses a timing method that doesn't block other functionality
        """
        print_objects = ["left",
                         str(self.lline_track.line_tracker_percent()),
                         "right",
                         str(self.rline_track.line_tracker_percent())]
        index = int(self.timer.elapsed_time()) % 4
        lcd_print(print_objects[index])

    def sense(self):
        if self.lline_track.line_tracker_percent() > 70:
            lon_tape = True

        if self.rline_track.line_tracker_percent() > 70:
            ron_tape = True
    
    def loop(self):
        sense()
        # print_sensor_val()
        execute_state()

bot = GridFollower()
bot.timer.start()
while True:
    bot.loop()

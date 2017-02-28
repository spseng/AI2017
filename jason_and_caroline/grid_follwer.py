# Python

import sys
import vex

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

        # State can be one of [forward, on_tape, off_tape]
        self.state = "forward"
        
        self.lon_tape = False
        self.ron_tape = False

        # Keep track of coordinates
        self.square = Vector(0, 0)

        # Going to the right
        self.direction = Vector(1, 0)

    def lcd_print(self, content):
        """Helper Function
        
        Prints [content] to the lcd"""
        self.serial.write(content)

    def turn_left(self):
        pass

    def turn_right(self):
        pass
    
    def forward(self):
        pass

    def stop(self):
        self.left_wheels.stop()
        self.right_wheels.stop()
    
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
            
    def sense(self):
        if self.lline_track.line_tracker_percent() > 70:
            lon_tape = True

        if self.rline_track.line_tracker_percent() > 70:
            ron_tape = True
    
    def loop(self):
        pass

bot = GridFollower()
while True:
    bot.loop()

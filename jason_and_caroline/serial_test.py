# Python
import sys
import vex

serial = vex.Serial(1, 9600)

# The arduino is programmed to ignore the first input
# because the first message outputs weird characters.
serial.write("begin")
sys.sleep(2)

while True:
    serial.write("Humans are")
    sys.sleep(1)
    serial.write("inferior")
    sys.sleep(1)

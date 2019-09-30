from microbit import *

while True:
    pin0.write_analog(1023)
    sleep(500)
    pin0.write_analog(0)
    sleep(500)

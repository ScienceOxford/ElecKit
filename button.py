from microbit import *

while True:
    button = pin0.read_digital()
    if button == 1:
        display.show(Image.DUCK)
    else:
        display.clear()

import time                  
import usb_hid
import analogio
import board
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import usb_hid

# initiera hid keyboard
kbd = Keyboard(usb_hid.devices)

# joystick = analog input på gpio 27
joystick = analogio.AnalogIn(board.GP27)

def read_joystick():
    # returnar mellan -1.0 och 1.0
    return (joystick.value - 32768) / 32768

# main loop
while True:
    # läser input från joystick
    position = read_joystick()
    
    # om positionen är "höger?"
    if position > 0.5:
        # registrerar men släpper inte
        kbd.press(Keycode.SPACE)
        time.sleep(0.05)
    
    # släpper space
    else:
        kbd.release(Keycode.SPACE)
        time.sleep(0.05)

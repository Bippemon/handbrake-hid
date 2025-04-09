# Simracing handbroms med pico
En handbroms byggd på raspberry pi pico för sim-racing
Kontrollen håller in Spacebar när man håller joystick över threshold åt "höger"

## Hårdvara
* Raspberry pi pico
* HW-504 joystick
* Micro usb sladd
* Jumper wires (M - F)
* Kardborreband
* Handtag för handbroms
* Bottenplatta för montering
* Skruv för montering


## Mjukvara
* CircuitPython
* Thonny
* Git


## Step by step
### - Kopplingar Joystick -> Pico
* GND -> Ground
* +5V -> 3V3
* VRX -> GPIO27
### - Ladda ner CircuitPython + CircuitPython library
* CircuitPython - https://circuitpython.org/board/raspberry_pi_pico/
* CircuitPython library - https://circuitpython.org/libraries
### - Starta pico i BOOTSEL mode
### - Drag & drop CircuitPython uf2 fil till Pico
### - Kopiera mappen "lib/adafruit_hid" -> Pico "/lib"
### - Kopiera code.py & boot.py till Pico
### - Starta om

### Att fixa
* Handtag
* Bottenplatta i trä (8-9cm) X 9cm
* Minst 8st skruv (3mm breda hål)



Kopiera "adafrui_bus_device" och "adafruit_hid" till /lib på pico

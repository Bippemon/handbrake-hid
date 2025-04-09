import storage
import usb_cdc
import usb_hid

# stänger av lagringsenheten på pico
storage.disable_usb_drive()

# stänger virtual COM-port (seriell kommunikation)
usb_cdc.disable()

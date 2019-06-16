import time
import sys

import RPi.GPIO as GPIO
from hx711 import HX711

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(-300)

hx.reset()
#hx.tare()

val = hx.get_weight(5)
hx.power_down()
hx.power_up()
time.sleep(0.1)
GPIO.cleanup()
print val

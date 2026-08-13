from machine import Pin
import time

led = Pin(16, Pin.OUT)
button = Pin(17, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        led.on()
    else:
       led.off()


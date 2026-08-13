from machine import Pin, PWM
import time

button = Pin(2, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(16, Pin.OUT))
led = Pin(17, Pin.OUT)

while True:
    if button.value() == 0:
        led.on()          
        buzzer.freq(1500)     
        buzzer.duty_u16(20000)
        time.sleep(0.5)       
        
    else:
        led.off()         
        buzzer.duty_u16(0)  
        time.sleep(0.1)
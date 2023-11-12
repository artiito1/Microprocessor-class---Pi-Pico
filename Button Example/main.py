from machine import Pin 
import time
button = Pin(12, Pin.IN,Pin.PULL_DOWN)
led = Pin(1, Pin.OUT)
while True :
    if button.value():
        led.toggle()
        time.sleep(0.5)
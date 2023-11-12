# Import necessary modules
from machine import Pin
import time

# Define a button on Pin 12 as an input with a pull-down resistor
button = Pin(12, Pin.IN, Pin.PULL_DOWN)

# Define an LED on Pin 1 as an output
led = Pin(1, Pin.OUT)

# Infinite loop for continuous operation
while True:
    # Check if the button is pressed (its value is True)
    if button.value():
        # Toggle the state of the LED (turn it on or off)
        led.toggle()

        # Pause for 0.5 seconds to debounce the button and control LED blinking speed
        time.sleep(0.5)

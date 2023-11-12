# Import necessary modules
from machine import Pin
from time import sleep

# Variable to track motion state
motion = False

# Function to handle interrupt when motion is detected
def handle_interrupt(pin):
    global motion
    motion = True
    global interrupt_pin
    interrupt_pin = pin

# Initialize LED on Pin 9 as an output
led = Pin(9, Pin.OUT)

# Initialize PIR motion sensor on Pin 21 as an input
pin = Pin(21, Pin.IN)

# Set up interrupt on rising edge for the PIR motion sensor
pin.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

# Infinite loop for continuous operation
while True:
    # Check if motion is detected
    if motion:
        # Print a message indicating motion and the pin that triggered the interrupt
        print('Motion detected! Interrupt caused by:', interrupt_pin)
        
        # Turn on the LED for 5 seconds
        led.value(1)
        sleep(5)
        
        # Turn off the LED
        led.value(0)
        
        # Print a message indicating that motion has stopped
        print('Motion stopped!')
        
        # Reset the motion flag
        motion = False

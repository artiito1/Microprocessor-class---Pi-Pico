# Import necessary modules
from time import sleep
from machine import Pin, ADC, PWM

# Initialize PWM for LED on Pin 7 with a frequency of 1000 Hz
led = PWM(Pin(7))
led.freq(1000)

# Initialize ADC (Analog-to-Digital Converter) for potentiometer on Pin 26
potentiometer = ADC(26)

# Infinite loop for continuous operation
while True:
    # Read the analog value from the potentiometer
    potentiometer_value = potentiometer.read_u16()
    
    # Print the current value of the potentiometer to the console
    print(potentiometer_value)
    
    # Set the duty cycle of the LED based on the potentiometer value
    led.duty_u16(potentiometer_value)
    
    # Pause for 0.25 seconds to control the loop speed
    sleep(0.25)

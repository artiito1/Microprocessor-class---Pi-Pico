from machine import Pin, Timer
from time import sleep

# Define the button pin as input with pull-down resistor
button = Pin(5, Pin.IN, Pin.PULL_DOWN)

# Define the red LED pin as output
kled = Pin(5, Pin.OUT)

# Define the blue LED pin as output
mled = Pin(6, Pin.OUT)

# Create timers for red and blue LED flashing
polis_timer_mavi = Timer()
polis_timer_kirmizi = Timer()

# Callback function for red LED flashing
def polisk(polis_timer_kirmizi):
    kled.toggle()

# Callback function for blue LED flashing
def polism(polis_timer_mavi):
    sleep(0.3)
    mled.toggle()

# Initialize timers with periodic callbacks
polis_timer_kirmizi.init(period=300, mode=Timer.PERIODIC, callback=polisk)
polis_timer_mavi.init(period=300, mode=Timer.PERIODIC, callback=polism)

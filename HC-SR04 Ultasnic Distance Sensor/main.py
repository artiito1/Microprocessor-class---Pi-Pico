import machine
import time

# Define the trigger pin as an output
trig = machine.Pin(27, machine.Pin.OUT)

# Define the echo pin as an input
echo = machine.Pin(21, machine.Pin.IN)

def read_distance():
    # Activate the ultrasonic sensor by turning on the trigger pin
    trig.on()
    time.sleep_us(10)  # Wait for 10 microseconds
    trig.off()  # Turn off the trigger pin

    # Measure the pulse time using time_pulse_us function
    pulse_time = machine.time_pulse_us(echo, 1, 30000)  # Wait up to 30 milliseconds for the echo pulse

    # Speed of sound is set to 34029 cm/s. Modify this value based on your environment.
    speed_of_sound = 34029  # Speed of sound in centimeters per second
    distance = (pulse_time / 2) * (speed_of_sound / 1000000)

    return distance

# Continuously read and print distance measurements
while True:
    distance = read_distance()
    print("Distance:", distance, "cm")
    time.sleep(1)  # Pause for 1 second before the next measurement
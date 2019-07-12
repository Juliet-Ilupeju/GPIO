import RPi.GPIO as GPIO
import time
import signal
import sys

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

# Turn off all lights when user ends demo
def allLightsOff(signal, frame):
    GPIO.output(25, False)
    GPIO.output(8, False)
    GPIO.output(7, False)
    GPIO.cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT, allLightsOff)

# Loop forever
while True: 
    # Red 
    GPIO.output(7, True) 
    time.sleep(3)  
    # Red and amber 
    GPIO.output(8, True) 
    time.sleep(1)  
    # Green 
    GPIO.output(25, False) 
    GPIO.output(8, False) 
    GPIO.output(7, True) 
    time.sleep(5)  
    # Amber 
    GPIO.output(7, False) 
    GPIO.output(8, True) 
    time.sleep(2)  
    # Amber off (red comes on at top of loop) 
    GPIO.output(8, False)
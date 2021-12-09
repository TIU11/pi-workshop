import time
#import RPi.GPIO as GPIO
from gpiozero import OutputDevice


# GPIO pin of Relay
#relay = OutputDevice(24, active_high=False, initial_value=False)
relay = OutputDevice(24)
relay.on()
time.sleep(5)
relay.off()

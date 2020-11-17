from sense_hat import SenseHat
from pyparrot.Minidrone import Mambo
import sys

sense = SenseHat()
# Change this to the address of the mambo
mamboAddr = ""
# Set True/False for the wifi depending on if you are using the wifi or the BLE to

mambo = Mambo(mamboAddr, use_wifi=False)
print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

try:
    if (success):
         # get the state information
     print("sleeping")
     def takeoff():
         mambo.smart_sleep(2)
         print("taking off!")
         mambo.safe_takeoff(5)

     def land():
         mambo.safe_land(5)
         mambo.smart_sleep(5)
         print("disconnect")
         mambo.disconnect()

    while True:
            for event in sense.stick.get_events():
                if event.action == 'pressed' and event.direction == 'up':
                    takeoff()
                if event.action == 'pressed' and event.direction == 'down':
                    land()

except:
    print("Error: Uh oh check your code!.\n")
    mambo.safe_land(1)
    mambo.disconnect()
    sys.exit()

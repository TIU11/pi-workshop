from pyparrot.Minidrone import Mambo
import sys
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
     mambo.smart_sleep(2)
     print("taking off!")
     mambo.safe_takeoff(5)
     print("turning")
     mambo.turn_degree(90)
     print("landing")
     mambo.safe_land(5)
     mambo.smart_sleep(5)
     print("disconnect")
     mambo.disconnect()
except:
    print("Error: Uh oh check your code!.\n")
    mambo.safe_land(1)
    mambo.disconnect()
    sys.exit()

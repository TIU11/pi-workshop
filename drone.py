from pyparrot.Minidrone import Mambo

# Change this to the address of the mambo
mamboAddr = "D0:3A:4B:91:E6:24"

mambo = Mambo(mamboAddr, use_wifi=False)
print("trying to connect")

success = mambo.connect(num_retries=3)

print("connected: %s" % success)

if (success):
    # get the state information
    print("sleeping")
    mambo.smart_sleep(2)
    print("taking off!")
    mambo.safe_takeoff(5)
    print("landing")
    mambo.safe_land(5)
    mambo.smart_sleep(5)
    print("disconnect")
    mambo.disconnect()

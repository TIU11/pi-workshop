import explorerhat
import time

# while True:
#         sensor = explorerhat.analog.one.read()
#         inches = sensor / 0.00819
#         print(inches)
#         time.sleep(0.1)
explorerhat.output.one.off()
time.sleep(1)

def get_distance():

    # Sends TRIG Out
    explorerhat.output.one.on()
    time.sleep(0.00001)
    explorerhat.output.one.off()

    # Gets ECHO Back
    while explorerhat.input.one.read()==0:
        pulse_start = time.time()

    while explorerhat.input.one.read()==1:
        pulse_end = time.time()
        
    print ("Pulse Start: {}".format(pulse_start))
    print ("Pulse End : {}".format(pulse_end))
    
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration / 0.000148

    distance = round(distance,4)

    print("Distance: {} inches".format(distance)) #in cm
    return distance

while True:
    distance = get_distance()
    time.sleep(0.1)

    if distance < 10:
        print("stop")
        explorerhat.motor.two.stop()
        explorerhat.motor.one.stop()
    elif distance < 20 and distance > 10:
        print("backwards")
        explorerhat.motor.two.forward(100)
        explorerhat.motor.one.backward(100)
    elif distance > 50:
        explorerhat.motor.one.forward(100)
        explorerhat.motor.two.backward(100)
    else:
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()

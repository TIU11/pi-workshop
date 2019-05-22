import requests
from time import sleep
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

now = time().strftime('%I:%M:%S %p')
temp = sensor.get_temperature()

event = "TempPi"
apikey = "your-key-here"
value1 = now
value2 = temp

url     = "https://maker.ifttt.com/trigger/%s/with/key/%s" % (event, apikey)
payload = {"value1" : value1,"value2" : value2}
headers = {}
res = requests.post(url, data=payload, headers=headers)

import csv
from time import time
from time import strftime
from time import sleep
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

def read_temp():
	now = strftime('%I:%M:%S %p') # 2:05:01 PM
	temp = sensor.get_temperature() * 1.8 + 32 # in Fahrenheit
	return [now, temp]

with open('data.csv', 'w') as f:
	writer = csv.writer(f)
	writer.write_row(['Time', 'Temperature'])

	while True:
		writer.write_row(read_temp())
		f.flush() # finish up the write
		print('row was written')
		sleep(1)

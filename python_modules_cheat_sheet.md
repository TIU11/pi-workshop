# Python Modules Cheat Sheet

Quick reference for third-party Python modules used in projects. For full project walk-throughs, including connecting things to your Raspberry Pi, visit http://stem.tiu11.org.

###### Install First

Since these Python modules aren't part of the Python Standard Library, they have to be installed. The linked docs will have instructions for Rasberry Pi, which runs on Raspbian. Look for `sudo apt-get update` and `sudo apt-get install`.

## Raspberry Pi GPIO Pins

> A simple interface to GPIO devices with Raspberry Pi.
>
> https://gpiozero.readthedocs.io

```python
from gpiozero import Button, LED, OutputDevice
from time import sleep

# LED
led = LED(17)

led.on()
sleep(1)
led.off()
sleep(1)

# Button

button = Button(3)

print('Press the button!')
button.wait_for_press()
print('Button was pressed!')

# Relay

relay = OutputDevice(24)

relay.on()
sleep(1)
relay.off()
```

## Automation HAT

> https://github.com/pimoroni/automation-hat
>
> [Getting Started Guide](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-automation-hat-and-phat) |
> [GPIO Pinout guide](https://pinout.xyz/pinout/automation_hat) |
> [Function Reference](https://github.com/pimoroni/automation-hat/blob/master/documentation/REFERENCE.md)

```python
import automationhat

value1 = automationhat.analog.one.read()
value2 = automationhat.analog.two.read()

# Check if an input/output/relay is on
if automationhat.input.one.is_on():
  print('One is on')

# Turn an output on or off
automationhat.output.one.on()  # Turn output 1 on
automationhat.output.one.off() # ...and off
```

## Temperature Probe

> Get the temperature from a w1 therm compatible sensor.
>
> https://github.com/timofurrer/w1thermsensor

```python
from w1thermsensor import W1ThermSensor
from time import sleep

sensor = W1ThermSensor()
temperature_in_celsius = sensor.get_temperature()
```

## Sense HAT

> https://pythonhosted.org/sense-hat/

```python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
red = (255, 0, 0)           # RGB levels are 0 to 255

sense.clear(red)            # Fill whole screen red
sleep(1)
sense.clear()               # Fill whole screen blank
sleep(1)
sense.set_pixel(4, 5, red) # Set specific pixel red
sleep(1)
sense.show_message("Pi Yum!!")

r = red             # Red
w = (255, 255, 255) # White
question_mark = [
  w, w, w, r, r, w, w, w,
  w, w, r, w, w, r, w, w,
  w, w, w, w, w, r, w, w,
  w, w, w, w, r, w, w, w,
  w, w, w, r, w, w, w, w,
  w, w, w, r, w, w, w, w,
  w, w, w, w, w, w, w, w,
  w, w, w, r, w, w, w, w
]

sense.set_pixels(question_mark)
```

## Pi Camera

> The picamera package for the Raspberry Pi camera module
>
> https://picamera.readthedocs.io/

Test in the Console.
```bash
# Show a preview. Press <Ctrl+C> to close the preview.
pi@raspberrypi:~ $ raspistill -k

# Take a picture and save it to a file.
pi@raspberrypi:~ $ raspistill -o image.jpg
```

### Photo
```python
from picamera import PiCamera
from gpiozero import Button
from time import sleep

camera = PiCamera()
button = Button(17)

while True:
  camera.start_preview(alpha=192)
  button.wait_for_press()
  sleep(3)
  camera.capture("/home/pi/button.jpg")
  camera.stop_preview()
```

### Video
```python
from picamera import PiCamera

camera = PiCamera()

camera.start_preview(alpha=192)
camera.framerate = 24
camera.start_recording('/home/pi/myvideo.h264')
camera.wait_recording(5)


camera.stop_recording()
camera.stop_preview()
```

## Internet Requests

Make HTTP requests on the internet.

> http://docs.python-requests.org/en/master/user/quickstart/

[HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) requests are how web browsers communicate on the internet. You make a request to a server, another computer on the internet, and it responds.
* Requests and responses are often called "messages".
* The main parts of a request are: a url, a method, headers, and sometimes a body.
  * Each type of request is called a "method" or "verb". We'll cover two common HTTP methods, `GET` and `POST`.
  * [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) are like settings. Most of the time, we're happy with the defaults, so just be aware of them.

### POST

An HTTP POST request asks a server to accept data you are sending it.. A web browser uses POST when you submit an online form.

```python
import requests

event     = "your IFTTT event name"
api_key   = "your-ifttt-key-here"
ifttt_url = "https://maker.ifttt.com/trigger/%s/with/key/%s" % (event, api_key)
payload   = { "value1" : value1, "value2" : value2, "value3" : value3 }
response  = requests.post(ifttt_url, data=payload)
```

### GET

An HTTP GET request asks a server to send it something. It is used to retrieve data.

Get a Joke
```python
import requests

# Get a joke in JSON format.
response = requests.get('https://official-joke-api.appspot.com/random_joke')
if response.ok:
  joke_data = response.json()
else:
  print("Oops! The joke is on me!")

# Tell the joke
print(joke_data['setup'])
sleep(1) # wait for it!
print(joke_data['punchline'])
```

Advanced: Download an image and save it to a file. Uses the [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#Image_types) from the response headers, telling us the type of content in the response, to add the right extension to the filename.

```python
import requests
import mimetypes

# Get the location of a random cat picture. Hopefully this is safe.
response = requests.get('https://aws.random.cat/meow')
data = response.json()
file_url = data['file']

# Get the picture.
response = requests.get(file_url)
if response.ok:
  # Name the file so the extension matches the type of image.
  content_type = response.headers['Content-Type']
  extension = mimetypes.guess_extension(content_type) # .png, .gif, ...
  filename = 'random_cat' + extension

  # Save the file, overwriting any existing file with the same name.
  with open(filename, 'wb') as f:
    f.write(response.content)
else:
  print('error when getting ' + file_url)
```

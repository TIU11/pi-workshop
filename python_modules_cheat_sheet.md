# Python Modules Cheat Sheet

Quick reference for third-party Python modules used in projects. For full project walk-throughs, including connecting things to your Raspberry Pi, visit https://stem.tiu11.org.

Contents
* [Raspberry Pi GPIO Pins](#raspberry-pi-gpio-pins)
* [guizero](#guizero)
* [Automation HAT](#automation-hat)
* [Temperature Probe](#temperature-probe)
* [Sense HAT](#sense-hat)
* [Pi Camera](#pi-camera)
* [Minecraft Pi](#minecraft-pi)
* [(Internet) Requests](#internet-requests)

**Need to Install First**

Since these Python modules aren't part of the Python Standard Library, they have to be installed. The linked docs will have instructions for Raspberry Pi OS. Look for `sudo apt-get update` and `sudo apt-get install` or sometimes `sudo pip3 install`.

## Raspberry Pi GPIO Pins

> A simple interface to GPIO devices with Raspberry Pi.
>
> https://gpiozero.readthedocs.io

(gpiozero is installed by default)

The [recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html) are a great place to start:
[LED](https://gpiozero.readthedocs.io/en/stable/recipes.html?highlight=motor#led),
[Button](https://gpiozero.readthedocs.io/en/stable/recipes.html?highlight=motor#button),
[Reaction Game](https://gpiozero.readthedocs.io/en/stable/recipes.html?highlight=motor#reaction-game),
[Motion sensor](https://gpiozero.readthedocs.io/en/stable/recipes.html?highlight=motor#motion-sensor),
[Motors](https://gpiozero.readthedocs.io/en/stable/recipes.html?highlight=motor#motors), etc. The [pin numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) diagram is helpful if you don't have one in your kit.

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

## guizero

> guizero is a Python 3 library for creating simple GUIs.
>
> It is designed to allow new learners to quickly and easily create GUIs for their programs.
>
> https://lawsie.github.io/guizero/

After [installing](https://lawsie.github.io/guizero/#raspberry-pi), check out their [Recipes](https://lawsie.github.io/guizero/recipes/) for examples to try out. Try this example to make a [PushButton](https://lawsie.github.io/guizero/pushbutton/) run [commands](https://lawsie.github.io/guizero/commands/) that turn an LED on and off.

```python
from guizero import App, Text, PushButton
from gpiozero import LED

red = LED(12)
app = App(title="GUI with LED Controls")

label = Text(app, text="Red")
on_button = PushButton(app, command=red.on, text="on")
off_button = PushButton(app, command=red.off, text="off")

app.display()
```

Get fancy with [sizes](https://lawsie.github.io/guizero/size/), [colors](https://lawsie.github.io/guizero/colors/) and [images](https://lawsie.github.io/guizero/images/).

As your GUI grows, it might get cluttered. Look into [Layouts](https://lawsie.github.io/guizero/layout/) for ways to organize things, like a [grid](https://lawsie.github.io/guizero/layout/#grid-layout) and (Boxes)[https://lawsie.github.io/guizero/layout/#boxes].

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

Setup
* `sudo pip3 install w1thermsensor` (see [installation](https://github.com/timofurrer/w1thermsensor#installation))
* Go to Raspberry Pi menu > Preferences > Raspberry Pi Configuration > Interface.
  - Enable 1-wire
  - Reboot

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

## Minecraft Pi

The [mcpi](https://github.com/martinohanlon/mcpi) module allows you to communicate with [Minecraft: Pi edition](https://www.minecraft.net/en-us/edition/pi).
* [Getting Started with Minecraft Pi](https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi) Raspberry Pi Project
* [mcpi API reference](https://www.stuffaboutcode.com/p/minecraft-api-reference.html)

Install with `sudo pip3 install mcpi`

```python
from mcpi import minecraft

mc = minecraft.Minecraft.create()

mc.postToChat("Hello world")
```

## Internet Requests

Make HTTP requests on the internet.

> https://docs.python-requests.org/en/master/user/quickstart/

[HTTP messages](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages) are how web browsers communicate on the internet. You make a **request** to a server (or a computer) and it sends a **response** back.
* The main parts of a **request** are:
  * `url` - the address a request will go to.
  * `method` - the "verb" or type of request. We'll cover `GET` and `POST` requests.
  * `body` - (optional) data like a form or a file
  * [headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) - (optional) like settings. Most of the time, we're happy with the defaults, so just be aware of them.
* The main parts of a **response**:
  * actually, it looks a lot like a request, so...all those parts :smile:
  * [status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) - a code in the response to your request to let you know if it was successfully completed.
    - `200 OK` - the request succeeded
    - `404 Not Found` - the server can't find that. Do you have a typo in the `url`?

### POST

An HTTP POST request asks a server to accept data you are sending it. A web browser uses POST when you submit an online form.

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

**Advanced GET Example:** Download an image and save it to a file. Uses the [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#Image_types) from the response headers, telling us the type of content in the response, to add the right extension to the filename.

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

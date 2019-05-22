#!/usr/bin/env python3

#
from pi_image import create_post
import ifttt
from guizero import App, Text

event   = 'create_post'
api_key = 'your-api-key'
message = 'Tweeting with Python and Ruby'
image   = 'stem.jpg'

app = App(title="Hello world")
app.display()
welcome_message = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="lightblue")
my_name = TextBox(app)

def say_my_name():
    welcome_message.value = my_name.value

update_text = PushButton(app, command=say_my_name, text="Display my name")
my_image = Picture(app, image)



# Create a post so we can give a public image url to IFTTT.
post = create_post(message, image)

if post:
    ifttt.send(event, api_key, value1=post['content'], value2=post['image_url'])

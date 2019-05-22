#!/usr/bin/env python3

#
from pi_image import create_post
import ifttt

event   = 'create_post'
api_key = 'your-api-key'
message = 'Tweeting with Python and Ruby'
image   = 'stem.jpg'

# Create a post so we can give a public image url to IFTTT.
post = create_post(message, image)

if post:
    ifttt.send(event, api_key, value1=post['content'], value2=post['image_url'])

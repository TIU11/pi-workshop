#!/usr/bin/env python3

# Interface to IFTTT

import requests
import pi_image

def send(event, api_key, value1=None, value2=None, value3=None):
    ifttt_url = "https://maker.ifttt.com/trigger/%s/with/key/%s" % (event, api_key)
    payload   = { "value1" : value1, "value2" : value2, "value3" : value3 }
    response  = requests.post(ifttt_url, data=payload)
    if response.ok:
        print("Called IFTTT '%s' event." % (event))
    else:
        print("Oops! Couldn't send message to IFTTT.")
        print(response.text)

def post_and_send(message, image, ifttt_event, ifttt_api_key):
    # Create a post so we can give a public image url to IFTTT.
    post = pi_image.create_post(message, image)

    if post:
        ifttt.send(ifttt_event, ifttt_api_key, post['content'], post['image_url'])

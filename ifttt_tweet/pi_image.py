#!/usr/bin/env python3

# Interface to https://pi-image.tiu11.org/

import requests

HOST = 'https://pi-image.tiu11.org/'

# Create a User
def create_user(username):
    url = HOST + 'users.json'
    data = { 'username': username }
    response = requests.post(url, json=data)
    if response.ok:
        user_data = response.json()
        print('Created user', user_data)
    else:
        print("Oops! Couldn't create the user '%s'" % username)
        print(response.text)

# Get a User by id
def get_user(user_id):
    url = HOST + 'users/%s.json' % (user_id)
    response = requests.get(url)
    if response.ok:
        print('Got user', response.json())
    else:
        print("Oops! Couldn't get the user.", response.text)

# Upload a User avatar image.
def upload_user_avatar(user_id, filename):
    url = HOST + 'users/%s.json' % user_id
    # headers = {'Content-type': 'multipart/form-data'}
    # data = { 'username': 'ahoyt', 'images': [] }
    # files = [ # this doesn't jive with the server
    #     # ('images', ('stem.jpg', open('stem.jpg', 'rb'), 'image/jpg'))
    #     ('images', open('stem.jpg', 'rb')),
    #     ('images', open('stem.jpg', 'rb'))
    # ]
    file = {'avatar': open(filename, 'rb')}
    response = requests.put(url, files=file)
    if response.ok:
        user_data = response.json()
        print('Updated user', user_data)
    else:
        print("Oops! Couldn't update user %s" % user_id)
        print(response.text)

# Create a Post
def create_post(content, image_filename):
    url = HOST + 'posts.json'
    data = { 'content': content }
    file = {'image': open(image_filename, 'rb')}
    response = requests.post(url, files=file, data=data)
    if response.ok:
        post = response.json()
        print('Created post', post)
        return post
    else:
        print("Oops! Couldn't create the post.")
        print(response.text)

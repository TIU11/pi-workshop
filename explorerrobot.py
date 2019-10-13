import explorerhat
from time import sleep
from guizero import App, PushButton

def forwards():
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.backward(100)
    sleep(1)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    
def backwards():
    explorerhat.motor.two.forward(100)
    explorerhat.motor.one.backward(100)
    sleep(1)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
 
def turn():
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.backward(100)

app = App("Robot controller")

drive = PushButton(app, forwards, text="Forwards")
reverse = PushButton(app, backwards, text="Backwards")
turns = PushButton(app, turn(), text="Turn")

app.display

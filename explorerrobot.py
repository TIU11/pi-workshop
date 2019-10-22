import explorerhat
from time import sleep
from guizero import App, PushButton, Text

def backwards():
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.backward(100)
    sleep(1)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    
def forwards():
    explorerhat.motor.two.forward(100)
    explorerhat.motor.one.backward(100)
    sleep(1)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    
def turns_right():
    explorerhat.motor.two.backward(100)
    sleep(1)
    explorerhat.motor.two.stop()


def turns_left():
    explorerhat.motor.one.forward(100)
    sleep(1)
    explorerhat.motor.one.stop()

    
def stops():
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

app = App("Robot controller")


drive = PushButton(app, forwards, text="Forwards")
reverse = PushButton(app, backwards, text="Backwards")
right = PushButton(app, turns_right, text="Right Turn")
left = PushButton(app, turns_left, text="Left Turn")
stop = PushButton(app, stops, text="Stop")


app.display

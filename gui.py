# GUI Light

from guizero import App, Text, PushButton
from gpiozero import LED

red = LED(12)
app = App()

label = Text(app, “Red”)
onButton = PushButton(app, command=red.on, text="on")
offButton = PushButton(app, command=red.off, text="off")

app.display()


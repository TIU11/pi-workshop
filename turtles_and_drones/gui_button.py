# GUI Commands

from guizero import App, Text, PushButton

def say_hello():
	text.value = "hello world"

app = App()
text = Text(app)
button = PushButton(app, command=say_hello)
app.display()

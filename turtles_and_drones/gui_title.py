# GUI Widgets

from guizero import App, Text

app = App(title="Hello world")
message = Text(app, text="Welcome to the Hello world app!")
app.display()

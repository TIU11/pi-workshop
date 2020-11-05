from guizero import App, PushButton, Slider
from pyparrot.Minidrone import Mambo

mamboAddr = "" # Mac Address of Bluetooth device
mambo=Mambo(mamboAddr, use_wifi=False)
success= mambo.connect(num_retries=3)
print("connected: %s" % success)

def flyme():
    if(success):
        mambo.safe_takeoff(5)
def landme():
    mambo.safe_land(5)

app = App(title="Fly")
takeoff = PushButton(app, command=flyme,text="Take off")
landbutton = PushButton(app, command=landme,text="Land")

app.display()

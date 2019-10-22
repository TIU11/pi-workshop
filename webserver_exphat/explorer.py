from flask import *
from time import time, strftime, sleep
from gpiozero import LED
import explorerhat

red = LED(17)

app = Flask(__name__)

@app.route('/')
def index():
    now = time()
    now = strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'HELLO!',
      'time': now
      }
    return render_template('index.html', **templateData)

# Change LED value POST request.
@app.route("/change_led_status/<int:status>", methods=['POST'])


def change_led_status(status):
  # Check the value of the parameter
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
        
    if status == 0:
        stops()
    elif status == 1:
        forwards()
    elif status == 2:
        backwards()
    elif status == 3:
        turns_right()
    elif status == 4:
        turns_left()
    else:
        return ('Error', 500)
    return ('', 200)


    
    
# Starts the app listening to port 5000 with debug mode
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

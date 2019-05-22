from flask import Flask
import datetime
from gpiozero import LED

red = LED(17)

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.date.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
    return render_template('index.html', **templateData)

# Change LED value POST request.
@app.route("/change_led_status/<int:status>", methods=['POST'])
def change_led_status(status):
  # Check the value of the parameter
  if status == 0:
    red.off()
  elif status == 1:
    red.on()
  else:
    return ('Error', 500)
  return ('', 200)

# Starts the app listening to port 5000 with debug mode
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

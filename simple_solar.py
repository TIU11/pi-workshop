from gpiozero import Button
import time

# GPIO pin for button monitoring
BUTTON_PIN = 27

# Initialize button with pull-up resistor
button = Button(BUTTON_PIN, pull_up=True)

print("Button Test - Press Ctrl+C to exit")
print("--------------------------------")

try:
    while True:
        current_state = button.is_pressed
        print(f"Button state: {'PRESSED' if current_state else 'RELEASED'}")
        time.sleep(0.3)
        
except KeyboardInterrupt:
    print("\nExiting program")
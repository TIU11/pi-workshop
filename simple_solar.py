from gpiozero import Button
import time

# GPIO pin definition - only need to monitor the button
BUTTON_PIN = 27  # GPIO pin connected to the button

# Initialize button component
button = Button(BUTTON_PIN, pull_up=True)  # Button with pull-up resistor

print("Solar Panel LED Monitor")
print("Press Ctrl+C to exit")
print("-----------------------")
print("IMPORTANT: The LED is powered directly by the solar panel")
print("The Pi is only monitoring the button state")
print("-----------------------")

try:
    while True:
        if button.is_pressed:
            # When button is pressed, solar panel is connected to LED
            print("Button pressed - Solar panel powering LED")
        else:
            # When button is released, solar panel is disconnected
            print("Button released - LED off")
        
        # Add a delay to prevent excessive printing
        time.sleep(0.5)
        
except KeyboardInterrupt:
    # Clean up on exit
    print("\nExiting program")
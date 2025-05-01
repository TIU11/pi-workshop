from gpiozero import Button, LED
import time

# GPIO pin definitions
LED_PIN = 17     # GPIO pin controlling the LED
BUTTON_PIN = 27  # GPIO pin connected to the button

# Initialize components
button = Button(BUTTON_PIN, pull_up=True)  # Button with pull-up resistor
led = LED(LED_PIN)                         # LED

print("Solar Panel LED Control")
print("Press Ctrl+C to exit")
print("-----------------------")

try:
    while True:
        if button.is_pressed:
            # When button is pressed, solar panel is connected to LED
            # We also turn on the LED via GPIO (optional)
            led.on()
            print("Button pressed - Solar panel powering LED")
        else:
            # When button is released, solar panel is disconnected
            led.off()
            print("Button released - LED off")
        
        # Add a delay to prevent excessive printing
        time.sleep(0.5)
        
except KeyboardInterrupt:
    # Clean up on exit
    led.off()
    print("\nExiting program")
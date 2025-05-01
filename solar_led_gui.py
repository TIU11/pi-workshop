from gpiozero import Button, LED
from guizero import App, Text, PushButton, Box, Drawing
import threading
import time

# GPIO pin definitions
LED_PIN = 17    # GPIO pin controlling the LED
BUTTON_PIN = 27 # GPIO pin connected to the button

# Initialize components
button = Button(BUTTON_PIN, pull_up=True)  # Button with pull-up resistor
led = LED(LED_PIN)  # LED

# Variables for monitoring
button_state = False
button_presses = 0
last_press_time = time.time()
connection_duration = 0
total_connection_time = 0

# Create a list to store connection times for the graph
connection_history = []
MAX_HISTORY = 50

# Function to monitor button presses and solar panel connection
def monitor_solar_connection():
    global button_state, button_presses, last_press_time, connection_duration, total_connection_time
    
    while True:
        # Check if button state has changed
        current_state = button.is_pressed
        
        if current_state != button_state:
            button_state = current_state
            current_time = time.time()
            
            if button_state:  # Button just pressed
                # Update press count and time
                button_presses += 1
                last_press_time = current_time
                # LED turns on when button is pressed (though in reality, 
                # the solar panel is directly powering the LED)
                led.on()
            else:  # Button just released
                # Calculate connection duration
                connection_duration = current_time - last_press_time
                total_connection_time += connection_duration
                
                # Add to history for graph
                connection_history.append(connection_duration)
                if len(connection_history) > MAX_HISTORY:
                    connection_history.pop(0)
                
                # LED turns off when button is released
                led.off()
        
        # Short delay to prevent CPU overuse
        time.sleep(0.1)

# Start the monitoring thread
monitor_thread = threading.Thread(target=monitor_solar_connection, daemon=True)
monitor_thread.start()

# Create GUI
app = App(title="Solar Panel Monitor", width=600, height=400)

# Add header
header_box = Box(app, width="fill", align="top")
title = Text(header_box, text="Solar Panel Monitor", size=20, font="Arial Bold")
instruction = Text(header_box, text="Press the physical button to connect the solar panel to the LED")

# Create display area
display_box = Box(app, width="fill", height=80, align="top")
display_box.bg = "#f0f0f0"

# Display information about solar usage
status_text = Text(display_box, text="Status: Disconnected", size=16, align="left")
presses_text = Text(display_box, text="Button Presses: 0", size=14, align="left")
current_text = Text(display_box, text="Current Connection: 0.0 seconds", size=14, align="left")
total_text = Text(display_box, text="Total Connection Time: 0.0 seconds", size=14, align="left")

# Add graph for visualization
graph_box = Box(app, width="fill", height=200)
graph = Drawing(graph_box, width=550, height=200)

# Controls area
controls_box = Box(app, width="fill", align="bottom")

# Add a manual button in the GUI for testing without the physical button
sim_button = PushButton(controls_box, text="Simulate Button Press", width=20)
sim_button.bg = "lightblue"

# Reset stats button
reset_button = PushButton(controls_box, text="Reset Statistics", width=20)
reset_button.bg = "lightcoral"

# Function for the simulation button
def toggle_simulation():
    if sim_button.bg == "lightblue":
        # Simulate button press
        button._fire_events(True)
        sim_button.bg = "orange"
        sim_button.text = "Release Simulated Button"
    else:
        # Simulate button release
        button._fire_events(False)
        sim_button.bg = "lightblue"
        sim_button.text = "Simulate Button Press"

sim_button.update_command(toggle_simulation)

# Function to reset statistics
def reset_statistics():
    global button_presses, connection_duration, total_connection_time, connection_history
    button_presses = 0
    connection_duration = 0
    total_connection_time = 0
    connection_history = []

reset_button.update_command(reset_statistics)

# Function to update the display
def update_display():
    # Update status
    if button_state:
        status_text.value = "Status: Connected - Solar panel powering LED"
        status_text.text_color = "green"
        current_text.value = f"Current Connection: {time.time() - last_press_time:.1f} seconds"
    else:
        status_text.value = "Status: Disconnected - Press button to connect"
        status_text.text_color = "red"
        current_text.value = f"Current Connection: 0.0 seconds"
    
    # Update statistics
    presses_text.value = f"Button Presses: {button_presses}"
    total_text.value = f"Total Connection Time: {total_connection_time:.1f} seconds"
    
    # Draw graph
    graph.clear()
    
    # Draw background
    graph.rectangle(0, 0, 550, 200, color="#f8f8f8")
    
    # Draw axes
    graph.line(50, 180, 530, 180, color="black")  # X-axis
    graph.line(50, 20, 50, 180, color="black")    # Y-axis
    
    # Draw labels
    graph.text(290, 195, text="Connection History", color="black")
    graph.text(20, 100, text="Duration (s)", color="black", rotate=90)
    
    # Draw grid lines and labels
    if connection_history:
        max_duration = max(max(connection_history), 5)  # At least 5 seconds scale
        
        for i in range(5):
            y = 180 - (i * 40)
            duration_val = round((i / 4) * max_duration, 1)
            graph.line(50, y, 530, y, color="lightgray")
            graph.text(35, y, text=str(duration_val), color="black", size=10)
    else:
        # Default grid if no history
        for i in range(5):
            y = 180 - (i * 40)
            duration_val = i * 5
            graph.line(50, y, 530, y, color="lightgray")
            graph.text(35, y, text=str(duration_val), color="black", size=10)
    
    # Plot connection durations
    if connection_history:
        bar_width = min(15, (480) / len(connection_history))
        spacing = 2
        x = 50
        
        for duration in connection_history:
            height = (duration / max_duration) * 160
            y = 180 - height
            
            graph.rectangle(x, y, x + bar_width, 180, color="green")
            x += bar_width + spacing

# Update display regularly
app.repeat(100, update_display)

# Start the app
app.display()
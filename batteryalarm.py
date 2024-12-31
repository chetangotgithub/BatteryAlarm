import psutil
import time
import winsound
import ctypes

def set_battery_alarm(threshold):
    """
    Set an alarm when the battery percentage reaches the threshold and the battery is not charging.
    threshold: int, battery percentage to trigger the alarm
    """
    while True:
        # Get the battery status
        battery = psutil.sensors_battery()
        percent = battery.percent
        power_plugged = battery.power_plugged

        # Print the current battery percentage and charging status
        print(f"Current battery level: {percent}%")
        print(f"Power plugged in: {'Yes' if power_plugged else 'No'}")

        # Check if the battery percentage is below or equal to the threshold and not charging
        if percent <= threshold and not power_plugged:
            print("Battery level is low! Please plug in your charger.")
            # Play a beep sound
            winsound.Beep(1000, 1000)  # frequency, duration in milliseconds
            # Show a pop-up message
            ctypes.windll.user32.MessageBoxW(0, "Battery level is low! Please plug in your charger.", "Battery Alarm", 1)
            time.sleep(2)
        elif percent >= 70 and power_plugged:
            print("Battery level is above 30% it is overcharging")
            winsound.Beep(1000,1000)
            ctypes.windll.user32.MessageBoxW(0, "Battery level is above 70%! Please unplug your charger.", "Battery Alarm", 1)
            time.sleep(2)
        else:
            # Wait for 60 seconds before checking again
            time.sleep(30)

# Example usage
# Set the alarm for when battery percentage reaches 32% and not charging
set_battery_alarm(32)



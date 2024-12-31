import time
import winsound

def set_alarm(alarm_time):
    """
    Set an alarm for the specified time.
    alarm_time: str in HH:MM format
    """
    while True:
        # Get the current time
        current_time = time.strftime("%H:%M")
        
        # Check if the current time matches the alarm time
        if current_time == alarm_time:
            print("Wake up! Time to check your battery!")
            # Play a beep sound
            winsound.Beep(1000, 1000)  # frequency, duration in milliseconds
            break
        
        # Wait for 30 seconds before checking again
        time.sleep(30)

# Example usage
# Set the alarm for 07:30 AM (24-hour format)
set_alarm("12:54")


import pandas as pd
import pywhatkit as kit
import time
from datetime import datetime

# Load Excel file
excel_file = 'contacts.xlsx'  # Change this to your file path
df = pd.read_excel(excel_file)

# Assuming the contact numbers are in a column named 'Contact'
contact_column = 'Contact'  # Change this to your actual column name

# Current time tracking for dynamic scheduling
now = datetime.now()
hour = now.hour
minute = now.minute + 1  # Start sending messages after a 1-minute buffer

# Iterate through each contact number
for index, row in df.iterrows():
    contact_number = str(row[contact_column])
    message = "Hello, this is a test message from Darshan Sheta."  # Customize as needed

    try:
        # Send message to the contact number
        kit.sendwhatmsg("+91" + contact_number, message, hour, minute)
        print(f"Message sent to {contact_number}")

        # Update the minute variable for the next message
        minute += 1  # Increment to avoid conflicts in sending times
        
        # Sleep to allow message scheduling
        time.sleep(1)
        
        # Adjust hour and minute for overflow
        if minute >= 60:
            minute = 0
            hour = (hour + 1) % 24

    except Exception as e:
        print(f"Failed to send message to {contact_number}: {e}")

print("All messages attempted.")

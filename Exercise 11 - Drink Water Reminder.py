# run using
# /usr/bin/python3 "/home/anshul/Documents/CodeWithHarry/Exercise 11 - Drink Water Reminder.py"

import platform
import notify2
import time

print(platform.system())

REPEAT_INTERVAL = 3600  # every hour

while True:
    notify2.init("Drink Water Reminder")
    n = notify2.Notification(
        "Drink Water",
        "Anshul, you should drink water now",
        "dialog-information",  # optional icon
    )
    n.show()
    time.sleep(REPEAT_INTERVAL)

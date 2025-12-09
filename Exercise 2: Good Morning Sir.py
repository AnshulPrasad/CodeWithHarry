import time

hour = int(time.ctime().split()[3].split(":")[0])
# or
# hour = int(time.strftime('%H'))
if hour < 12:
    print("Good morning!")
elif 12 <= hour < 17:
    print("Good afternoon!")
elif 17 <= hour < 21:
    print("Good evening!")
else:
    print("Good night!")

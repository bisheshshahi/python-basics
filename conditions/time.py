import time

name = "Bishesh"

current_time = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

if hour >= 4 and hour < 12:
    greeting = "Good morning"
elif hour >= 12 and hour < 16:
    greeting = "Good afternoon"
elif hour >= 16 and hour < 20:
    greeting = "Good evening"
else:
    greeting = "Good night"

print(greeting, "Mr.", name + ".")
print("Current time is:", current_time)

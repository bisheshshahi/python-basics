import time
name = "Bishesh"
exactTime = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
if hour>=12 and hour<16:
  print("Good afternoon, Mr.",name,end='.')

elif hour>=20 and hour<24:
  print("Good night, Mr.",name,end='.')

elif hour>=4 and hour<12:
  print("Good morning, Mr.",name,end='.')

elif hour>=16 and hour<20:
  print("Good evening, Mr.",name,end='.')

else:
  print("Good night, Mr.",name,end='.')

print("Current time is:",exactTime)
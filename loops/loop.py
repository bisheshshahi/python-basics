#printing number from 1 to 10
for i in range(1,11):
 print (i)
print()

#print a rectangle from stars
for i in range(1,5):
 print('*'*4)
print()

#print a right angled triangle from stars
for i in range(1,5):
 print('*' * i)
print()

#print a hollow rectangle
for i in range(1,6):
  if i==1:
    print('*'*4)

  elif i==5:
    print('*'*4)
  
  else:
    print('*  *')

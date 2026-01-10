#Determine your grade
marks = int(input("Enter your marks:"))

#Check if marks are outside the valid range
if marks<0 or marks>100:
  print("Invalid marks! Please enter a value between 0 and 100.")

else:#Determine the grade based on marks
  if marks>=90:
    grade="A"

  elif marks>=80:
    grade="B"
 
  elif marks>=70:
    grade="C"
 
  elif marks>=60:
    grade="D"
  
  else:
    grade="F"
  
#Display result
  print("You scored",marks,"marks.","Your grade is",grade,end=".")

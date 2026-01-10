#Determine your grade
marks = int(input("Enter your marks:"))

if marks<=100 and marks>=90:
  grade="A"
  print("You scored",marks,"marks.","Your grade is",grade,end=".")

elif marks<=89 and marks>=80:
  grade="B"
  print("You scored",marks,"marks.","Your grade is",grade,end=".")

elif marks<=79 and marks>=70:
  grade="C"
  print("You scored",marks,"marks.","Your grade is",grade,end=".")

elif marks<=69 and marks>=60:
  grade="D"
  print("You scored",marks,"marks.","Your grade is",grade,end=".")

elif marks<=59 and marks>=0:
  grade="F"
  print("You scored",marks,"marks.","Your grade is",grade,end=".")

else:
  print("Invalid marks! Please enter a value between 0 and 100.")
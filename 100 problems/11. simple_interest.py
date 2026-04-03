#Write a program to find the simple interest when the value of principle,rate of interest and time period is not given.
#SI = (P*T*R)/100

print("Calculate Simple interest")
principle = float(input("Enter principle: "))
time = float(input("Enter time: "))
rate = float(input("Enter rate: "))

simple_interest = principle * time *rate
print("Simple Interest: ", simple_interest)
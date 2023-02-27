# write code to validata user input is within a range
# 

age = int(input("enter a number between 15 & 85 "))

'''
validates but I have to run several times to get correct input
'''
if age >=  15 and age <= 85:
  print("I can look up your soc ins number !")
  # call sin_lookup()
else:
  print(f"age not valid {age}")

# using while & or
print ("using while & or")
age = int(input("enter a number between 15 & 85 "))

'''
validates, only get past the loop if my number is
within the range 15-85 
stays inside the loop until within the range
'''
while ( age < 15 or age > 85 ):
  age = int(input("(while with or)enter a number between 15 & 85 "))

print(f"age valid {age}")
# using while & or
print ("using while & and")
'''
validates, only get past the loop if my number is
NOT within the range 15-85 
stays inside the loop until OUTSIDE the range
'''

# challenge, can you change this to use and to ensure the number is within 15-85

while (age >=  15 and age <= 85):
   age = int(input("(while with and)enter a number between 15 & 85 "))

print(f"age valid {age}")

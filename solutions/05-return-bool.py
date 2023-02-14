# returning a boolean True or False
# this is NOT A STRING 

def first_smaller(num1, num2):
  return num1 < num2 

def first_smaller2(num1, num2):
  small = num1 < num2
  return small

print("Testing")
print(smaller(1,2))
print(smaller(5,2))
print(smaller2(1,2))
print(smaller2(5,2))

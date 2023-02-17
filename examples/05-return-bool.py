# returning a boolean True or False
# this is NOT A STRING 

def first_smaller(num1, num2):
  return num1 < num2 

def first_smaller2(num1, num2):
  small = num1 < num2
  return small

def first_smaller3(num1, num2):
  if num1 < num2:
    small = True
  else:
    small = False
  return small

print("Testing")
print(first_smaller(1,2))
print(first_smaller(5,2))
print(first_smaller2(1,2))
print(first_smaller2(5,2))
print(first_smaller3(1,2))
print(first_smaller3(5,2))

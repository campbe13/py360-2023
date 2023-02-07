# write a function that compares 2 numbers and returns the smallest
# have the user input 3 numbers, use the function to display the smallest of the 3
# pmcampbell
# 2023-02-06

#test 1,2,3   ans 1
#test 321,222,678   ans 222
def smallest(number1, number2):
  if number1 < number2:
    small = number1
  else: 
    small = number2
  return small

first = int(input("first number of 3 svp: "))
second = int(input("second number of 3 svp: "))
third = int(input("third number of 3 svp: "))

small = smallest(first, second)
small = smallest(third, small)

print (f"smallest number {small} ")
# a function that returns something (that we know)
# num = input("give me a number")
# num = smallest( 100, 1000) # 100 
# print("smallest", num)

# num = smallest( 999, 1) # 1 
# print("smallest", num)

''' exception handling '''

'''asking for a positive number '''

''' if we get an error the code "crashes" or stops'''
print("no exception handling")
num = int(input("number svp: "))

''' if we get an error we handle it and do not "crash" or stop'''
print("with exception handling")
try:
  num = int(input("number svp (type a letter): "))
except ValueError:
  print('That was not a number, try again')
  num = -1
else:
  print("number input",num)
  
'''exception handling enter positive numbers '''
def inventory():
  count = -1 # set border condition to get into the loop
  while count < 0:
    try:
      count = int(input('Enter number of apples '))
    except ValueError:
      print("not a number, try again")
    else: 
      if count < 0:
        print("try again cant have - apples")

  # you only reach this statment when a number >= 0  is entered
  return count
 
# get inventory count for 4 items 
my_inventory = []
for i in range(4):
  my_inventory.append(inventory())
print(my_inventory)  
''' using exception handling for mars temperature '''
degrees = -130  # set to get into the while loop 
while degrees < -129  or degrees >= 21:
  try:
    degrees = int(input('Enter temperature '))
  except ValueError:
    print('not a number')
  else:
    pass
  
print("valid temp for mars", degrees)
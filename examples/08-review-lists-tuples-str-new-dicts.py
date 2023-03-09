# tuple vs list

# tuples immutable
print("tuple")
nums  = (1, 2, 3, 4)
print(nums[1])
#nums[1] = 7   # error!!
print(nums)

for i in range (len(nums)):
   print(nums[i])

for num in nums:
  print(num)
  
if 3 in nums:
  print("3 is in there")

for letter in "the quick brown fox":
  print( letter,end='-')
print()

# every 2nd letter
phrase = "the quick brown fox"
for i in range(1,len(phrase),2):
   if phrase[i] != ' ':
      print(phrase[i])
# every 2nd letter, don't count  space
print("while, every 2nd")
i = 1
count = 0 
while i < len(phrase):
  if phrase[i] != ' ':
    print(phrase[i], i)
    i += 2
  else:
    i += 1
  

if "a" in phrase:
  print("we have an a")
else:
  print("no a :(")
print("list")
num1 = 5
num2 = num1 
print("1",num1, "2", num2)
num1 += 2
num2 += 3
print("1",num1, "2", num2)

# lists are mutable
nums  = [1, 2, 3, 4]
print(nums[1])
nums[1] = 7  
print(nums)
numstoo = nums 
numstoo[0] = 9
nums[3] = 9
print("og", nums)
print("too", nums)
new = nums + [5,6,7]
new += [1,1,1]
print ("new", new)
if 3 in nums:
  print("3 is in there")
empty = {}  # dict
empty_list = []
empty_tuple = ()
month1 = { 'jan' : 1, 'feb' : 2, 'mar' : 3 }
month2 = { 1: 'jan', 2: 'feb', 3: 'mar' }
month2[5] = 'may'
print(month2[3], "shows march-matches on key")  
print(month2)
if 5 in month2:
    print("we have may")
if may in month2:
    print("we have may")
  
for value in month1.values():
  print(value)
for key in month1.keys():
  print(key)
  
for month_name,month_number in month1.items():
  print(f"{month_name} is {month_number}")

# add all numbers between 1-10 
sum = 0 
counter = 1
while counter <= 10:
  sum = sum + counter   # sum += counter
  counter += 1          # counter = counter + 1
  
print (f"sum is {sum}")
# initialize sum accumulator, to 0 before the loop
# within the loop add each item
sum = 0
for num in range(1,11):
  sum += num
  # print (f"sum is {sum}")   # debug 

print (f"sum is {sum}")

for i in range(5, 96, 5):
  print(i, end='-')
print()
for letter in "Python is great":
    print(letter*2, end='')

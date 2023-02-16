# isEven() 
# code isOdd() yourself

def is_even(num):
  if num % 2 == 0:
    result = True
  else:
    result = False 
  return result
  
def is_even2(num):
  return num % 2 == 0
    
'''
don't check again only 2 possibilities 
if num % 2 == 0:
    result = True
elif  num % 2 != 0:
    result = False 
'''

print (f"2 even {is_even(2)}")
print (f"7 not even {is_even(7)}")

num = 2224
if is_even2(num):
  print(f"{num} is even")
else:
  print(f"{num} is NOT even")

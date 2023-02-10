# examples of functions  & using the random library
# pmcampbell
# 2023-02-10

import random
'''
random rolls of dice, sides as parameter
display the results
no return
'''
def better_roll(sides):
  roll1 = random.randint(1,sides)
  roll2 = random.randint(1,sides)
  print(f'{sides} sided dice, here comes heaven {roll1} {roll2}')

''' 
random rolls of 2x 6 sided dice
display the results
no return
'''
def roll():
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,6)
  print(f'7-11 here comes heaven {roll1} {roll2}')

''' 
random rolls of 2x 6 sided dice
return both dice
'''
def roll_return():
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,6)
  return roll1, roll2
  
print("calling 6 sided")
roll()
roll()
roll()
roll()

dice_sides = int(input("How many sides to your dice: "))
print(f"calling {dice_sides} sided")
better_roll(dice_sides)
better_roll(dice_sides)
better_roll(dice_sides)
better_roll(dice_sides)

print(f"calling 6 sided, returns a tuple")
roll1, roll2 = roll_return()
print(f'7-11 here come\'s heaven {roll1} {roll2}')
roll1, roll2 = roll_return()
print(f'7-11 here come\'s heaven {roll1} {roll2}')


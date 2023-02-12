# 6/49 pick generator
# using random library generate 6 numbers & a bonus
# all between 1-49 inclusive
# display results
# pmcampbell
# 2023-02-06

import random

# 6 numbers 
pick1 = random.randint(1,49)
# print (pic1)
pick2 = random.randint(1,49)
pick3 = random.randint(1,49)
pick4 = random.randint(1,49)
pick5 = random.randint(1,49)
pick6 = random.randint(1,49)

# check if user wants a bonus number
# https://loteries.lotoquebec.com/en/lotteries/lotto-6-49
answer = input("Do you want an extra? ")
if answer == 'y':
  # bonus number (extra)
  bonus = random.randint(1,49)
  print(f"Winning numbers: {pick1} {pick2} {pick3} {pick4} {pick5} {pick6} bonus {bonus}")
else: 
  print(f"Winning numbers: {pick1} {pick2} {pick3} {pick4} {pick5} {pick6} no extra")

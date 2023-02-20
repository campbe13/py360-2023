
# exercises from week5 lab on if/else/elif
# pmcampbell
# 2023-02-17

#1 isVowel() is in it's own file, check the other files

#2 vote_and_drink() 
'''
vote and drink, given an age determine if a person can vote or drink
parameter age  in years
returns tuple of boolean values (vote, drink)
'''
def vote_and_drink(age):
  if age >= 21:
    vote,drink = True,True
  elif age >= 18:
    vote = True
    drink = False
  else:
    drink = vote = False
  return vote,drink


can_vote,can_drink = vote_and_drink(21) # both True
print("vote",can_vote, "drink",can_drink)
can_vote,can_drink = vote_and_drink(19) # True, False
print("vote",can_vote, "drink",can_drink)
can_vote,can_drink = vote_and_drink(12) # both False
print("vote",can_vote, "drink",can_drink)

#2 richter() 
def richter(magnitude):
  if magnitude < 2:
    descriptor = "Micro"
  elif magnitude < 3:
    descriptor = "Very minor"
  elif magnitude < 4:
    descriptor = "Minor"
  elif magnitude < 5:
    descriptor = "Light"
  elif magnitude < 6:
    descriptor = "Moderate"
  elif magnitude < 7:
    descriptor = "Strong"
  elif magnitude < 8:
    descriptor = "Major"
  elif magnitude < 10:
    descriptor = "Great"
  else:
    descriptor = "Meteoric"
  return descriptor

# using range to test 
# range returns ints
# range(start, stop, increment)
# for float range, need numpy
for magnitude in range (1, 11):
  print(f'A magnitude {magnitude} earthquake is considered to be {richter(magnitude)}')
  
#4 pass_fail() 
'''
given a grade, determine if it is a pass
parameter: grade
return True if pass, False if fail

note: a better name for this fuction would be isPass()
'''
def pass_fail(grade):
  return grade >= 60
def pass_fail1(grade):
  if grade >= 60:
    result = True
  else:
    result = False
  return result

for grade in range(40, 80, 10):
  if pass_fail(grade):
    print(f"{grade} you passed! :)")
  else:
    print(f"{grade} you failed :(")

#5 calculate_tip(rate,cost):
'''
given a tip rate & cost of meal, return the tip amount
parameter rate of tip, cost of meal
return  tip amount
'''
def calculate_tip(rate,cost):
  if rate > 1:
    rate = rate / 100
  tip = rate*cost
  return(tip)
  
cost = 11.45
rate = 15
print(f'{cost} % {rate} tip amt {calculate_tip(rate,cost)}')

cost = 3.75
rate = .1
print(f'{cost} % {rate} tip amt {calculate_tip(rate,cost)}')

#5 animal_sounds(pet):
'''
given a type of pet return the sound it makes 
parameter string type of pet
return string sound
'''
def animal_sounds(pet):
  if pet == "dog":
    sound = "woof"
  elif pet == "cat":
    sound = "meow"
  elif pet == "mouse":
    sound = "squeak"
  elif pet == "elephant":
    sound = "trumpet"
  else:
    sound = "oink"
  return sound

for pet in ["mouse","elephant","dog","cat","horse"]:
  print(f'your {pet} says {animal_sounds(pet)}')
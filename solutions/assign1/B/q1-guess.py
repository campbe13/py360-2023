'''
Q1 guess
'''
import random
secret = random.randint(5,555)
print(f"secret {secret}")

guess = int(input("guess a number btw 5-555: "))
# ifs only
if guess < secret:
  print("guess higher")
if guess > secret:
  print ("guess lower")
if guess == secret:
  print("you guessed it!")
# using if/elif/else
if guess < secret:
  print("guess higher")
elif guess > secret:
  print ("guess lower")
else: 
  print("you guessed it!")
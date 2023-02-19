'''
Q1 guess
'''
import random
secret = random.randint(123,700)
print(f"secret {secret}")

guess = int(input("guess a number btw 123-700: "))
# ifs only
if guess < secret:
  print("too low")
if guess > secret:
  print ("too high")
if guess == secret:
  print("you guessed it!")
# using if/elif/else
if guess < secret:
  print("too low")
elif guess > secret:
  print ("too high")
else: 
  print("you guessed it!")
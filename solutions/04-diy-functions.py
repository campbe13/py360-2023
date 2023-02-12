# Write a series of functions 
# note the funcitons are just before the tests to make it clearer
# normally the functions would be defined at the top of the file 
# and the funciton calls at the bottom
#
# pmcampbell
# 2023-02-09

import math

'''
#1
right angle triangle
params 2 sides
returns hypotenuse length
'''
def hypotenuse_length(side1, side2):
  length = math.sqrt((side1**2 + side2**2))
  return length

# testing 
# sides 12, 33 expected 35.114  
# sides 41, 3 expected 41.109
print(f"12,33 hyp: {hypotenuse_length(12,33):.3f}")
print(f"41,3 hyp: {hypotenuse_length(41,3):.3f}")


'''
#2
right angle triangle perimeter
params 2 sides
returns perimeter
'''
def perimeter(side1, side2):
  length = math.sqrt((side1**2 + side2**2))
  return length + side1 + side2

# testing 
# sides 12, 33 hyp 35.114  expected 80.114
# sides 41, 3 hyp 41.109 expected 85.109
print(f"12,33 perimeter: {perimeter(12,33):.3f}")
print(f"41,3 perimeter: {perimeter(41,3):.3f}")

'''
#4
height of a tree
params distance, angle 
returns height
'''
def tree_height(distance, angle):
  radians = math.radians(angle)
  height = math.tan(radians) * 100
  return height

# testing 
# distance 12, angle 70 expected 514.455
# distance 100, angle 18 expected 32.492
print(f"dist 12m, angle 79 height: {tree_height(12,79):.3f}")
print(f"dist 100m, angle 18 height: {tree_height(100,18):.3f}")

'''
#3
decide on optimal change to return
params dollars and change, float
returns an f string 
'''
def optimal_change(total_money):
  # convert to int bc cannot have half a coin
  cents = int(total_money * 100 )
  toonie  = cents // 200
  cents = cents - toonie* 200
  loonie  = cents // 100
  cents = cents - loonie * 100
  quarter = cents // 25
  cents = cents - quarter * 25
  dime = cents // 10
  cents = cents - dime * 10
  nickel = cents // 5
  cents = cents - nickel * 5
  return f'Toonies: {toonie}, Loonies:{loonie}, Quarters: {quarter}, Dimes: {dime}, Nickels: {nickel}, Pennies: {cents}'

# testing 
# verified with http://www.csgnetwork.com/moneycounter.html
# 4.31 Toonies 2 Loonies 0 Quarters 1 Dimes 0 Nickels 1 Pennies 1
# 13.91 Toonies 6 Loonies 1 Quarters 1 Dimes 1 Nickels 1 Pennies 1
print(optimal_change(4.31))
print(optimal_change(13.41))
  
'''
#3
WITHOUT CONVERT TO INT  
note the pennies results (imprecision, due to floating point)
decide on optimal change to return
params dollars and change, float
returns an f string 
'''
def optimal_change_float(total_money):
  # convert to int bc cannot have half a coin
  cents =  total_money * 100
  toonie  = cents // 200
  cents = cents - toonie* 200
  loonie  = cents // 100
  cents = cents - loonie * 100
  quarter = cents // 25
  cents = cents - quarter * 25
  dime = cents // 10
  cents = cents - dime * 10
  nickel = cents // 5
  cents = cents - nickel * 5
  return f'Toonies: {toonie}, Loonies:{loonie}, Quarters: {quarter}, Dimes: {dime}, Nickels: {nickel}, Pennies: {cents}'

# 4.31 Toonies 2 Loonies 0 Quarters 1 Dimes 0 Nickels 1 Pennies 1
# result
# Toonies: 2.0, Loonies:0.0, Quarters: 1.0, Dimes: 0.0, Nickels: 1.0, Pennies: 0.9999999999999432
print(optimal_change_float(4.31))

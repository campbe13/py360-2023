# calculate the distance to sea bed from a boat
# given (input) the length of the anchor cable and the angle of the cable
# pmcampbell
# 2023-01-31

# test data: 
# length = 30 m 
# angle = 51 degrees 
# answer: 18.88 m
# length = 100 m 
# angle = 31 degrees 
# answer: 85.72 m
# for others use https://www.calculator.net/right-triangle-calculator.html

import math

# code here
def calculate_depth(cable_length, cable_angle):
  theta = 90 -  cable_angle
  #print (f'seabed & cable angle is {theta}')  
  theta_in_radians = math.radians(theta)
  depth = math.sin(theta_in_radians) * cable_length
  return depth
  
cable_length = float(input("What is your anchor cable length: "))
cable_angle = float(input("What is the angle between your anchor cable & perpendicular: "))

# using a variable  (if we want to use the result of the func in another calc, use a variable)
distance_to_seabed = calculate_depth(cable_length, cable_angle)
print (f'distance to seabed {distance_to_seabed:.2f}')

#same thing, using func call inside an f string
print (f'distance to seabed {calculate_depth(cable_length, cable_angle):.2f}')

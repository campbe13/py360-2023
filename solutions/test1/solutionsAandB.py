# Solutions for test 1 2023
# Version A and B

import math
# 8 area of regular polygon (also in examples )
''' 
calculate the area of a regular polygon
ref https://www.mathopenref.com/polygonregulararea.html
parameter number of sides
returns area
https://www.calculatorsoup.com/calculators/geometry-plane/polygon.php
https://www.omnicalculator.com/math/regular-polygon-area
'''
def areaA(side, count):
  top  = side**2 * count
  radians = math.radians(180/count)
  bottom = 4* math.tan(radians)
  area = top/bottom
  return area
  
length =  5
count  = 6
# result 64.9519052838329
print(f'A length of a side {length} number of sides {count} area of regular polygon {areaA(length,count)}')
length =  10.5
count  = 3
# result 47.739650383617196
print(f'A length of a side {length} number of sides {count} area of regular polygon {areaA(length,count)}')

def areaB(apothem, count):
  return  apothem**2 * count * math.tan(math.pi/count)
# apothem 4.33
length = 4.33
count = 12
# result 60.28503136766251
print(f'B apothem of a side {length} number of sides {count} area of regular polygon {areaB(length,count)}')
length = 1.23
count = 7

print(f'B apothem of a side {length} number of sides {count} area of regular polygon {areaB(length,count)}')


# A1
def sum_even(num1, num2, num3):
#def sum_even(num1, num2, num3, num4, num5):
  sum = 0 
  num1 = round(num1)
  num2 = round(num2)
  num3 = round(num3)
  # num4 = round(num4)
  # num5 = round(num5)
  if num1 % 2 == 0:
    sum = sum + num1
  if num2 % 2 == 0:
    sum = sum + num2
  if num3 % 2 == 0:
    sum = sum + num3
  # if num4 % 2 == 0:
  #   sum = sum + num4
  # if num5 % 2 == 0:
  #   sum = sum + num5
  return sum 
  
# print(sum_even(1,2.1,3.3,4.2,5) )
# print(sum_even(1,7.6,9,32.5,55))

print(sum_even(6,2.1,3.3) )
print(sum_even(1,7.4,9.1))

# B1
def sum_odd(num1, num2, num3):
#def sum_even(num1, num2, num3, num4, num5):
  sum = 0 
  num1 = round(num1)
  num2 = round(num2)
  num3 = round(num3)
  # num4 = round(num4)
  # num5 = round(num5)
  if num1 % 2 != 0:
    sum = sum + num1
  if num2 % 2 != 0:
    sum = sum + num2
  if num3 % 2 != 0:
    sum = sum + num3
  # if num4 % 2 == 0:
  #   sum = sum + num4
  # if num5 % 2 == 0:
  #   sum = sum + num5
  return sum 
  
# print(sum_even(1,2.1,3.3,4.2,5) )
# print(sum_even(1,7.6,9,32.5,55))

print(sum_odd(1,2.1,3.3) ) #4
print(sum_odd(1.7,6,9.8))  #0
# q3 A alarm() B wake()
def alarm(time, sleep):
  return (time + sleep)%24

print ("alarm")
print(alarm(21,9)) # 6
print(alarm(3,9)) # 12
print(alarm(24,9)) # 9

print(alarm(17,10)) # 3
print(alarm(4,7)) # 11

def wake (time, sleep):
  return (time - sleep)%24

print ("wake")
print(wake(21,9)) # 12
print(wake(3,9)) # 18

print(wake(17,10)) # 7
print(wake(4,7)) # 21

# q4 A light() B wave()
# B
def wave(wavelength):
  if wavelength <  380  or wavelength > 740:
    return "error","error"
  if wavelength >= 610 and wavelength <= 740:
    colour = "Red"
    description = "RBV"
  elif wavelength >= 565 and wavelength <= 599:
    colour = "Yellow"
    description = "blank"
  elif wavelength >= 510 and wavelength <= 564:
    colour = "Green"
    description = "blank"
  elif wavelength >= 423  and wavelength <= 450:
    colour = "Blue"
    description = "RBV"
  elif wavelength >= 380 and wavelength <= 400:
    colour = "Violet"
    description = "RBV"
  else:  
    colour = "Unknown"
    description = "blank"
  return colour, description

print(wave(654))
print(wave(577))
print(wave(522))
print(wave(425))
print(wave(1))
print(wave(411))

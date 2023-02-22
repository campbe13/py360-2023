# Write and test your own functions!
import random, math

# 1 doughnuts(quantity)
'''
calculate the cost of doughnuts 
parameter count of doughnuts
returns cost
'''
def doughnuts(quantity):
  if quantity < 6:
    cost = 1.29 * quantity
  elif quantity < 12:
    cost = 1.10 * quantity
  elif quantity > 12:
    cost = 1.05 * quantity
  else: 
    cost = 11.99
  return cost

# 4  @ 5.16
# 12 @ 11.99
# 14 @ 14.70
# 7  @ 7.70
for quantity in [4, 12, 14, 7]:
  print(f'{quantity} costs {doughnuts(quantity):.2f}')

#2 dice_game()
'''
simulate a dice game with 2 six sided lights
parameter count of doughnuts
returns cost
'''
def dice_game():
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  if dice1 + dice2 == 7 or dice1 + dice2 == 11 or dice1 == dice2:
    return "win"
  else:
    return "lose"

print("play ", dice_game())
print("play ", dice_game())
print("play ", dice_game())

#3 day_old_pastries(count)
def day_old_pastries(count):
  PASTRY = 5.49
  cost = PASTRY * count
  discount = cost * .6
  return cost, discount

# 1 @ 5.49 & 3.29
# 5 @ 27.45 & 16.47
# 8 @ 43.92 & 26.35
for count in [1, 5, 8]:
  total, discounted = day_old_pastries(count)
  print(f'{count} before discount {total:.2f} after {discounted:.2f}')

# 4 PST & QST
'''
calculate GST
parameter cost
returns gst amount
'''
def GST(cost):
  if cost < 0:
    return 0
  return cost  * .05
  
'''
calculate PST
parameter cost
returns pst amount
'''
def PST(cost):
  if cost < 0:
    return 0
  return cost  * .09975
  
# 15.43 GST 0.77, pst 1.54
cost = 15.43
print(f'Purchase {cost}$ GST {GST(cost):.2f}$ PST {PST(cost):.2f}$')
# 10.00 GST 0.05, PST 0.09975
cost = 10.0 
print(f'Purchase {cost}$ GST {GST(cost):.2f}$ PST {PST(cost):.2f}$')

# 5 plus_tax, use PST & QST
'''
calculate gst, pst and total cost
parameter cost
return tuple cost + tax, gst, pst
'''
def plus_tax(cost):
  gst = GST(cost)
  pst = PST(cost)
  return cost+gst+pst, gst, pst
  
cost = 10.0
total, gst,pst = plus_tax(cost)
print(f'Purchase total {total:.2f} = cost {cost}$ + GST {gst:.2f}$ + PST {pst:.2f}$')
print(f'Purchase total {total} = cost {cost}$ + GST {gst}$ + PST {pst}$')

# 6 area of right angle triangle

'''
calculate the area of a right angled triangle
parameter base and height length
returns area
'''
def area_triangle(base,height):
  return base*height/2
base = 10
height = 15
# result 75
print(f'{base} {height} area of ra triangle {area_triangle(base, height)}')

# 7 area of  triangle
'''
calculate the area of a  triangle
using heron's formula
ref https://www.mathsisfun.com/geometry/herons-formula.html
parameter three sides
returns area
'''
def area_triangle2(side1, side2, side3):
  s = (side1 + side2 + side3 )/2
  area = math.sqrt(s* (s-side1)* (s-side2)* (s-side3))
  return area
  
side1, side2, side3 = 5,5,5
# result 10.82531
print(f'{side1} {side2} {side3} area of triangle {area_triangle2(side1, side2, side3)}')

# 8 area of regular polygon
'''
calculate the area of a regular polygon
ref https://www.mathopenref.com/polygonregulararea.html
parameter length and number of sides
returns area
'''
def area_reg_polygon(side, count):
  top  = side**2 * count
  radians = math.radians(180/count)
  bottom = 4* math.tan(radians)
  area = top/bottom
  return area
  
length =  5
count  = 6
# result 64.951
print(f'length of a side {length} number of sides {count} area of regular polygon {area_reg_polygon(length,count)}')

# 9 windchill index 
'''
calculate the windchill
ref https://weather.gc.ca/windchill/wind_chill_e.html
parameter wind speed in kph, temperature celsius
returns windchill index
'''
def windchill_index(temperature, wind_speed):
   if temperature >10:
     return 0
   chill = 13.12 + 0.6215 *  temperature \
          - 11.37*(wind_speed**0.16) \
          + 0.3965*temperature*(wind_speed**0.16)
   return chill
wind = 35
temperature = -5
# result -13.57
print(f'temp {temperature} wind kph {wind} chill {windchill_index(temperature, wind)}')

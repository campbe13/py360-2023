import math
'''
Q3 angle of the sun
tan (theta)   = opp /adj
tan (theta)   = pole / shadow 
theta  = arctan (pole/shadow)
soh-cah-toa

http://www.carbidedepot.com/formulas-trigright.asp
'''
def sun(pole, shadow):
  tan_theta = pole / shadow
  angle = math.atan(tan_theta)
  return math.degrees(angle)
# pole 18, shadow 12, angle 56.309932474020215
print(f"sun pole 18 shadow 12 angle {sun(18,12):.4f}")
# pole 5.5, shadow 3.7, angle 56.07020257793936
print(f"sun pole 5.5 shadow 3.7 angle {sun(5.5, 3.7):.4f}")
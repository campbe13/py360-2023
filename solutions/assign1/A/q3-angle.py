import math
'''
Q3 angle of the ladder
sin (theta)   = opp / hyp
sin (theta)   = height / ladder
theta  = arcsin (height/ladder)
soh-cah-toa

http://www.carbidedepot.com/formulas-trigright.asp
'''
# ladder 30, height 20m 
def angle(height, ladder):
  sin_theta = height / ladder
  angle = math.asin(sin_theta)
  return math.degrees(angle)

# ans 41.810314895778596
print(f"ladder leng 30m building height 20m angle {angle(20,30):.4f}")
# ans 55.1745
print(f"ladder leng 5m building height 6m angle {angle(5.5,6.7):.4f}")
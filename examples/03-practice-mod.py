# code some clock addition together using %
# 12 hour clock

def add_hours_12(hour, add_hours):
  new_hour = (hour + add_hours) %12
  if new_hour == 0:
    new_hour = 12
  #print("new_hour " + str(new_hour) + " O'clock")  
  print(f'new_hour {new_hour} O\'clock')  

def add_hours_24 (hour, add_hours):
  new_hour = (hour + add_hours) %24
  print(f'new_hour {new_hour}h 24h clock')  

add_hours_12(11, 1)  # 12 O'clock
# add_hours_24(12,13)  # 1
# add_hours_24(12,5)   # 17
add_hours_12(11,10)  # 9
add_hours_12(11, 17)  # 4
add_hours_12(10, 15)  # 1
# hour = 11
# # add hours without exceeding 12 
# new_hour = (hour +  1)%12
# print("new_hour" + str(new_hour))
# new_hour = (hour + 10)% 12
# print("new_hour", new_hour)
# new_hour = (hour + 17)% 12
# print("new_hour", new_hour)

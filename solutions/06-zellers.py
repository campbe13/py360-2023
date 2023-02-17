# this is a program that will given a day, year month, determine the day of the week
# it uses Zeller's congruence algorithm 
# ref https://en.wikipedia.org/wiki/Zeller%27s_congruence

# pmcampbell
# 2023-02-18

'''
implement zeller's algorithm
parameter: year (yyyy), month(mm) day(dd) 
returns day of the week 0-6 ( 0 is Sunday)
'''
def zeller(year, month, day):
  c = year//100 
  y = year %  100
  m = month -2
  if m < 1:
    m = m + 12
    y = y - 1 
  print (y, c, m)
  day_number = ( (26*m - 2) // 10 + day + y + y//4 + c//4 +5 *c) % 7
  print("testing day#", day_number)
  return day_number
'''
same as above but illustrates a formula in error due to using decimal division!
'''
def zeller_error(year, month, day):
  c = year//100 
  y = year %  100
  m = month -2
  if m < 1:
    m = m + 12
    y = y - 1 
  print (y, c, m)
  day_number = ( (26*m - 2) / 10 + day + y + y/4 + c/4 +5 *c) % 7
  print("testing day#", day_number)
  return day_number

'''
given a numbered day, return a string naming the day
parameter  day of the week 0-6
returns  text for the day of the week ( 0 is Sunday)
'''
def day_name(day_number):
  if day_number == 0:
    day =  "Sunday" 
  elif day_number == 1:
    day = "Monday"
  elif day_number == 2:
    day =  "Tuesday"
  elif day_number == 3:
    day =  "Wednesday"
  elif day_number == 4:
    day =  "Thursday"
  elif day_number == 5:
    day =  "Friday"
  else:
    day =  "Saturday"
  return day

#code the main function below
'''
main() is the entry point for a program
ask for the year, month, day
use the functions to determine the name of the associated day of the week
Display the information
'''
def main():
  year = int(input("enter a year: "))  
  month = int(input("enter a month: "))  
  day = int(input("enter a day: "))  
  day_zeller = zeller(year,month,day)
  print(f"WITH floor division \nThat  day is/was/will be a {day_name(day_zeller)}")
  print(f"ERROR using decimal division \nThat day is/was/will be a {day_name(zeller_error(year,  month, day))}")


# Code below ensures that the function called main is invoked when you run
if __name__ == "__main__":
    main()
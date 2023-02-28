# demo
# testing using range
# for count in range(5,0, -2):
#   print(count)
import random
'''
given a starting point & an increment/decrement 
display a count down
params start, increment
return None
'''
def countdownby(start, increment):
  increment = abs(increment)
  for count in range(start,0, -increment):
      print(count)
  print("Blastoff", "!"*start)
'''
count the number of marks over 90
param list of grades
return count of over 90
'''
def count_grades(grades_list):
  count = 0
  for grade in grades_list:
    if grade  > 90:
      count += 1
  return count
'''
for testing (I think it's not useful otherwise)
create a list of grades
parameter list size
returns  list
'''
def create_grades(size):
  grades = [] 
  for x in range(size):  
    grade = random.randint(0,100)
    #print("generated ", grade)
    grades.append(grade) 
    #print(grades)
  return grades
  
def main():
  # testing create grades list func
  grades3 = create_grades(random.randint(2,105))
  # last element of a list
  print (grades3, len(grades3 ))
  print("last element", grades3[len(grades3)-1], grades3[-1], )
  # testing count grades > 90
  grades = [10, 11, 12]
  grades2 = [10, 11, 12, 91, 92, 93]
  for list in (grades, grades2, grades3):
    print (list)
    print ("over 90", count_grades(list) )
  # testing count down function
  countdownby(5,1)
  countdownby(50, 5)
  countdownby(50, -5)
  

if __name__ == "__main__":
     main()

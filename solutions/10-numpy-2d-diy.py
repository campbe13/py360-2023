# working with numpy
# 
import numpy as np
import math
'''
calculate the average grade for each class 
parameter  a numpy 1d or 2d array
returns a new 1d array with the average mark
with every item doubled
'''
def grade_average(gradesarray):
  classesct,gradesct = gradesarray.shape
  averages = np.zeros(classesct)
  ix = 0
  for course in gradesarray:
    averages [ix]  = course.mean()
    ix += 1
  return averages    

'''
calculate the trace of an array 
param: array
return trace
'''      
def trace(array):
  rows,cols = array.shape
  # only useful on a square matrix
  if rows != cols:
    return None
  trace = 0
  for i in range(rows):
    trace += array[i][i]
  return trace
  
  
'''
add 2 arrays, result in a third
params 2x arrays 
return array sum of the arrays'''
def sum(array1,array2):
  if array1.shape != array2.shape:
    return None
  rows,cols = array1.shape
  sum2 = np.zeros_like(array1)
  for i in range(rows):
    for j in range(cols):
      sum2[i][j] = array1[i][j]+array2[i][j]
  return sum2

'''
compare 2 arrays, item by item
params 2x arrays 
return True if all elements match, else False
'''
def compare(array1,array2):
  if array1.shape != array2.shape:
    return None
  rows,cols = array1.shape
  sum2 = np.zeros_like(array1)
  for i in range(rows):
    for j in range(cols):
      if array1[i][j] != array2[i][j]:
        return False
  return True
  
def main():
  #  2d arrays
  

  print("grade_average()--------------------")
  grades = [[55,66,77], [95,76,25], [55,25,97]]
  gradesnp = np.array(grades)
  print(gradesnp, type(gradesnp))
  averages = grade_average(gradesnp)
  ix  = 0
  for course in gradesnp:
    print(f"grades {course} average {averages[ix]:.2f}")
    ix += 1
    
  print("\ntrace()--------------------") 
  print("calc ",trace(gradesnp))
  print("numpy.trace() ",gradesnp.trace())
  print("numpy.diagonal().sum() ",np.diagonal(gradesnp).sum())

  print("\nsum()--------------------") 
  print(gradesnp)
  calcvalue = sum(gradesnp,gradesnp)
  print("calc", calcvalue)
  print("+", gradesnp+gradesnp)
  print('calc vs + values same\n', calcvalue == (gradesnp+gradesnp))

  print("\ncompare()--------------------") 
  print(gradesnp)
  print(compare(gradesnp, gradesnp))
  print(gradesnp == gradesnp)
  other = np.copy(gradesnp)
  other [1,2] = 5
  print(other)
  print(compare(gradesnp, other))
  print(gradesnp == other)

if __name__ == "__main__":
  main()

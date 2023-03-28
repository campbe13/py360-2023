# using arrays with numpy

import numpy as np 

# list
grades =  [ 99, 55, 76, 85]

# use a list to create a numpy array
grades_np = np.array(grades)

print (grades_np)
print(type(grades_np))

# create an empty zeroed numpy array
grades_360 =  np.zeros(5)
print(grades_360)
print(type(grades_360))

grades_440 = np.empty(10)

print(grades_440)
print(type(grades_440))

sequence = np.arange(6)  # 6 elements 0-5 in my array
print(sequence)

# just like range() start, stop, skip
seq2 = np.arange(2,13,2)
print(seq2)

seq2 = np.arange(2,13,1.5)
print(seq2)

# nums over an interval
# start, stop, count of elements
seq4 = np.linspace(1,10, 3)
seq3 = np.linspace(1,1000, 100)
print (seq3)

seq4 = np.linspace(1,10, 3)
print(seq4)
# low, high, size
rand = np.random.randint(1,1000,10)
print(rand)
# low, high, size
rand_float = np.random.uniform(1,1000,12)
print(rand_float)

grades_list =  [ 99, 55, 76, 85]

# use a list to create a numpy array
grades = np.array(grades_list)

print (grades, len(grades))
print(grades[0])

for i in range(len(grades)):
  print(i, grades[i])

# add 2
for i in range(len(grades)):
  grades[i] += 2

print(grades)

for grade in grades:
  print (grade)

## 2d arrays
grades_440 =  [ 99, 55, 76, 85]
grades_360 =  [ 89, 65, 66, 75]

grades_all = np.array([grades_440, grades_360] )
print (grades_all)
print(type(grades_all))
# 1st element of 2nd row
print (grades_all[1,0])


arr2d = np.arange(1,9).reshape(2,4)
print(arr2d)
arr2d = np.arange(1,10).reshape(3,3)
print(arr2d)

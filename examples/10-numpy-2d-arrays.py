# examples of 2d arrays using numpy
#
import numpy as np

'''
consider 2d arrays 
think of it as a list or 1d array where each element is an array
so you can think of them as if they are arrays of arrays 
''' 


arr2d = np.array( [[1, 2, 3], [3, 4, 5]])
print (arr2d)
# attributes of a numpy array
# will tell you how many dimensions
print("dimensions in array",arr2d.ndim) 
# try shape, size, dtype, itemsize, data  (itemsize in bits, individ elements)
print("element 1,2 in array", arr2d[1, 2])   

'''
copy, weird results, same memory shown for each
don't show students ??
https://stackoverflow.com/questions/41315280/what-is-a-python-buffer-object-pointing-to-the-start-of-the-array-s-data 
'''
arr3 = np.copy(arr2d)
arr3[0,0] = 99
arr2d[0,0] = 125
print(arr3,arr3.data)
print(arr2d, arr2d.data)


'''
# don't show students n dimensional array
nd = np.ndarray(shape=(3,3,3))
print (nd)
print(nd.ndim)
''' 

arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print (arr2d)
# will tell you how many dimensions
print("dimensions in array",arr2d.ndim) 
print("element 2,0 in array", arr2d[2,0])   

# What happens?
# VisibleDepricationWarnning
# DO NOT USE
# works but deprecated – rows with different lengths
arr2d = np.array( [[1, 2, 3], [3]])  
print (arr2d)

''' other ways to create 2d arrays '''
# arange(1,9) fill with 1 to 9
# reshape(2,4) reshape into 2 row x 4 column matrix 
another = np.arange(1,9).reshape(2,4)
print(another)
another = np.arange(1,9).reshape(4,2)
print(another)

another  = np.arange(1,10).reshape(3,3)
print(another)
another  = np.arange(1,5).reshape(2,2)
print(another)
#another  = np.arange(1,5).reshape(3,3) # ???
#print(another)

''' 2d arrays with random numbers '''
arrfloat = np.random.uniform(0, 100, (4, 5))
print(arrfloat)
arrint = np.random.randint(0, 100, (5, 4))
print(arrint)
'''
-> the third parameter is a shape tuple 
- the shape indicates the number of arrays (1st  think as rows) and how may elements in each (2nd - think as columns)
'''

'''iterate through a 2d array - need nested loops '''
another = np.arange(0,100).reshape(10,10)
colcount = 0
rowcount = 0
# each row is a 1d array
for row in another:
   print(row)
for row in another:
  for col in row:
    print (col)

'''Create a random 3x3 array, and manipulate the elements:'''
# backup/copy
arrint = np.random.randint(0, 100, (3, 3))
backup_arrint = np.copy(arrint)

''' 
solution 1 use a range to iterate through the rows,
for each row use a range to iterate through the columns
multiply by 2
'''
print (arrint)
for i in range(len(arrint)):
    for j in range(len(arrint[i])):
        arrint[i, j] = 2*arrint[i, j]
print ("doubled")
print(arrint)
''' 
solution 2 itterate through the rows of the array
for each row use a range to iterate through the columns
multiply by 3
'''
arrint = np.copy(backup_arrint)
print (arrint)
for row in arrint:
    for i in range (len(row)):
        row[i] = 3* row[i]
print ("tripled")
print(arrint)

''' 
solution 3 or use a nice property  of python np arrays!!! 
(optimized for mathematics remember!)
use a range to iterate through the rows,
for each row use a range to iterate through the columns
multiply by 4
'''
arrint = np.copy(backup_arrint)
print (arrint)
arrint = 4*arrint
print ("quadrupled",arrint)
arrint = np.copy(backup_arrint)
print(arrint)
arrint = arrint+4
print ("plus 4")
print(arrint)

''' useful numpy methods '''
arr1 = np.random.uniform(0, 10, (3, 3))
print(arr1)
print("mean ",np.mean(arr1))
print("std dev ",np.std(arr1))

arr1 = np.random.randint(0, 10, (3, 3))
arr2 = np.random.randint(0, 10, (3, 3))
print("arr1")
print(arr1)
print("arr2")
print(arr2)

print("addition arr2+arr1")
print(arr2+arr1)

print("multiplication arr2@arr1")
print(arr2@arr1)

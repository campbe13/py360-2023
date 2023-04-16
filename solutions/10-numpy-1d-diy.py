# working with numpy
# 1 dimensional arrays 
# 
import numpy as np
import math
'''
takes a numpy 1d array and returns a new one
with every item doubled
'''
def double(array):
  # we have to create our new array first
  
  # 2d would need same shape
  # create empty array, same shape   
  # double = np.empty_like(array)
  # create array, same shape, zero fill
  # double = np.zeros_like(array)
  
  # 1d so len or size ok
  # dub = np.zeros(len(array)
  double = np.zeros(array.size)
  # then use an index to go through every element in the array
  for ix in range(array.size):
    double[ix]  = 2 * array[ix]  
  return double
  
'''
create & fill a numpy array with random rolls between 1 and 6
using numpy functions
parameters
size:  size of array
return numpy array of dice rolls
'''      
def dice_rolls(size):
  return np.random.randint(1, 7, size)
  
''' 
generate an array, for each element count the number of elements in the array
that are greater, 

note this code covers 1d 
size: size of array
return the results in a new numpy array
test data
  randarray = np.array([65, 87, 32, 53, 2, 5, 23])
  result should be  [1,0,3,2,6,5,4]
  
'''
def random_array(size):
  ''' 
  test data
  randarray = np.array([65, 87, 32, 53, 2, 5, 23])
  '''
  randarray = np.random.randint(0, 100, size)
  
  counts = np.zeros(randarray.size) # init the counter array
  # use each element in the array
  # note 
  #  i is the ix for the element we are comparing to the rest
  #  j is the ix for the array (go through the whole array for each i)
  for i in range(randarray.size):
      # for each element randarray[i] need to look through the 
      # entire array to find which ones are greater: change j 
      for j in range(randarray.size):
         if randarray[i] < randarray[j]:
           counts[i] += 1
  return randarray, counts

'''
calculate & return the std dev of the given array
param: array
return: std dev

Note followed this algo, but get different results to numpy so slightly off (errors)  
    Calculate the mean as discussed above. The mean of [1, 2, 3, 4, 5] is 3.
    Calculate variance for each entry by subtracting the mean from the value of the entry. So variance will be [-2, -1, 0, 1, 2].
    Then square each of those resulting values and sum the results. For the above example, it will become 4+1+0+1+4=10.
    Then divide the result by the number of data points minus one. This will give the variance. So variance will be 10/(5-1) = 2.5
    The square root of the variance (calculated above) is the standard deviation. So standard deviation will be sqrt(2.5) = 1.5811388300841898.
'''
def stddev(array):
  # array = np.array([1, 2, 3, 4, 5] )
  # print(array)
  # print(array.mean())
  variance = np.zeros(array.size)
  ix = 0
  for elem in array:
    variance[ix] = elem - array.mean()
    ix += 1
  # print (variance)
  sum = 0
  for elem in variance:
    # print(elem**2)
    sum += elem**2 
  # print (sum, array.size-1)  
  # print("numpy", array.std())
  # print("calc", sum/(array.size-1))
  return math.sqrt(sum/(array.size-1))

def main():
  # create a new array
  print("double()--------------------")
  array1d = np.array([5,1,7])
  print("array1",array1d)
  print("double", double(array1d))
  
  print("\ndice_rolls()--------------------")
  dice = dice_rolls(10)
  print("dice",dice)
  # average (slow)
  sum=0
  for die in dice:
    sum += die
  print(f'slow the average is {sum/len(dice):.2f}')
  
  # better to use the methods & attributes of the array object
  print(f'better dice.sum()/dice.size {dice.sum()/dice.size:.2f}')
  print(f'best dice.mean() {dice.mean():.2f}')
  # max and min 
  minval = maxval = dice[0]  # init min & max
  #min = max
  for die in dice:
    if die<minval:
      minval = die
    if die>maxval:
      maxval=die
  print(f'slow The max is {maxval} and the min is {minval}')
  # python min & max 
  print(f'better The max is {max(dice)} and the min is {min(dice)}')
  # numpy min & max  (np optimized) 
  print(f'best The max is {dice.max()} and the min is {dice.min()}')
  
  print("\nrandom_array()--------------------") 
  # test with 5 
  array,count = random_array(5)
  print("random array",array)
  print("count greater",count)

  print("\nstddev()--------------------") 
  randarray = np.random.randint(0, 100, 10)
  print("numpy", randarray.std())
  print("calc", stddev(randarray))
if __name__ == "__main__":
  main()

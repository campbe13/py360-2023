# NumPy arrays - exercises 

  **using arrays with numpy**

  _list are fine for smaller ops but they are not optimized for mathematical calculations so we use numpy_

  
## Useful
* [Numpy beginners guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
* [Numpy reference](https://numpy.org/ )
## Implement the following functions, test them in main()
### double(array)
  Write a function that takes an array and returns a new array where every item is doubled
  
  Ex array =  5, 1, 7   and greater_array = 10, 2, 14

### dice_rolls(size)  (redux)
  1. Write a function that fills an array of `size` with random numbers between 1 and 6.  (use the numpy function to generate random numbers)
  2. Write code in `main()` to 
     * calculate the average of the returned array
     * find the smallest number in the  array
     * find the largest number in the  array
### array, greater_array = random_array(size) 
Create numpy array with size  random integers between 0 and 100
 (use the numpy function to generate random numbers)
For each element of the array determine the count of elements that are greater than it and put the answer in a new array  (pattern: parallel arrays)

Ex array =  5, 1, 7   and greater_array = 1, 2, 0

### find the standard deviation of the values in an array  `stddev(array)`
Create numpy array with random integers between 0 and 100 
Use it as the argument to your array, return the standard deviation 
![image](image.png)

look up the numpy built in standard deviation function and use it to compare to your result. 
Check the results
# Working with numpy 2d
 **exercises using numpy with 2d arrays**

_you can copy your code from the exercises using numpy with 1d arrays ( or exercises using lists)  & change it to use numpy_

* as always create test data and expected results, then test your code
* note easiest to work with 3x3 arrays of ints, but should work with any array

## Reference
* https://numpy.org/doc/stable/index.html  << use the search
* https://numpy.org/doc/stable/reference/routines.linalg.html

also
* [NumPy Beginners Guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
* [NumPy Math](https://numpy.org/doc/stable/reference/routines.math.html)
* [NumPy Statistics](https://numpy.org/doc/stable/reference/routines.statistics.html)

## an array of grades
Write a function `grade_average()` to take a 2d array of  grades 
as a parameter & return a numpy array containing the average grade for each one. 
(ex rows: 1st array is physics grades, 2nd array is calculus grades, etc )
  * _hint_ you can use your 1d functions from the previous exercises as a starting point
  * _hint_ your averages array  is the same size as the rows of the parameter 2d array
  * _hint_ you are given a 2d matrix in main.py but you can generate your own using other dimensions & randint 0-100 to test your code.
##   calculate the trace
Write a function `trace()` to take a 2d array 
as a parameter & return the trace (sum of diagonal elements).  Do this by looping through the rows, then verify your answer using the numpy function  [np.trace](https://numpy.org/doc/stable/reference/generated/numpy.trace.html) 
## add two matricies
Write a function `sum()` to take two  2d arrays 
as parameters  & returns a new matrix that is the sum of the two.   Do this by looping through the rows, then verify your answer using the `array1+array2` syntax or the   function [np.array_equiv](https://numpy.org/doc/stable/reference/generated/numpy.array_equiv.html)
* _hint_ your indicies  will be the same for both
## compare two matricies
Write  a function `compare()` Use your code from **`sum()`** instead of adding, compare the values between matricies, as soon as one pair is unequal return False. Otherwise if they are equal return True.
* _hint_ to test use the same array as both arguments
## optional functions
Other matrix operations, write code to do the following, then test your results using the numpy functions
* calculate the determinant of a 2x2 matrix [numpy.det](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html)
* transpose a 3x3 matrix [numpy.transpose](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)
* multiply two 2x2 matricies [numpy.matmul](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)
# Instructions  

  **In this exercise, you will practice writing functions, and then invoke them with your test data.**
 
  _Before you test your functions, choose 2 test cases, calculate the expected results and put your test cases & results in comments (before the functions)._ 

  Note: the easiest way to test your functions is to call them with literal data and print the result for example:
```python
# function
def square(x):
  return x*x
# test
print(f' 5 result {square(5)}')    # should be 25
print(f' 10 result {square(10)}')   # should be 100
# or if you prefer
sq = square(3)
print("square of 3 is" + str(sq))
```
<!-- note to self do this 2nd next time -->    
## Time for you to plan and code your functions!
1. Write a function that takes the number of doughnuts and returns the total cost of the doughnuts based on this information:    

Tim Hortons sells doughnuts in the following combinations
  * 1 for 1.29$
  * 12 for 11.99$ 
  * more than 12  for 1.05$ each
  * between 6-11 for 1.10$ each
2. Write a function `dice_game`  that simulates rolling 2 six sided dice (use random, between 1 & 6)  if the total of the dice is 7, 11, or doubles () return "win", otherwise return "lose"

1. A bakery sells pastries for 5.49$ if they are day old they are discounted by 60%. Write a function `day_old_pastries` that takes the quantity of day old pastries required as a parameter then returns a tuple: 
  * Total before discount, Total after discount

4. In Quebec we pay PST/QST and GST on most purchases write two functions `GST` & `PST` that take 1 parameter each, the amount of your purchase, and return the required tax.    values for GST & PST https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/
    * Note: in this case the acronym is ok as a function name as it is well known
    * if the amount of the purchase is negative, return 0
    * Example test `print(f'Purchase 15.43$ GST {GST(15.43):.2f}$ PST {PST(15.43):.2f}$')`
3. write a function `plus_tax()` that takes the amount of a purchase as a parameter, then returns a tuple of,  total to pay (purchase + taxes), gst and pst.  It will call your GST & PST functions to get the total tax.
3. `area_triangle` takes the base and height as parameters and returns the area (assume right angle triangle)
    * formula (base * height) / 2 
    * ex some test data &  call the function given base 10 height 15`area_triangle(10,15)` should result in `75` 
2. `area_triangle2` takes the three sides parameters and uses Herons formula to calculate and rerturns the area of the triangle.   (you will need the math library & https://www.mathsisfun.com/geometry/herons-formula.html )
3. `area_reg_polygon` takes the length of a side and the number of sides as parameters, and returns the area.  https://www.mathopenref.com/polygonregulararea.html 
4. `windchill_index` takes temperature in celsius and wind speed in kph as parameters, returns the windchill index.
    * calculator for test data https://weather.gc.ca/windchill/wind_chill_e.html 
    * formula: Wind chill = 13.12 + 0.6215T – 11.37 (V^0.16) + 0.3965T (V^0.16)
      * T = Temperature in degrees Celsius
      * V = Wind velocity in kilometers per hour
    * windchill is only valid for temperatures <= 10 return 0 if the temperature given is > 10
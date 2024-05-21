# Instructions  

  **In this exercise, you will be writing 3 different functions, and then invoking them with your test data.**
 
  _Before you test your functions, choose 2 test cases, calculate the expected results and put your test cases & results in comments (before the functions)._ 

## Time for you to plan and code your functions!

Below are three functions, code them one at a time then test them using your test data, if it's working do the next.

1. `hypotenuse_length()` 
  * takes the lengths of 2 sides of a right-angle triangle as parameters and returns the length of the hypotenuse
2. `perimeter()`
  * takes the lengths 2 sides of a right-angle triangle as parameters and returns the perimeter of the triangle. 
   * Challenge: `perimeter` will call the function `hypotenuse_length`  use the returned value in the perimeter calculation 
4. `tree_height()`
  * Someone is standing looking at a tree, calculate the height of the tree
  * give the distance to the tree and the angle between the ground and the top of the tree as parameters
  * hint: use the math library & tangent
  * return the height of the tree
  * from https://www.analyzemath.com/Trigonometry_problems/trigonometry_problems.html
3. `optimal_change()`
  * calculate the optimal amount of change to provide.  (fewest coins)
  * Your function takes **one parameter**, the total change in dollars and cents, example: $4.31 would be 431 cents (assume input is a non-negative floating point number). 
 It then determines what coins should be given in order to make that change. 
  * Figure out first how many toonies (200 cents), then loonies (100 cents), quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent—assume they still exist) should be given back in change.   
  * hint: do this " on paper for 431 cents"
   * Display these 6 values in an f-string, example:, `return f'Toonies: {toonie}, Loonies: {loonie}, Quarters: {quarter}, Dimes: {dime}, Nickels: {nickel}, Pennies: {penny}'`
   * Note: my tests will fail if you display a different f-string

## Final testing!
When your code is tested with your  own test cases, run my tests (on the right hand side, see Tools, Tests as below.  If they fail, figure out why and fix the code.
![run tests](tools-tests.png)
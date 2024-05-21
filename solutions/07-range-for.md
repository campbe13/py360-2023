# Instructions  

  **using for loops and the range function**

  _Write functions, then test them by calling them_

## Reference
* https://docs.python.org/3/tutorial/controlflow.html#the-range-function
* https://docs.python.org/3/library/functions.html#func-range
## exercises 
  For the below write a or function  (note do not use `input()` or `print()` inside a function unless specifically requested)
  
  1. Write a function that takes 2 numbers,  adds all the numbers between, and returns the sum
    * `sum_between(2, 4)` should return 9 (i.e., 2+3+4)
  2. Write a function that takes 2 numbers, and adds all the even numbers between, and returns the sum
     * `sum_even(2, 4)` should return 6 `(2+4)`
     * `sum_even(3, 8)` should return 18 `(4+6+8)`
  4. Write a function  `factorial` that takes a positive number, computes the factorial of that number, and returns it
     * `factorial(5)` should return 120   `1*2*3*4*5`
     * Note factorial computation starts at 1
     * do not use a recursive solution (do not call factorial() within factorial)
  3. Write a function `countdown()` that takes a positive number, then displays a countdown from that number to 0, then displays "Blastoff!!"
     * hint: use a  step that will decrease the number
     * countdown(2) should display
      ```
      2
      1
      0
      Blastoff!!
      ```
3. copy `countdown()` use it to write a function `countdownby` that takes a positive number to start the countdown and the interval to use then displays a countdown from that number to 0, then displays "Blastoff!!"
     
     *  countdownby(10,3) should display
      ```
      10
      7
      4
      1
      Blastoff!!
      ```
3. copy `countdownby` use it to write a function `nasa` that takes a positive number to start the countdown and the interval to use and a string `"up"`  or `"down"` then displays a count up or down from that number to 0, then displays "Blastoff!!"
     *  data validation: if the number is 0 or negative, return 
     *  if the string is not "up" or "down"  return
     *  if the string is `"up"` count up from 0 to the `start number`
     *  if the string is `"down"` count down to 0 as before
     *  nasa(10,3, "down") should display
      ```
      10
      7
      4
      1
      Blastoff!!
      ```
   *  nasa(10,3, "up") should display
      ```
      0
      3
      6
      9
      Blastoff!!
      ```
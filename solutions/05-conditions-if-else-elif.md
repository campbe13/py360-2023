# Instructions  

  **exercises using if/else**

_Before you test your functions, choose 1 test case, calculate the expected results and put your test cases & results in comments (before the functions)._ 

**there are a lot of exercises in here, be sure you can do & understand at least 1,2 and 3**

  ## Steps
  1. Write a function called `isVowel` that takes a letter as an argument,  returns `True` if it is any of `a,e,i,o,u` or `y` return `False` otherwise.  (they are mutually exclusive so use elif)
     *  to test use a separate function call each of the vowels and one other letter.
     *  use if/elif to solve this
  4. Write a function `vote_and_drink` in some places you cannot drink until you reach the age of 21, you can vote at 18.  The function takes age as a parameter and returns a tuple of values, (wether they can vote, whether they can drink). I gave you test data.

     * Ask the user for their age
     * use the function to and check age.
     * Display a message telling them the results 
     * ex tests
       * `can_vote,can_drink = vote_and_drink(21) #  both True`
       * `can_vote,can_drink = vote_and_drink(19) #  True, False`
       * `can_vote,can_drink = vote_and_drink(12) #  both False`
         
  
  2. Richter scale

The following table contains earthquake magnitude ranges on the Richter scale and their descriptors: 
 ![image](assets/image.png)
 Write a function  `richter` that takes the magnitude as a parameter and  returns the descriptor text, shown on the right.
 
Write a program that reads a magnitude from the user and displays the appropriate descriptor as part of a meaningful message. For example, if the user enters 5.5 then your program should indicate that a magnitude 5.5 earthquake is considered to be a moderate earthquake.   (use a format string)

  4. Write a function `pass_fail` that takes a grade as a parameter(floating point), returns True if the grade is 60% or over, False if not
  * Ask the user for their grade
  * call the function and use it to tell them if they passed or not

  5. Write a function called `calculate_tip` that takes a `tip_rate` and a `cost` as parameters. If the rate is greater than 1, divide it by 100 to get the percentage. Multiply the rate and the cost, and return the tip amount
     *  ask the user for the rate and value
     *  call your function with those values
     *  display the returned  tip value
  
 6. Write a function `animal_sounds` that returns a text sound depending on the paraeter given; `woof` if it is a dog, `meow` if it is a dog and `oink` if anything else.  (match only against `"dog"` and `"cat"` unless you want to add more)
     * Ask the user for their pet (ex dog or cat)
     * call the function
     * display the pet type and the sound  
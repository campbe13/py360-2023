# Instructions  

You will use the  random library to simulate 2 dice rolls! It's for a game that uses two dice. It will display the value that was "rolled" 

## first
  1. add the import statement for the random library
  2. Write a function `roll` that
     * takes no parameters
     * generates a random number, twice ; (note a 6 sided dice shows 1 - 6, not 0
     * displays the roll with appropriate text.
  

Call your function a few times. The "roll" should be different each time 

## second
Now, set the seed (before you generate a random number) and notice, what happens? 
ex `random.seed(876)`

## Test data
* none, it's random

## Optional
(comment out the seed if you tried it)

Modify your function `roll()` to take 1 parameter, the number of sides on the dice.
Use that when you generate your roll.
# Instructions  

**exercises using lists  & loops**

_Write code snippets or functions, then test them by calling them_

_Do_ *not* _use built-in functions_

## Reference
* https://docs.python.org/3/tutorial/datastructures.html
* https://developers.google.com/edu/python/lists 
* https://colab.research.google.com/github/computationalcore/introduction-to-python/blob/master/notebooks/3-fundamentals/PY0101EN-3-2-Loops.ipynb#scrollTo=5RKQt6Uh_wuj

## Steps
### Instructions  Use the grades list
1. Write a function `average` to take a list of grades as a parameter & return the average grade (do not include any grades that are <0 or > 100)
* you will need to also create a list with values <0 & >100 to test this
* How does this differ from using range() ?
### Instructions  Use the grades list
1. Write a function `highest` to take a list of grades as a parameter & return the largest grade (hint use a variable largest, start at 0 and hold the largest "so far" with each itteration of the loop
### Instructions  Use the cegeps list
1. Write a function to `cegeps` take a list of cegeps as a parameter it will display each element of the list with a text "you could go to " + the name of the cegep.
2. if the list item contains the string "Dawson"  (hint `x in y` for strings) add "the best" at the end of the string,  for example:
3. once you get it working, modify the code to check for any case (upper,lower, mixed) for dawson
```
you could go to JAC
you could go to Dawson the best
```
### Instructions  Roll the dice 
1. Write the snippet of code/function  to fill a list with 10 random numbers between 1 and 6  (if you want to use more sides to your dice that is fine)   <br>Hints: 
   * ` dicerolls = []   #empty list to start`  before the loop
   * use a for with a range ( 10 times )
   * inside the loop 
     * generate a random number
     * ` dicerolls.append(num)  #adds num to the end of the list `
   * use the list in the next steps
    
2. Do the following first without built in functions (`for` is not a function) optional use built in
   1. calculate the average & display it
   4. find the largest number in the list & display it
   5.  find the smallest number in the list & display it
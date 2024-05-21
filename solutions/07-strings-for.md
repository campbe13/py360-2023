# Instructions  

  **During lecture, exercises with strings**

  _Write code snippets or functions, then test them by calling them_

  ## Reference
*  https://docs.python.org/3/library/stdtypes.html#string-methods
*  https://colab.research.google.com/drive/1b49Dg_tIu-n-wGd5puIJmUDuwqTxc1gk?usp=sharing#scrollTo=WFrR7qtHYJkb
  
  **There are solutions and hints to do some of these in the slides, but try them yourself first.**
  
  ## Steps
  For the below write a  function   & test it

  1. 8 chars only `eight` :
     * parameter a word 
     * Write a function that does the following: 
     * If the word is more than 8 characters, return 'Too long'
     * If the word is less than 8 characters, return 'Too short'
     * If the word is 8 characters, return 'Perfect, thank you for the word starting with' and show the first letter
  1. x chars only `limitchars` :
     * copy the code from `eight`
     * add a parameter: size
     * Write a function that does the following: 
     * If the word is more than size characters, return 'Too long'
     * If the word is less than size characters, return 'Too short'
     * If the word is size  characters, return 'Perfect, thank you for the word starting with' plus the first letter 

  3. bad password function `checkpass` : 
     * parameters username and password
     * Write a function to: check if the username is a substring of the password, tell them they need a better password, if it is not, tell them it's ok
     * you decide what to return (string/ True-False etc)
  4. how many e's `counte` : 
     * parameter:  a sentence
     * Write a function that will count the number of 'e' in their sentence
     * return a tuple, of count & some text identifying it
  3. how many e's or E's `counteE`: 
     * modify the code from `counte`
     * two ways to do this, use a string  method or count both 
  3. function to reverse a word `reverse`: 
     * using the parameter, return a string containing the reversed value
  3. function to return every 2nd letter `second`: 
     * using the parameter, return a string with only every 2nd letter of the parameter
     * Note depending on how ou use an index you may get Index Out of Bounds, if so you will have to check at the end of your loop / after incrementing something like  
  ``` 
  if index >= len(string):
      return(newstring)
  ```
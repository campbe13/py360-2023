# Instructions  
  **some exercises using dicts etc**

  _write functions as indicstaed below  & test them_
## Reminders
* tuple `()` indexed, immutable, usually heterogeneous
* list `[]` indexed, mutable, usually homogeneous
* dict `{}` unordered, unique keys, key value pairs, key maps to value, mutable
* set `{}` unordered, unique values (no keys), not-indexed, (mutable if not a `frozenset`)
  
## dict functions
  
  1. Write a function `create_triples()` that creates a dict containing powers of 3, up to 10  return the dict.  ex `{0:0, 1:3, 2:9...  10:59049}`  hint use for
  Challenge:  instead of 10 use a parameter as the maximum
  2. Write a function `count_letters()` that takes a string as a parameter count the vowels (aeiou,y) in the string and return a dict with those counts. ex `{a:2,i:0...}`.
  3. Write a function `begin_end()` that takes a string and a letter as parameters. It checks if the letter is at the beginning or end of the letter, then constructs a dict to return.
     ex: `begin_end('python is great', 'p')` would return `{'begin':True ,'end':False.}` 
6. write a function `make_dict()` that takes as a parameter a list and returns a dict.  The list can have any length and any values but assume they are unique and the same type. It will use the list values as keys in a  dict, and set the value to zero. 
 ex `['apples', cherries']` converted to `{'apples':0, 'cherries':0}` 
7. create a list of grocery 4 items,  use `make_dict()` to create a dictionary  from that list
Create a function `prices()` that takes a dict created by `make_dict()` as a parameter.  In the function prompt the user for the price of each of the _key_ items, update the dict.  Print the dict before and after you call `prices()` to see the results
  Note: prices will not be a single purpose function (we don't usually use input inside a function)
## Set function  
Write a function that takes a list as a parameter & converts it into a set, Do not use 
## Optional, long
Write a function `morse()` That takes a string parameter and returns the morse code for that string. 
Morse code is an encoding scheme that uses dashes and dots to represent numbers and letters.  Create a dict from [here](https://morsedecoder.com/) (scroll down, only alphabet if you want) the key is the letter, the value is the series. For key `a` the value would be `._` ( dot dash )

  _hint_ if you create your dict with uppercase keys convert the string to upper  before converting & vice versa )
Ex morse('hello') would return `.... . .-.. .-.. ---`
You can use this decoder https://morsedecoder.com/  to test your results morse<>alphabet

Teacher's solution to #5 & 6 https://replit.com/@pcampbell/BigheartedPassionateDebugger (I did not choose the name)
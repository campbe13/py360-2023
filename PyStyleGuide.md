# Style Guidelines for Python
Note that when you write code you should think about making your code readable for you or anyone else who has to change it.  Use white space and the following guidlines.  This  is an important aspect of coding.
## For variable names and function names 
### Rules you must follow or else there will be a syntax error 
* name must start with a letter (or underscore _do not use underscore this way, it is special purpose_)
* can contain letters, digits , and underscores
* function and variable names are case sensitive  (so `Add_tax` and `add_tax` and `Add_Tax` ... would be considered different functions (do not do this on purpose, it would be confusing))
* cannot be a **reserved** keyword
    * certain words already have a meaning in Python
    * if you tried to use the word as a variable or function name, Python would be confused about what you wanted to do
    * for example try naming a variable "if" or "while" or "print"  you will create errors 
### Rules most Python programmers follow, including you!
[Python.org PEP8 Conventions](https://www.python.org/dev/peps/pep-0008/)
* PEP8 is the Style Guide for Python Code
* variables start with a lowercase letter 
* if a variable name is many words, use an underscore to separate
### Example
```python
# good names
area_right_triangle()
length
height
# bad names
a()
area()
l
h
```
## For functions
    
* All functions must have a docstring comment that explains what they do, what they take as parameters,  and what they return
* Functions should be responsible for one thing only! (single responsibility)
    * Don't write a function that asks for user input, calculates and prints to screen
    * instead 
      1. ask for user input
      2. call a function with the argument(s)
      3. display the return value of the function
    * Why? The function is not tied to the user interface -> can be reused
* Be careful of indentation! Use the repl.it default - it will add indents if the previous line ends with a colon `:` (if you are using another editor for each indentation use 4 spaces)
* Add empty/blank lines (whitespace) before and after function definitions. Also add blank lines to indicate logical sections.

### Example
```python
''' 
add_five: This function adds 5 to the parameter and returns that value
parameter: a  number
returns: the given number plus 5
test data:
5 results in 10
100 results in 105
1.1 results in 5.1
'''
def add_five(num):
    return (num +5)
    
num = int(input('Enter a number'))

print(add_five(num))
```

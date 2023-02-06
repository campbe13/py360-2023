# IDE 
## how do I make a block of code into comments, so it will not run 

1. select the lines you want to comment
2. `ctrl + /`

## how do I clear the console ?
* `ctrl + l`  the letter L, lower case

# Python
## think about data types
You can't have a fraction of an egg so int is appropriate
```
eggs  = input("number of eggs")
eggs = int(eggs) # can't have a fraction of an egg
```
You can have a fraction of a dollar so float is appropriate
```
cost_lumber  = input('what is the cost of lumber')
cost_lumber = float(cost) 
```

## be careful about unnecessary operations
```
meal=input("what is the cost of the meal?")
meal=float(meal)
tip = float(meal * 0.18) 
```
The `float(meal * 0.18)` is not necessary because meal and 0.18 are both floating point numbers already, it works but there is an unneccessary function call & the coder not noting the data type.   You only need `tip = meal * 0.18`  

## printing only 2 decimal places
### round() function 
[docs.python.org round()](https://docs.python.org/3.8/library/functions.html#round)

The problem with rounding is that you lose precision, do it after all calculations.  The 2nd argument is precision, if omitted, it returns an integer.
```
my_pi =   3.1415926535
print(my_pi, 'no rounding' )
my_pi2 = round(my_pi,2)
print(my_pi2, 'with 2 decimal points')
my_pi6 = round(my_pi,6)
print(my_pi6, 'with 6 decimal points')
```
### format string
[docs.python.org format strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

These are special strings that can be used to display variables within a string, with a format specifier if you want.
```
my_pi =  3.1415926535
print(f'This is PI ${my_pi} without a format specifier' )
print(f'This is PI ${my_pi:.2f} with 2 decimal points')
print(f"This is PI ${my_pi:.3f} with 3 decimal points")
```

## how can I get input in the middle of an input string?
_Note this is a cludge and won't always work._
You need to write your string before the input position then add a carriage return `\r`  this places the cursor on the same line and writes over your text again to reposition the cursor.

Example `x = input("give me    some data \rgive me")`
What happens is
1. displays `"give me   some data"`
2. moves the cursor back to the beginning of the same line
3. writes the text after the \r `"give me"` and leaves the cursor there, _in between_
4. so it looks like you have text after your input field but you can write over the text

We spoke of `\n` in reality it signals a carriage return + new line

This is sort of a hack, not very clean but it works
```
sales_tax = input("What is the sales tax in your area?    % \r What is the sales tax in your area? ")
print(sales_tax)
```

# Instructions  

You may not complete this during the lab time, you can come back to it  & complete it before next class.

Use the slides (on moodle) for code exmples 

1. create an algorithm: think about the problem, create a flowchart or write in point form the steps you will use 
1. use iterative development ___(code a bit, test it, do the next bit...)___
1. use comments for code you want to keep but not remove (ex for debugging)
1. use print statements to see what is in your variables, if you are not sure (ex for debugging)
5. if you do not finish today you can logoff and come back to complete it
1. when you have finished all three you can `submit`   you do not need to submit, do so if you want to see my solution or feedback from me.  (let me know if you want feedback)

__Write your code in main.py modify & run that directly__

#  Calculators
## reminder in python we use the following [arithmetic operators](https://greenteapress.com/thinkpython2/html/thinkpython2002.html#sec9)
* add  `+`
* subtract `-`
* divide `/`
* multiply `*`
* exponent `**`
  
## reminder input() always returns a string so to do arithmetic we must convert
```
age  = input("how old is your dog?")
dogyrs = age * 7    # error!!!
age = int(age)      # convert string to int  (no decimal point)
dogyrs = age * 7    # ok!!!
cost = input('how much is your dog food')
cost = float(cost)  # convert sting to float (has decimal pont) 
print("wow", cost, "is a lot")
```

## we will do a summing caluclator together
First identify your code & yourself at the top of `main.py`

Write the code that asks the user to enter 2 numbers The program calculates and displays the sum of the two numbers. 

1. write down test data   (2 sets)
2. calculate results  
3. run your code with with that data  if it matches you are done!

write your code below the print statement


## Perimeter Calculator  (& Area)

Write the code that asks the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle.   After you display the 

1. write down test data   (2 sets)
2. calculate results  
3. run your code a few times with that data

write your code below the print statement

# Restaurant Tip Calculator 
Write the code that asks the user to enter the price of a meal at a restaurant 
The program calculates the amount of the tip to be paid at 18%. The tip and total price are then displayed separately.

1. write down test data   (2 sets)
2. calculate results  
3. run your code with with that data  if it matches you are done, or do the challenge

## challenge
When it is working and tested for 18% modify it to ask the user to enter the percentage instead of always using 18% 


# Volume and Surface Area Calculator

Write the code that asks the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 

Here is where you could look up the forumula for the surface area of a cuboid, but it's `2lw + 2hl + 2hw = surface`

1. write down test data   (2 sets)
2. calculate results  
3. run your code with with that data  if it matches you are done!
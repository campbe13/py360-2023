# Functions
## Some gotchas
Functions are isolated blocks of code designed to be single use
### they must be defined before they are used
```
#  Error, the interpreter has not "seen" convert_celsuis when it looks at this line of code
print(convert_celsius(10)) 

def convert_celsius(fahr): 
    celsius = (fahr-32) *5/9
    return celsius
```
### variables inside a function are not available outside
```
#  Error, the interpreter doesn't know what convert_celsuis when it looks at this line of code​
print(convert_celsius(10)) 

def convert_celsius(fahr): 
    celsius = (fahr-32) *5/9
    return celsius
# Error, the variable celsius is not available outside the function​  
# this is called variable scope
print(celsius)

# this will work!!
print(convert_celsius(10))

# this will work!
# this is a new celsius, 
# not the same as the one in convert_celsius
celsius = convert_celsius(-5.8)
print(f' -5.8\u00B0F is {celsius}\u00B0C ')
```

### parameter values are copies of the argument (cannot change them for the calling program)
```
def func(a,b,c):
  c = abs(c)
  return a**2 + b - c
  
x = 5
y = 8
z = -10
q = func(x,y,z)
# what is the value of z ?
```
### any statement after a return is NEVER executed, if it's part of the code block
```
def func(a,b,c):
  result = a**2 + b - c
  return result
  print ("testing")   # <<<< never reached!
  print (result)    # <<<<< never reached!
  
print(10,4,5 "func ", func(10,4,5))
# what is displayed?
```
versus
```
def func(a,b,c):
  result = a**2 + b - c
  return result
print ("testing")  
 
print(10,4,5 "func ", func(10,4,5))
# what is displayed?
```

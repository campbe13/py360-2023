# Setting up  programs in python
## correct structure 
```
# description
# name
# date

# import statments

# functions
'''
function description (1 each)
'''
def myfunc():
    pass   

# main() function
def main():
    pass      # code to run the programm & use the functions
    
if __name__ == '__main__':
    main()
```
## why use `__name__`
Python modules allow us to use other code in our programs. When a Python module or package is imported, `__name__` is set to the module’s name. 
Usually, this is the name of the Python file itself without the .py extension.  

__main__ is the name of the environment where top-level code is run. 
*Top-level code* is the first user-specified Python module that starts running. 
It is “top-level” because it will be used to import all other modules that the program needs. 
Sometimes “top-level code” is called an *entry point* to the application.

Ref https://docs.python.org/3/library/__main__.html

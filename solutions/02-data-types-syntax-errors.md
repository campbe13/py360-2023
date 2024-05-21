# Instructions  

The code in main.py has  a lot of errors in it.

I want you to run the code & fix the errors. Also when a print statement prints a value without explanation add an explanation.
Just try things!

    Before you run it, try to decide what the outcome will be.  Then run the code to check your expectations (the whole script or bits in the console). If the results do not match what you expect think about why that is.
  
## hints
* you will have to fix some  syntax to make them run properly
* try statements on the rhs in the console before or while changing the script in main.py
* remember operator precedence, check the slides in moodle (PEMDAS)
* python interpreter likes everything aligned (no murky indents)

## optional unicode characters
This is extra (& ) for those who were asking about using superscript)
To print non standard characters you can escape  the unicode value 

The \ escapes & the u indicates unicode followed by the character code
`print("unicode spiral \u058D")  `

### numbers superscript ex
* `print("x\u00b2")   # x to the power of 2`
* `print("y\u2079")   # y to the power of 9`
 ``` 
 x = 10
 print(str(x) + "\u2075 is " + x**5)
 ```
### numbers subscripts ex 
* `print("x\u2082 + x\u2083")   # x sub 2 + x sub 3`

### challenge look up some characters and display them also
ex unicode for PI is U+03C0  `print("\u03c0")`
You may want to try a few from this [unicode super/subscripts letters](https://unicode-table.com/en/sets/superscript-and-subscript-letters/)  or just google unicode for ... 
# Instructions   Caesar cypher with digits

The [Caesar cypher](https://en.wikipedia.org/wiki/Caesar_cypher) is one of the most basic encryption techniques. It is a substituition cypher, where each character is replaced by another one. It is usually used to encrypt text messages, but in this exercise, you are going to encrypt numbers using only the arithmetic operators __(no conversion to strings allowed in the cypher!)__

## Caesar cypher and numbers

Here is how we will encrypt numbers using Caesar cypher. Let's say my number is 123, 
and the shift value is 3. This means I will add 3 to each digit, and the encrypted 
number is 456.

Let's take another example. Let's say my number is 680 and the shift value if 4. I need 
to add 4 to each digit, and I need to restart back at 0 when the addition is 10 or more 
(remember modulo arithmetic?). So the encrypted number is 024. __Notice that it is not 
the same as adding 444 to the original number!__

_Implement the code for postive numbers & shift first, then if you wish add code for negative, see the optional challenge below_

### Optional challenges
Negative shift: the number is 518 and the shift value is -2: we will subtract 2 from 
each digit, again with modulo arithmetic. So the encrypted number is 396

Negative nubmer: the number is -518 and the shift is -2. We will always find 
the encrypted number using the absolute value of the number, then returning the sign. 
So the answer will be -396. Hint: the function `abs(x)` returns `|x|`. To return the 
sign, check if |x| is the same as x.

Note:  to decrypt you would have to subtract the same shift value.

## Your application
Write an application that asks the user for a whole number with 4-digits, and a shift. Assume that your user is a good user and they listen to you (they will only ever enter 4 digits  &  1 digit shift!) Display the encrypted number as the result.

You should be able to do everything using integers, `//`, `%`, `+`, and `*`. No strings 
or new constructs allowed!

## Analyse how you will perform your computations FIRST
Write pseudo-code or draw a flowchart. Decide on the formulae you will use to split up the digits & to add the shift.
Try the problem on paper to see what you would 
do if you were doing it manually: (ex input 1234  shift 2)  this will make sure you 
understand the problem:

1. break up the number `1 x 1000 + 2 x 100 + 3 x 10 + 4    `
1. add 2 to each of the digits    `1+2` & `2+2` & `3+2` & `4+2`
1. results in  `3456`

Now try one on paper where there will be overflow (ex 7400 shift 5)

___Hint you need to break up the number, you can use division & modulus to do this, best  to use variables (4) one to save each digit___
## Documenting your test cases
At the top of the file, before even coding, write your test cases between the triple 
quotation mark comment `''' '''`. Each test case should show the original number, the 
shift value and the expected output. When you run your application, you will run your 
test cases to make sure it works correctly.

## Coding your application  Last
Ask the user for the number to encrypt first, then the shift value. Perform the calculations. Display the encrypted number.

## Running test cases
Once you successfully run your test cases (meaning you have typed them in and seen the
correct/ expected results), it is time to run my test cases!! Click on the check-mark 
on the bottom left, then the `Run tests` button. See if they all pass!
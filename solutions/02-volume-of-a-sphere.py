# ask for diameter of a sphere
# display the volume of the sphere

# author: everybody in the class
# 2022-01-31 

# test data 
# diameter 6.65
# expected result: 153.97973
# diameter 7.25
# expected result: ~199.53

diameter = float(input("enter the diameter of your sphere: "))
# precedence ok! 
volume = 4/3 * 3.14159 * (diameter/2)**3

print(f'a sphere of diameter {diameter} is {volume:.3f}' )


'''
# for debugging
print(diameter)
print(diameter/2)
print(volume)
'''

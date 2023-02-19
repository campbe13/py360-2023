'''
Q2 check digit
'''
# 1234 check dig 0
# 2185 check dig 8

num = int(input("enter a 4 digit number: "))

dig1 = num//1000
dig2 = num//100%10
dig3 = num//10%10
dig4 = num%10
check = (dig1*1  + dig2*2 + dig3*3 + dig4*4)%10
print(f'{num}{check}')

'''
Q2 check digit
'''

num = int(input("enter a 4 digit number: "))

dig1 = num//1000
dig2 = num//100%10
dig3 = num//10%10
dig4 = num%10
check = (dig1 * dig2 + dig3 * dig4)%10
print(f'{num}{check}')
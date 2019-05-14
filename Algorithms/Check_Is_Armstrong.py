'''
author: Paul Larkin
date: 14/05/2019
details: Python program that checks
if a number is an Armstrong Number
'''

#Armstrong checker
def check_armstrong(number):
    original_num = number
    total = 0
    while number>0:
        current = number%10
        total += (current*current*current)
        number = int(number/10)
    
    return (total == original_num)

#Main Body
number = int(input("Enter a number"))
if(check_armstrong(number)):
    print(number,"is an Armstrong Number")
else:
    print(number,"is NOT an Armstrong Number")
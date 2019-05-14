'''
author: Paul Larkin
date: 14/05/2019
details: Python program that counts
the number of sequences in a numbers
Collatz Conjecture
'''

#Collatz function
def check_collatz_count(number):
    counter = 0
    while number>1:
        if number%2 == 0:
            number = int(number/2)
        else:
            number *=3
            number +=1
        counter +=1

    return counter

#Main Body
number = int(input("Enter a Number"))
print(check_collatz_count(number))
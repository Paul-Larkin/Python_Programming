'''
author: Paul Larkin
date: 15/05/2019
description: FizzBuzz
'''

#Main Body
for x in range (1, 101):
    if x%3==0 and x%5==0:
        print(x,"Fizz Buzz")
    elif x%3==0:
        print(x,"Fizz")
    elif x%5==0:
        print(x,"Buzz")
    else:
        print(x)
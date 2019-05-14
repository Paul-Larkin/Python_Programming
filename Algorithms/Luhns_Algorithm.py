'''
author: Paul Larkin
date: 14/05/2019
details: Python program that performs Luhn's Algorithm
'''

#Function takes in a str number, reverses it, performs
#Luhn's Algorithm and returns boolean result
def check_is_valid(card):
  reverse_card = ""
  for x in range (len(card)-1, -1, -1):
    reverse_card = reverse_card + card[x]
  current_number = 0
  sum_num = 0
  for x in range (0,len(reverse_card)):
    current_number = int(reverse_card[x])
    if x%2!=0:
      current_number *= 2
      if current_number > 9:
        current_number -= 9
    sum_num += current_number
    
  return (sum_num%10==0)

#Main body
card_number = input("Enter a Credit Card Number")
if(check_is_valid(card_number)):
  print(card_number+" is a VALID number")
else:
  print(card_number+" is an INVALID number")
import os
import time
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()


numbers = [1, 3, 5]

print(5 in numbers)
print(8 in numbers)

print(5 not in numbers)
print(8 not in numbers)

print('\nFim do EX: 1')
os.system("pause")
clearConsole()

##############################################################3

cities = ["Chicago", "London", "Tokyo"]

for city in cities:
  print(city)


print('\nFim do EX: 2')
os.system("pause")
clearConsole()

##############################################################
numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
numbers.sort()

for number in numbers:
  if number > 42:
    break
  print(number)

print('\nFim do EX: 3')
os.system("pause")
clearConsole()

##############################################################


import random
numbers = []

while len(numbers) < 5:
  numbers.append(random.randint(1, 100))

for number in numbers:
  print(number)
  if number >= 90:
    print('Found at least one number greater than 90')
    break
else:
  print('No numbers greater than 90')

print('Complete')

print('\nFim do EX: 4')
os.system("pause")
clearConsole()

##############################################################



suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

for  suit in suits:
  for rank in ranks:
    print(f'{rank} of {suit}') 
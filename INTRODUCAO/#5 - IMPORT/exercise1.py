import os
import time
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

#------------------------------------------------------------------------------1
dado = 1
while dado < 7:
    dado = random.randint(1, 20)
    print('seu dado caiu em ' + dado)
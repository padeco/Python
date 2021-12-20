import os
import time


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

#------------------------------------------------------------------------------1
fahrenheit = 'saida'

while fahrenheit.isnumeric() == False:
    fahrenheit = input('Qual a temperatura em fahrenheit quer transformar em celsius? \n')

    if fahrenheit.isnumeric() == False:
        print('Erro! favor inserir um Numero!\n')
        os.system("pause")
        

celsius = (float(fahrenheit) - 32) * 5/9
print(round(celsius,1),'ºC')

print('\nFim do Desafio')
os.system("pause")
clearConsole()
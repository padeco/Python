import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'
  

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'
 # First challenge
print('\t' + first_value.title())
 # Second challenge
mess = second_value.strip()
message = mess.replace('-','')
print(message.capitalize())
  # Third challenge
message1 = third_value.replace(' ','')
message2 = message1.replace('-',' ')
print('\t\t' + message2.swapcase())

    # Fourth challenge - use only the print() function (no f-strings)
'''instrucao='{}#{}#{}!'.format(fourth_value,fifth_value,sixth_value)
print(instrucao)'''
print(f'{fourth_value}#{fifth_value}#{sixth_value}!')
print(f'\t{fourth_value}')
 # Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'\t{fifth_value}')


print(f'\t{sixth_value}')

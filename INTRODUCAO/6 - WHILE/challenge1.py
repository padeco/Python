import os
import time
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()


numero = 0
contador = 0
chute = 1

print('Primeira pessoa a acertar o numero ganha!')

while chute != numero:
  contador += 1
  numero = random.randint(1, 5)
  chute = input('insira o numero que caira no dado:  ' )
  if chute.isnumeric():
        chute = int(chute)
  
  print(f'chutou {chute} e caiu {numero}')
else:
    print(f'Vitoria voce chutou {numero} e gahou!!!')

print(f'Voce jogou o dado {contador} vezes.')
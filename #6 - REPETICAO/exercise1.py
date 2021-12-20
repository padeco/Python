import os
import time
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()


roll = 0
count = 0

print('First person to roll a 5 wins!')
while roll != 5:
  
  name = input('Enter a name, or \'q\' to quit:  ' )

  if name.strip() == '':
        continue        #VOLTA PARA O COMECO DO WHILE

  if name == 'q':
        break           #QUEBRA O LAÇO DE REPETICAO
  
  count = count + 1
  roll = random.randint(1, 5)
  print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins!!!')

print(f'You rolled the dice {count} times.')


print('\nFim do EX: 1')
os.system("pause")
clearConsole()


#------------------------------------------------------------------------------2

count = 0
while count <= 20:
    count += 3
    print(count)

'''
=	Atribuir
+=	Adicionar e, em seguida, atribuir
-=	Subtrair e, em seguida, atribuir
*=	Multiplicar e, em seguida, atribuir
/=	Dividir e, em seguida, atribuir
%=	Obter o módulo e, em seguida, atribuir
**=	Executar o expoente e, em seguida, atribuir
//=	Executar a divisão de base e, em seguida, atribuir'''
import os
import time
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

numero = random.randint(1, 10)
contador = 0
chute = 0
print('chute um numero de 1 a 10')

while chute != numero:
    contador += 1
    chute = input(f'Enter chute #{contador}: ')

    if chute.isnumeric():
        chute = int(chute)
    else:
        print('Apenas numeros, por favor')
        continue

    if chute > numero:
        print('Seu chute foi alto, tente novamente!')
    elif chute < numero:
        print('Seu chute foi baixo, tente novamente!')

else:
    print(f'Voce precisou de {contador} tentativas!')


'''Nossa meta era criar uma estrutura de looping em Python para iterar usando um bloco de código pelo período que uma condição fosse atendida.

Usando a instrução while, implementamos um loop que continuou executando um bloco de código enquanto uma expressão booliana era avaliada como True. 
Usamos a instrução else para executar um bloco de código após a expressão booliana ser avaliada como False. 
Também adicionamos a instrução break para sair completamente do bloco de código. 
Adicionamos uma instrução continue para modificar e definir o caminho de execução de volta para a avaliação da expressão booliana da instrução while. 
Também usamos novos operadores de atribuição para adicionar incrementos e decrementos simples aos nossos programas.'''
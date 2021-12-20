import os
import time



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()


print('''_________        .__               .__              .___                   
\_   ___ \_____  |  |   ____  __ __|  | _____     __| _/________________   
/    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \   / __ |/  _ \_  __ \__  \  
\     \____/ __ \|  |_\  \___|  |  /  |__/ __ \_/ /_/ (  <_> )  | \// __ \_
 \______  (____  /____/\___  >____/|____(____  /\____ |\____/|__|  (____  /
        \/     \/          \/                \/      \/                 \/ ''')

os.system("pause")
clearConsole()

#-----------funcao do primeiro valor -----------
primeiro_valor = 'saida'

while primeiro_valor.isnumeric() == False:
    primeiro_valor = input('Insira o primeiro valor: \n')

    clearConsole()
    if primeiro_valor.isnumeric() == False:
        print('Erro!!! Favor inserir um numero!')
        time.sleep(2)
        clearConsole()



#----------- funcao do operador ------------
operador_valor = 'saida'
while operador_valor.isalnum() == True:
    print('Primeiro valor é: ' + str(primeiro_valor))
    print('''Operadores:
    +: operador de adição
    -: operador de subtração
    *: operador de multiplicação
    /: operador de divisão
    %: operador de módulo
    **: operador de expoente\n
    ''')
    operador_valor = input('Insira o Operador desejado:\n')

    if operador_valor.isalnum() == True :
        print('Erro!!! Favor inserir um operador!')
        time.sleep(2)
        clearConsole()

clearConsole()

#-----------funcao do segundo valor -----------
segundo_valor = 'saida'

while segundo_valor.isnumeric() == False:
    print(str(primeiro_valor)+ ' ' + operador_valor)
    segundo_valor = input('Insira o segundo valor: \n')

    if segundo_valor.isnumeric() == False:
        print('Erro!!! Favor inserir um numero!')
        time.sleep(2)
        clearConsole()

primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

if operador_valor == '+':
    resultado = primeiro_valor + segundo_valor
    operacao = 'Soma'
elif operador_valor == '-':
    resultado = primeiro_valor - segundo_valor
    operacao = 'Subtração'
elif operador_valor == '*':
    resultado = primeiro_valor * segundo_valor
    operacao = 'Multiplicação'
elif operador_valor == '/':
    resultado = primeiro_valor / segundo_valor
    operacao = 'Divisão'
elif operador_valor == '%':
    resultado = primeiro_valor % segundo_valor
    operacao = 'Modulação'
else:
    resultado = primeiro_valor ** segundo_valor
    operacao = 'Exponenciacção'


print(operacao + ' de ' + str(primeiro_valor) + ' ' + operador_valor + ' ' +  str(segundo_valor) + ' = ' + str(resultado))
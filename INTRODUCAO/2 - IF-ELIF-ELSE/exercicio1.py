import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

########################### EX:1

valor = '6'

if valor == '7':
    print('Este Valor é 7')


print('Fim do EX: 1')
os.system("pause")

clearConsole()

########################### EX:2

valor = '8'

if valor == '7':
    print('Este Valor é 7')
else:
    print('Este não Valor é 7')

print('Fim do EX: 2')
os.system("pause")
clearConsole()


########################### EX:3

valor = '8' #Podemos usar quantos ELIF quanto for necessario, todo o código recuado abaixo da elif é parte do bloco de código que é executado se a expressão booliana é avaliada como True.

if valor == '7':
    print('Este Valor é 7')
elif valor == '8':
    print('Este valor é 8')
elif valor == '9':
    print('Este valor é 9')
else:
    print('Esse Valor não é o que procuramos')

print('Fim do EX: 3')
os.system("pause")
clearConsole()

########################### EX:4

valor = '6'

if valor < '8': # sim é menor 
    print('Este Valor é menor que 8')
elif valor < '7': #sim tambem é menor porem nao sera executada pois ao comparar com (if valor < '8':) deu true e o programa inicia o boleano TRUE 
    print('Este valor é menor que é 7')
else:
    print('Esse Valor não é o que procuramos')

print('Fim do EX: 4')
os.system("pause")
clearConsole()

########################### EX:5

primeiro_valor = True
segundo_valor = '6'

if primeiro_valor: # Toda booliana TRUE nao precisa o argumento ou seja nao precisa escrever dessa forma (if first_value == True:)
    if segundo_valor == '6':
        print('Estou aqui')

print('Fim do EX: 5')
os.system("pause")
clearConsole()

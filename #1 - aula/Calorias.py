import time
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole() # use esse comando toda vez que quiser limpar o console

print('Programa para controle de ingestao de calorias!')
time.sleep(3)

clearConsole()

print('Informe o dia?')
data = input()
print('Informe quantas calorias ingeriu em cada refeição!!')
time.sleep(2)


print('Café da manhã?')
cafe = int(input())
time.sleep(.5)
clearConsole()

print('Almoço?')
almoco = int(input())
time.sleep(.5)
clearConsole()

print('jantar?')
jantar = int(input())
time.sleep(.5)
clearConsole()

print('Lanche?')
lanche = int(input())
time.sleep(.5)
clearConsole()

result = (cafe + almoco + jantar + lanche)

print('Seu total de calorias no dia ' + data + 'é: ' + str(result))
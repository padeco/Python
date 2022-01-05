import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

#-------------------------------------------------------------------------------------#
resp_invalida = True
def retorno():



    print('Deseja sair do programa? S/N')

    resposta = input()           

    if resposta == 's' or resposta =='sim':
        print('Saindo pro programa')
        resp_invalida = False
        time.sleep(3)
        exit()
    elif resposta == 'n' or resposta == 'nao':
        print('Em que ponto do programa deseja retornar?')
        print('1 - Inicio')
        print('2 - Abas')
        clearConsole()
        resp_invalida = False        
    else:
        print('Desculpe, Resposta invalida!')
        clearConsole()


    print('Responda corretamente!')
    time.sleep(3)
    clearConsole()


while resp_invalida:

    retorno()

print('Fim do EX: 1')
os.system("pause")

clearConsole()
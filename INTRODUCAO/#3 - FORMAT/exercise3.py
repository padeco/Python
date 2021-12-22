import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



#---------------------------------------------------------------------1
    #{} .FORMAT CHAMA O VALOR DE UM VARIAVEL PARA DENTRO DE OUTRA VARIAVEL, CASO NAO SEJA DEFINIDA A SEQUENCIA {0},{1}...
    # SERA SUBSTITUIDO DA DIREITA PARA ESQUEDA
    # LEMBRANDO QUE AS VARIAVEIS PODE SER DEFINIDA DETRO DO .FORMAT()
def ex1():
    medicine = 'Coughussin'
    dosage = 5
    duration = 4.5

    instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
    print(instructions)

    instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
    print(instructions)

    instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)

    print(instructions)

    print('Fim do EX: 2')
    os.system("pause")
    clearConsole()

#------------------------------------------------------------------------------2
def ex2():
    #OUTRA FORMA E CHAMAR A FUNCAO FORMAT {}
    name = 'World'
    message = f'Hello, {name}.'
    print(message)

    count = 10
    value = 3.14
    message = f'Count to {count}.  Multiply by {value}.'
    print(message)

    print('Fim do EX: 3')
    os.system("pause")
    clearConsole()

#------------------------------------------------------------------------------3
def ex3():
    #F{} PERMITE FAZER CALCULOS DENTRO DA VARIAVEL
    width = 5
    height = 10

    print(f'The perimeter is {(2 * width) + (2 * height)} and the area is {width * height}.')

    print('Fim do EX: 3')
    os.system("pause")
    clearConsole()

#------------------------------------------------------------------------------4
def ex4():
    #f{} INSERE CARACTERES DEFINIDOS NOS PARAMETROS DE EXEMPLOS A BAIXO
    value = 'hi'

    print(f'.{value:<25}.') #DIREITA
    print(f'.{value:>25}.') #ESQUERDA
    print(f'.{value:^25}.') #METADE CADA LADO
    print(f'.{value:-^25}.') #PODEMOS DEFINIR QUAL TIPO DE CARACTERE SERA INSERIDO

    print('Fim do EX: 4')
    os.system("pause")
    clearConsole()
import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

#------------------------------------------------------------------------------1
# FUNCAO TYPE COMO JA FOI USADA ANTERIORMENTE MOSTRA QUAL O TIPO DA VARIAVEL

print(type('7'))    #STRING
print(type(7))      #INT
print(type(7.1))    #FLOAT


print('\nFim do EX: 1')
os.system("pause")
clearConsole()


#------------------------------------------------------------------------------2
# A FUNCAO ISINSTANCE() MOSTRA QUAL O TIPO DE VARIAVEL É ESPERADO, SE A VARIALVEL RETORNAR O ESPERADO RETORNA TRUE, CASO CONTRARIO FALSE

print(isinstance('7', str))         #TRUE
print(isinstance(7, int))           #TRUE
print(isinstance(7.1, float))       #TRUE

print(isinstance(7, str))           #FALSE
print(isinstance('7', int))         #FALSE
print(isinstance('7.1', float))     #FALSE

# A FUNCAO TYPE TAMBEM PODE SER USADO PARA RETORNAR UM BOOLIANO, POREM NAO É ACONSELHAVEL, ENTAO PARA VER SE UM RESULTADO É BOOLIANO USE ISINSTANCE()

print(type('7') == str)
print(type(7) == int)
print(type(7.1) == float)

print(type(7) == str)
print(type('7') == int)
print(type('7.1') == float)

print('\nFim do EX: 2')
os.system("pause")
clearConsole()


#------------------------------------------------------------------------------3
#FORMA ERRADA DE RECEBER DADOS DO USURARIO OU DE OUTROS PRGRAMAS, JA QUE VOCE ESTA USANDO SOMENTE O IMPUT E ESPECIFICANDO QUE A ENTRADA SEJA INTEIRA, E SE NAO FOR?
#POR ISSO DEVERA SER USADO A FUNCAO ISNUMERIC()

first_value = int(input('First Number: '))
second_value = int(input('Second number: '))
sum = first_value + second_value
print("Sum: " + str(sum))
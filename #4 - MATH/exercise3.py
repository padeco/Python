import os
import time


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

#------------------------------------------------------------------------------1
'''Muitos dos operadores são intuitivos, mas se você não tiver certeza, eles estarão listados aqui:

+: operador de adição
-: operador de subtração
*: operador de multiplicação
/: operador de divisão
%: operador de módulo, que fornece o resto (se houver) após a divisão de um valor por outro. É útil saber se um valor é divisível de maneira uniforme pelo outro.
**: operador de expoente. Por exemplo, "5 elevado à quarta potência" é expresso como 5 * 5 * 5 * 5.'''

first_value = 5
second_value = 4

sum = first_value + second_value
difference = first_value - second_value
product = first_value * second_value
quotient = first_value / second_value
modulus = first_value % second_value
exponent = first_value ** second_value 

print('Sum: ' + str(sum))
print('Difference: ' + str(difference))
print('Product: ' + str(product))
print('Quotient: ' + str(quotient))
print('Modulus: ' + str(modulus))
print('Exponent: ' + str(exponent))

print('\nFim do EX: 1')
os.system("pause")
clearConsole()


#------------------------------------------------------------------------------2

print(3 + 4 * 5)
print((3 + 4) * 5)
#------------------------------------
first_value = 5
second_value = 4

quotient = first_value / second_value

print(type(quotient))
print(quotient)
#------------------------------------
pi = 3.14
print(type(pi))
print(int(pi))

uptime = 99.99
print(type(uptime))
print(int(uptime))
#------------------------------------ FUNCAO ROUND() SERVE COMO UM ARREDONDAMENTO 
pi = 3.14
print(type(pi))
print(int(pi))
print(round(pi))

uptime = 99.99
print(type(uptime))
print(int(uptime))
print(round(uptime))

print('\nFim do EX: 1')
os.system("pause")
clearConsole()


#------------------------------------------------------------------------------2
#FUNCAO ROUND FAZ UM ARREDONDAMENTO NAO SOMENTO PARA NUMEROS INTEIROS, MAS PODEDENDO INSERIR O NUEMRO DE CASAS DECIMAIS
first_value = round(7.654321, 2)
print(first_value)

second_value = round(9.87654, 3)
print(second_value)


'''Recapitulação
Estas são algumas ideias importantes que devem ser consideradas nesta unidade:

Operadores são minifunções de atalho que executam uma operação em um ou mais operandos (valores literais ou variáveis etc.).
Há operadores matemáticos internos para as necessidades mais comuns. 
As operações matemáticas mais avançadas foram resolvidas pelo módulo de matemática na Biblioteca Padrão do Python. 
Outras bibliotecas de software livre de terceiros abrangem uma ampla gama de funcionalidades necessárias em ciência de dados, visualização de dados e aprendizado de máquina.
A ordem das operações matemáticas no Python segue as regras do acrônimo PEMDAS.
Quando você faz a conversão de um valor do tipo float em um valor do tipo int, os valores após o decimal são truncados e perdidos. 
Use a função round() para controlar como os valores são arredondados.
Algumas funções são definidas com vários parâmetros de entrada. 
Para transmitir vários argumentos para a função, use uma vírgula (,) entre cada argumento. 
Às vezes, os argumentos são opcionais. Nesses casos, a função continua operando, mas usa um valor padrão ou implementação alternativa.'''
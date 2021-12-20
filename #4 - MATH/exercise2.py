import os
import time


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

#------------------------------------------------------------------------------1
#EMBORA NO EXEMPLO A BAIXO O AMBOS EXEMPLOS APONTAM PARA UMA CADEIA DE CARACTERES E NO MOMENTO ESTAO COMO STRING, 
#A FUNCAO ISNUMERIC INFORMA QUAL DAS VARIAVEIS PODE SER CONVERTIDA PARA UM TIPO DE DADOS INTOU FLOAT.

numeric_value = '7'
print(type(numeric_value))
print(numeric_value.isnumeric())        #TRUE

string_value = 'Bob'
print(type(string_value))
print(string_value.isnumeric())         #TRUE



print('\nFim do EX: 1')
os.system("pause")
clearConsole()

'''
isalnum()	Verifica se a cadeia de caracteres não tem caracteres especiais, como %, $, #, @ ou !.
isalpha()	Verifica se a cadeia de caracteres contém apenas letras do alfabeto.
isdecimal()	Verifica se a cadeia de caracteres contém apenas valores decimais (números).
istitle()	Verifica se a cadeia de caracteres segue as regras de uso de maiúsculas (como em uma frase).
isupper()	Verifica se a cadeia de caracteres contém apenas letras maiúsculas.
islower()	Verifica se a cadeia de caracteres contém apenas letras minúsculas.
'''

#------------------------------------------------------------------------------2

first_value = input('First Number: ')

if first_value.isnumeric() == False: #CASO O USUARIO INSERIR UM NUMERO O ISNUMERIC SERA TRUE E PULARA O IF, CASO CONTRARIO RETORNARA FALSE E ENTRARA NO IF
    print('Value is not a number.')
    exit()

second_value = input('Second Number: ')

if second_value.isnumeric() == False:
    print('Value is not a number.')
    exit()

print(type(first_value))
print(type(second_value))
first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: ' + str(sum))

print('\nFim do EX: 2')
os.system("pause")
clearConsole()

#------------------------------------------------------------------------------3

first_value = input('First Number: ')
second_value = input('Second Number: ')

if first_value.isnumeric() == False or second_value.isnumeric() == False:
    print('Please enter numbers only.')
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: ' + str(sum))


print('\nFim do EX: 3')
os.system("pause")
clearConsole()


#Recapitulação
#O isnumeric() permite verificar se um valor pode ser convertido em um int ou um float.
#A função isnumeric() é um exemplo de uma função auxiliar, porque ela dá suporte ao uso de um tipo de dados como str. Você acessa esses tipos de funções usando o operador de acessador de membro caractere de ponto (.).
#Use a função exit() para encerrar a execução do programa imediatamente.
#Às vezes, você pode usar o operador lógico or para reduzir a quantidade de código que você precisa escrever para implementar as verificações restritas.
#Uma função auxiliar opera em um valor de um tipo especificado, fornecendo utilitários úteis que permitem executar operações comuns em valores que pertencem a esse tipo de dados.
#Cada tipo de dados dá suporte a algumas funções auxiliares. Você examinou rapidamente algumas funções auxiliares str que ajudam a entender o conteúdo dos valores de cadeia de caracteres.
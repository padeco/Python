import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)




# 3 FORMAS DIFERENTES DE USA O O CAPITALIZE() 
# ESSA FUNCAO GARANTE QUE O PRIMEIRO CARACTERE DE UM CADEIA DE CARACTERES SEJA MAIUSCULA.
message = str.capitalize('first message')
print(message)

message = 'second message'.capitalize()
print(message)

message = 'third message'
print(message.capitalize())

print('Fim do EX: 7')
os.system("pause")
clearConsole()

#------------------------------------------------------------------------------8

message = 'hello world'
print(message.lower())              #FORÇA OS CARACTERES SEREM minusculas
print(message.upper())              #FORÇA OS CARACTERES SEREM MAIUSCULAS

message = message.title()           #FORMATA A CADEIA DE STRINGS A SER COMO UM TITULO (Sempre A Primeira Letra Sera Maiuscula)
print(message)
print(message.swapcase())           #iNVERTE a fORMATACAO.

print('Fim do EX: 8')
os.system("pause")
clearConsole()

#------------------------------------------------------------------------------9
#O método count() fornece uma contagem do número de vezes que um caractere especificado é usado em uma cadeia de caracteres.
location = 'Mississippi'
print(location.count('s'))

#A FUNCAO LEN() CONTA QUANTOS CARACTERES TEM EM UM LISTA DE CARACTERES
print(len('how many characters in this string?'))

print('Fim do EX: 9')
os.system("pause")
clearConsole()

#------------------------------------------------------------------------------10
# AS FUNCOES STARTSWICH() E ENDSWITCH() VERIFICAM SE AS CADEIAS DE CARACTERES INICIAM OU TERMINAM DA FORMA ESPECIFICA
message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))

print('Fim do EX: 10')
os.system("pause")
clearConsole()

#------------------------------------------------------------------------------11
def ex11():
# AFUNCAO FIND() LOCALIZA UM CARACTERE ESPECIFICO DE UMA LISTA DE CARACTERES, INICIANDO POR 0 (ZERO)
#'The quick brown fox jumps over the lazy dog' FIND('Q') = 4
    message = 'The quick brown fox jumps over the lazy dog'
    print(message.find('q'))

    print(message.find('t'))
    print(message.find('T'))

    print('Fim do EX: 11')
    os.system("pause")
    clearConsole()

#------------------------------------------------------------------------------12
def ex12():
    #REMOVE CARACTERE VAZIOS A ESQUERDA A DIREITA E AMBOS
    message = '    middle     '
    print('.' + message.lstrip() + '.')
    print('.' + message.rstrip() + '.')
    print('.' + message.strip() + '.')

    print('Fim do EX: 12')
    os.system("pause")
    clearConsole()

#------------------------------------------------------------------------------13
def ex13():
    #INVERTE UMA CADEIA DE CARACTERES POS OUTRA
    #('essence', 'soul') SERA REMOVIDO 'ESSENCE' E TROCADO POR 'SOUL'
    message = 'brevity is the essence of wit'
    message = message.replace('essence', 'soul')
    print(message)
    print('Fim do EX: 13')
    os.system("pause")
    clearConsole()

#------------------------------------------------------------------------------14
def ex14():
    #A FUNCAO RJUST() ADICIONA QUANTIDADE X DE CARACTERES DEFINIDAS PELO PRIMEIRO PARAMETRO, SEGUNDO PARAMETRO PODE SER INSERIDO PODEMOS MODIFICAR QUAL CARACTERE SERA INSERIDO.
    message = 'howdy'
    print(message.rjust(20))
    print(message.rjust(20, '-'))
    print(message.ljust(20))
    print(message.ljust(20, '-'))

    print('Fim do EX: 14')
    os.system("pause")
    clearConsole()
    

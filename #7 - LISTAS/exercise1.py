import os
import time
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()


#--------------------------------------------------------------------------1
#VOCE DEFINE UMA LISTA POR [] (COLCHETES) E SEPARA ELES POR VIRGULA (,)

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown\n']

print(colors)
print(type(colors))

#SE ADICIONAR VARIOS TIPOS DE DADOS EM UMA LISTA ELE SERA INALTEDADO E CONTINUARA SAINDO COMO LISTA.
sundry = ['John', 3.14, 7, False]
print(sundry)
print(type(sundry)) #<class 'list'>

#EXEMPLO DE LISTA VAZIA
my_list = []


print('\nFim do EX: 1')
os.system("pause")
clearConsole()

#------------------------------------------------------------------------------2
#NESSE EXEMPLO ESTAMOS CHAMANDO OS ELEMENTOS DA LISTA, ONDE O PRIMEIRO NUMERO É 0 (ZERO) DA ESQUEDA PRA DIREITA
#PODEMOS TAMBEM ACESSAR ALISTA DA DIREITA PRA ESQUERDA USANDO NUMEROS NEGATIVOS ONDE COMEÇAMOS POR -1 O ULTIMO
# -2 O PENULTIMO E ASSIM POR DIANTE
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

# print(colors)
# print(type(colors))

print(f'0-based indexing into the list ... second item: {colors[1]}')

print(f'Last item of the list: {colors[-1]}')

print(f'Next to last item in the list: {colors[-2]}')

print('\nFim do EX: 2')
os.system("pause")
clearConsole()

#------------------------------------------------------------------------------3
#SELECIONANDO UMA FATIA NO MEIO DE UMA LISTA, A CHAMADA AQUI É SEMELHANTE A CHAMADA PADRAO DA LISTA
#COM UMA DIFERENÇA QUE USAMOS : (DOIS PONTOS) PARA SEPARAR O INICIO E O FIM DA FATIA QUE IREMOS ACESSAR

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

# print(f'0-based indexing into the list ... second item: {colors[1]}')

# print(f'Last item of the list: {colors[-1]}')

# print(f'Next to last item in the list: {colors[-2]}')

print('\nPrint a SLICE, starting at index 2 and excluding index 5:') #ACESSA DO 2 AO 5 DO GREEN AO ORANGE
print(colors[2:5])
print(type(colors[2:5]))

print('\nPrint a slice, starting at index 0 to index 3:') #ACESSA DO COMECO DA LISTA 0 (ZERO) AO NUMERO 3 RED AO BLUE
print(colors[:3])

print('\nPrint a slice, starting a index 4 to the end of the list:') #DO QUERTO ELEMENTO AO ULTIMO YELLOW ATE O BROWN
print(colors[4:])

print('\nPrint a slice, from the 4th from the end (but not the last item):')
print(colors[-4:-1])

print('\nFim do EX: 3')
os.system("pause")
clearConsole()

#------------------------------------------------------------------------------4
#EXISTEM VARIAS FUNCOES ALCILIARES COMO POR EXEMPLO REVERSE QUE INVERTE ORDFEM E SORT QUE SORTEIA A ORDEM
#CUIDADO JA QUE ESSAS MUDANCAS SAO PERMANENTES
colors.reverse()
print(colors)

colors.sort()
print(colors)

#------------------------------------------------------------------------------5
#POP REMOVE UM ITEM DA LISTA

print(colors)

color = colors.pop(0)
print('popped', color)

print(colors)

#----------------------------------------------------------

print(colors)

colors.append('black')
colors.append('white')

colors.remove('yellow')
colors.remove('orange')

print(colors)
import os
import time
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

#-------------------------------------------------------------------1
#DENTRO DOS PARENTESES PODE SER INSERIDO UM PARAMETRO PARA USALO QUANDO FOR CHAMADO 
#POREM SE CHAMAR SEM O ARGUMENTO OCORRERA UM ERRO NO CODIGO
def say_hello(name):
  print(f'Hello {name}!')

say_hello('Bob')

print('\nFim do EX: 1')
os.system("pause")
clearConsole()
#-------------------------------------------------------------------2
'''Quando você define um parâmetro de entrada como parte de sua função, um argumento é necessário. 
Você poderá tornar o argumento opcional fornecendo um valor padrão que será usado se o 
chamador não passar um argumento.'''

def say_hello(name='World'):
  print(f'Hello {name}!')

say_hello()
say_hello('Bob')

print('\nFim do EX: 2')
os.system("pause")
clearConsole()

#-------------------------------------------------------------------3
'''As definições de função podem ter vários parâmetros de entrada. 
Para defini-los, separe cada par de parâmetros com uma vírgula (,).
Você também pode usar o valor None ao definir o valor padrão de um parâmetro de entrada. 
Isso permite que a função verifique se o valor None está em seu corpo e imprima uma mensagem apropriada.'''

def say_hello(name='World', greeting=None):
  if greeting == None:                      #Aqui, você adicionou o parâmetro de entrada greeting e definiu seu valor padrão como None. 
    print(f'Hello {name}!')                 #Esse valor é uma palavra-chave especial que representa o objeto NoneType.
  else:
    print(f'{greeting} {name}!')

say_hello()
say_hello('Bob')
say_hello(greeting='Howdy')
say_hello('Bob', 'Howdy')

print('\nFim do EX: 3')
os.system("pause")
clearConsole()

#-------------------------------------------------------------------4
'''Aqui, você criou a função add_two_numbers() que aceita dois parâmetros de entrada. 
Em seguida, ela executa uma operação de adição nesses parâmetros no corpo da função e retorna a soma.'''

def add_two_numbers(x, y):
    return x + y

add_two_numbers(4, 6)           #AQUI O RESULTADO DA SOMA NAO É CAPTURADO E USADO EM NADA
result = add_two_numbers(5, 7)
print(result)

print('\nFim do EX: 4')
os.system("pause")
clearConsole()

#-------------------------------------------------------------------5
'''Você pode reconhecer esse código de um módulo anterior. 
Ele gera 52 cartas combinando todos os naipes e classificações de um baralho típico. 
Conforme gera cada combinação, a função acrescenta a cadeia de caracteres a uma lista vazia chamada deck. 
A função retorna essa lista.'''

def create_deck():
  suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
  deck = []

  for  suit in suits:
    for rank in ranks:
      deck.append(f'{rank} of {suit}')

  return deck

my_deck = create_deck()
print(len(my_deck))
#print(my_deck)

print('\nFim do EX: 5')
os.system("pause")
clearConsole()

#-------------------------------------------------------------------6
'''Essa primeira versão do código define uma variável chamada value, mas não retorna value. Em vez disso, 
você deseja apenas ver se o código pode acessar value fora do bloco de código da função.'''
'''
def some_function():
    value = 10

print(value)'''

# AQUI NAO CHAMAMOS A FUNCAO AO IMPRIMIR A VARIAVEL VALUE, ENTAO O RESULTADO SERA O VALOR DA VARIAVEL FORA DA
# FUNCAO, JA QUE O VALOR DELA DENTRO DA FUNCAO ATE FOI RETORNADO MAS NAO FOI ALOCADO A VARIAL DE FORA.
value = 1

def some_function():
    value = 10
    return value

print(value)
some_function() # SE NAO FOR ATRIBUIDA A NADA NAO SERA IMPRESSA
print(value)

'''Moral da história: as variáveis definidas fora de uma função não afetam as variáveis definidas dentro dela, 
a menos que o código retorne o valor interno e, em seguida, o use. 
O escopo das variáveis de uma função é selado e ocultado do código fora da função e vice-versa.'''
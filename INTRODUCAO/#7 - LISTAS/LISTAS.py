import limpa

'''Listas Python
Resumindo, uma lista é uma coleção de objetos arbitrários, algo semelhante a um array em muitas outras linguagens de programação, 
mas mais flexível. As listas são definidas em Python, 
colocando uma sequência separada por vírgulas de objetos entre colchetes ( []), conforme mostrado abaixo:'''

limpa.clearConsole()

a = ['foo', 'bar', 'baz', 'qux']

print('a= ' + str(a))
print('fim\n')

a = ['foo', 'bar', 'baz', 'qux']
b = ['baz', 'qux', 'bar', 'foo']

print('a= ' + str(a))
print('\n')
print('b= ' + str(b))
print(a == b)                       #<false>
print(a is b)                       #<false>

print('\n')
limpa.os.system('pause')
limpa.clearConsole()

########################################################################################################################
'''
Listas podem conter objetos arbitrários
Uma lista pode conter qualquer variedade de objetos. Os elementos de uma lista podem ser todos do mesmo tipo:
'''

a = [2, 4, 6, 8]
print(a)            #[2, 4, 6, 8]

'''
Ou os elementos podem ser de vários tipos:
'''
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
print(a)
print('\n')

print(int)                          #<class 'int'>
print(len)                          #<built-in function len>

def foo():
    pass

print(foo)                          #<function foo at 0x035B9030>

import math
print(math)                         #<module 'math' (built-in)>

a = [int, len, foo, math]
print(a)                            #[<class 'int'>, <built-in function len>, <function foo at 0x02CA2618>, <module 'math' (built-in)>]

print('\n')
limpa.os.system('pause')
limpa.clearConsole()

########################################################################################################################
'''Uma lista pode conter qualquer número de objetos, de zero a tantos quanto a memória do seu computador permitir:'''

a = []
print(a)

a = ['foo']
print(a)

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

print (a)

'''Os objetos de lista não precisam ser exclusivos. Um determinado objeto pode aparecer em uma lista várias vezes:'''

a = ['bark', 'meow', 'woof', 'bark', 'cheep', 'bark']
print(a)

# Os elementos da lista podem ser acessados ​​pelo índice
# Os índices para os elementos em asão mostrados abaixo:
# Praticamente tudo sobre indexação de string funciona de maneira semelhante para listas. 
# Por exemplo, um índice de lista negativa conta a partir do final da lista:

a =                  ['foo',   'bar',  'baz',  'qux',  'quux',  'corge']
indice_de_a =        ['0',     '1',    '2',    '4',    '5',      '6']
indice_inverso_de_a =['-6',    '-5',   '-4',   '-3',   '-2',     '-1']

print(a[0])
print(a[1])
print(a[2])
print('\n')
print(a[-1])
print(a[-2])
print(a[-3])
########################################################################################################################
print('\n')
limpa.os.system('pause')
limpa.clearConsole()

#Fatiar também funciona. Se "a" for uma lista, a expressão "a[m:n]" retorna a parte de ado índice mpara, mas não incluindo, o índice n:

print(a[2:5]) #['baz', 'qux', 'quux']

print(a[-5:-2]) #['bar', 'baz', 'qux']
print(a[1:4]) #['bar', 'baz', 'qux']
print(a[-5:-2]==a[1:4]) #[true]

#A omissão do primeiro índice inicia a fatia no início da lista e a omissão do segundo índice estende a fatia até o final da lista:
a = ['foo',   'bar',  'baz',  'qux',  'quux',  'corge']
print(a[:4], a[0:4]) #['foo', 'bar', 'baz', 'qux'] ['foo', 'bar', 'baz', 'qux']
print(a[2:], a[2:len(a)]) #['baz', 'qux', 'quux', 'corge'] ['baz', 'qux', 'quux', 'corge']
print(a[:4] + a[4:]) #['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print('\n')
print(a[0:6:2]) #['foo', 'baz', 'quux'] # começa em ZERO e le ate 6 no caso o ultimo ja que nao tem ate 6 mas de 2 em 2
print(a[1:6:2]) #['bar', 'qux', 'corge']
print(a[6:0:-2])#['corge', 'qux', 'bar']
########################################################################################################################

print('\n')
limpa.os.system('pause')
limpa.clearConsole()

#se colocar o s valores negativos ele ira fazer os passos inversamente ao normal

print(a[::-1]) #['corge', 'quux', 'qux', 'baz', 'bar', 'foo']

# Os operadores de concatenação ( +) e replicação ( *):

print(a) # ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

a + ['grault', 'garply'] # se usar o sinal de + ira adicionar os valores especificados na lista
#['foo', 'bar', 'baz', 'qux', 'quux', 'corge', '<grault>', '<garply>']

a * 2                   # multipica a lista em x determinado pelo parametro apos o *
#['foo', 'bar', 'baz', 'qux', 'quux', 'corge', '<foo>', '<bar>', '<baz>','<qux>', '<quux>', '<corge>']

['foo', 'bar', 'baz', 'qux', 'quux', 'corge'][2] #se for impresso Retornara o indice 2 da Lista = '<baz>'


['foo', 'bar', 'baz', 'qux', 'quux', 'corge'][::-1] #sera impresso de forma contraria a partir do "-1" que é <corge> ['corge', 'quux', 'qux', 'baz', 'bar', 'foo']


'quux' in ['foo', 'bar', 'baz', 'qux', 'quux', 'corge'] # verifica se '<quux>' esta na lista retorna um <bool> No caso true


['foo', 'bar', 'baz'] + ['qux', 'quux', 'corge'] # soma as duas listas


len(['foo', 'bar', 'baz', 'qux', 'quux', 'corge'][::-1]) # len conta quantas elementos tem na lista comecando de "-1" ate "-6" e retorna o valor  = 6

print('If Comrade Napoleon says it, it must be right.'[::-1])

print('\n')
limpa.os.system('pause')
limpa.clearConsole()
##############################################################################################################################################

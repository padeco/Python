'''<INTERVALO> é uma coleção de objetos - por exemplo, uma lista ou tupla. 
Os <statementS> no corpo do loop são denotados por indentação, 
como acontece com todas as estruturas de controle do Python, e são executados uma vez para cada item em <INTERVALO>. 
A variável de loop <VARIAVEL> assume o valor do próximo elemento a <INTERVALO> cada vez que ocorre no loop.'''



#ESTRUTURA DO FOR:

# for <VARIAVEL> in <INTERVALO>:
#     <statementS>

a = ['foo', 'bar', 'baz']
for i in a:
    print(i)
'''    
foo
bar
baz'''


######################################################################################################
'''Ok, agora você sabe o que significa para um objeto ser iterável e sabe como usá-lo 
iter()para obter um iterador dele. Depois de obter um iterador, o que você pode fazer com ele?

Um iterador é essencialmente um produtor de valor que produz valores sucessivos de seu objeto iterável associado.
A função embutida next()é usada para obter o próximo valor do iterador.'''


a = ['foo', 'bar', 'baz']

itr = iter(a)
itr #<list_iterator object at 0x031EFD10>


next(itr)
#foo
next(itr)
#bar
next(itr)
#baz

'''Iterando por meio de um dicionário
Você viu anteriormente que um iterador pode ser obtido de um dicionário com iter(), 
portanto, você sabe que os dicionários devem ser iteráveis. 
O que acontece quando você percorre um dicionário? Vamos ver:'''

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)
'''
foo
bar
baz'''

for k in d:   # OU          for v in d.values():
     print(d[k])  #           print(v)
'''
1
2
3
'''


for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)
'''
1 2
3 4
5 6
'''

'''Conforme observado no tutorial sobre dicionários Python , o método de dicionário .items()
retorna efetivamente uma lista de pares de chave / valor como tuplas:'''

d = {'foo': 1, 'bar': 2, 'baz': 3}

d.items()
#dict_items([('foo', 1), ('bar', 2), ('baz', 3)])



d = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in d.items():
    print('k =', k, ', v =', v)
    
'''
k = foo , v = 1
k = bar , v = 2
k = baz , v = 3'''
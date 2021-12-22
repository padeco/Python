from os import readlink
from types import ClassMethodDescriptorType
import limpa

#--------------------------------------------------------------------------1


#  EXEMPLO PADRAO DE DICIONARIO
# ONDE "d" É O NOME DO DICIONARIO 
# KEY É SAO VALORES PRINCIPAIS E VALUE SAO OS VALORES ASSOCIADOS A CADA KEY CORRESPONDENTE

'''
d = {
    <key>: <value>,
    <key>: <value>,
    <key>: <value>
}
'''

# EXEMPLO:
# NESSE EXEMPLO TEMOS OS NOMES DOS TIMES DE BASEBALL DE CADA LUGAR 'Seattle' => 'Mariners'
MLB_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}

# UM DICIONARIO TAMBEM PODE SER CRIADO COM A FUNCAO 'dict()' UMA FUNCAO INTERNA
# O ARGUMENTO DA DICT() DEVE SER UM PAR DE VALORES-CHAVE COMO NO EXEMPLO A BAIXO
'''
d = dict([
    (<key>, <value>),
    (<key>, <value>),
    
    (<key>, <value>)
])
'''

#EXEMPLO DE COMO FICARIA O DICIONARIO DOS TIMES
MLB_team1 = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
])

# SE OS VALORES-CHAVE FOREM STRING SIMPLES VOCE PODE DEFINIR ELES DA SEGUINTE FORMA:
MLB_team2 = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)
limpa.os.system('pause')
limpa.clearConsole()

print(type(MLB_team))

print(MLB_team)

print(MLB_team1)
print(MLB_team2)
print('\n')
limpa.os.system('pause')
limpa.clearConsole()

#As entradas no dicionário são exibidas na ordem em que foram definidas. 
# Mas isso é irrelevante quando se trata de recuperá-los. 
# Os elementos do dicionário não são acessados ​​por índice numérico:
#MLB_team[1] <<<< isso esta errado

# AFORMA CORRETA DE ACESSAR <KEYS> DO MLB_team

MLB_team['Minnesota']

MLB_team['Colorado']

print(MLB_team['Minnesota'])
print(MLB_team['Colorado'])

print('\n')
limpa.os.system('pause')
limpa.clearConsole()

# SE VOCE SE REFERIR A UMA CHAVE QUE NAO EXISTE NO DICIONARIO ELE TRATA UM ERRO:
#File "c:\Users\manoel.torres\OneDrive - Kumulus\Documents\GitHub\Python\INTRODUCAO\#9 - DICIONARIO\BLOCO_PADRAO.py", line 88, in <module>       
#    MLB_team['Toronto']
#KeyError: 'Toronto'

#MLB_team['Toronto']
#print(MLB_team['Toronto'])


#----------------------------------------------------------------------------------
#ADICIONAR UM CHAVE AO DICIONARIO É SIMPLES BASTA ATRIBUIR OS VALOR-CHAVE E O VALOR 
# NESSE EXEMPLO A <KEY1> <kansas city> E O <VALOR> É <Royals>

print(MLB_team)
MLB_team['Kansas City'] = 'Royals'

print(MLB_team)

print('\n')
limpa.os.system('pause')
limpa.clearConsole()

#PARA EDITAR UM VALOR BASTA CHAMAR O VALOR-CHAVE E ATRIBUIR UM NOVO VALOR PARA ELE:
print(MLB_team)
MLB_team['Seattle'] = 'Seahawks' #TROCANDO <Seattle>: <Mariners> POR <Seattle> <Seahawks>
print(MLB_team)

print('\n')
limpa.os.system('pause')
limpa.clearConsole()

#PARA EXCLUIR UM VALOR É TAO SIMPLES QUANTO ADICIONAR, BASTA ADICIONAR A FUNCAO DEL ANTES DE CHARMAR O DICIONARIO
print(MLB_team)
del MLB_team['Seattle']
print(MLB_team)

print('\n')
limpa.os.system('pause')
limpa.clearConsole()


# Chaves de dicionário vs. índices de lista
# TENTAR CHAMAR UM VALOR COM UM VALOR-CHAVE INESISTENTE OU POR UM INDECE NUMERO IRA TRAZER O MESMO ERRO: <KEYERROR>
# EMBORA UMA FORMA PARECE SER <STRING> E OUTRA <INT> AMBAS SAO UM VALOR <IMUTAVEL> QUE CHAMA O VALOR DO DICIONARIO
# NAO IMPORTA A ORDEM DO DICIONARIO
# MLB_team['Toronto']
# MLB_team[1]

# A SINTAXE PODE ATE SER SEMELHANTE MAS VOCE NAO PODE TRATAR UM DICIONARO COMO UMA LISTA, CHAMANDO O ULTIMO
# VALOR DA LISTA COMO SE FOSSE UM INDECE:
De = {3: 'd', 2: 'c', 1: 'b', 0: 'a'}
print(De[0])
print(De[3])
# FORMA ERRADA <print (De[-1])>


print('\n')
limpa.os.system('pause')
limpa.clearConsole()

PESSOA = {}
print(type(PESSOA)) #<class 'dict'>

PESSOA ['Nome'] = 'Manoel'
PESSOA ['Sobrenome'] = 'Torres'
PESSOA ['Idade'] = 'Idade'
PESSOA ['Estado Civil'] = 'Solteiro'
PESSOA ['Filhos'] = ['Malcon','Maria','Joe']                # UMA <LISTA> DENTRO DE UM <DICIONARIO>
PESSOA ['Pets'] = {'Cachorro' : 'jorge', 'Gato': 'Nao'}     # UM <DICIONARIO> DENTRO DE OUTRO

print(PESSOA)
print('\n')
print(PESSOA['Nome'])
print(PESSOA['Idade'])
print(PESSOA['Estado Civil'])
print(PESSOA['Filhos'])
print(PESSOA['Pets'])
print('\n')

print(PESSOA['Filhos'][-1])         # POR SE TRATAR DE UMA LISTA (<FILHOS>) PODEMOS CHAMAR ELE PELO INDICE
print(PESSOA['Pets']['Gato'])       # NESSE CASO POR SER UM <DICIONARIO> DEVEMOS CHAMAR A PALAVRA CHAVE

print('\n')
limpa.os.system('pause')
limpa.clearConsole()

# EM UM <DICIONARIO> QUASE QUALQUER VALOR PODE SER USADO COMO UM DICIONARIO COMO O EXEMPLO A BAIXO:
# 42 <INT> - 2.78 <FLOAT> E TRUE <BOOL>
foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}

#VOCÊ PODE ATÉ USAR OBJETOS INTEGRADOS, COMO TIPOS E FUNÇÕES:

d = {int: 1, float: 2, bool: 3}
#PRINT(d[float]) EXIBIRA  2

'''
NO ENTANTO, EXISTEM ALGUMAS RESTRIÇÕES ÀS QUAIS AS CHAVES DE DICIONÁRIO DEVEM OBEDECER.
PRIMEIRO, UMA DETERMINADA CHAVE PODE APARECER EM UM DICIONÁRIO APENAS UMA VEZ. 
CHAVES DUPLICADAS NÃO SÃO PERMITIDAS. 
UM DICIONÁRIO MAPEIA CADA CHAVE PARA UM VALOR CORRESPONDENTE, 
PORTANTO, NÃO FAZ SENTIDO MAPEAR UMA CHAVE ESPECÍFICA MAIS DE UMA VEZ.
VOCÊ VIU ACIMA QUE, AO ATRIBUIR UM VALOR A UMA CHAVE DE DICIONÁRIO JÁ EXISTENTE, 
ELE NÃO ADICIONA A CHAVE UMA SEGUNDA VEZ, MAS SUBSTITUI O VALOR EXISTENTE
'''

#<E-----------------------------------------------------------------------------

#Uma tupla também pode ser uma chave de dicionário, porque tuplas são imutáveis:

d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
print(d[(1,1)])


'''
Lembre-se da discussão sobre tuplas que uma razão para usar uma 
tupla em vez de uma lista é que existem circunstâncias em que um tipo imutável é necessário. 
Este é um deles.)

No entanto, nem uma lista nem outro dicionário podem servir como chave de dicionário, 
porque listas e dicionários são mutáveis:
''' 
# <ERRADO> d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'} POIS [] SAO UM LISTA



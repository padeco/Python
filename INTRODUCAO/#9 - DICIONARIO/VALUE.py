from os import readlink
from types import ClassMethodDescriptorType
import limpa

#RESTRIÇÕES AOS VALORES DO DICIONÁRIO
'''
POR OUTRO LADO, NÃO HÁ RESTRIÇÕES AOS VALORES DO DICIONÁRIO. 
LITERALMENTE, NENHUM. 
UM VALOR DE DICIONÁRIO PODE SER QUALQUER TIPO DE OBJETO QUE O PYTHON SUPORTA, 
INCLUINDO TIPOS MUTÁVEIS COMO LISTAS E DICIONÁRIOS, E OBJETOS DEFINIDOS PELO USUÁRIO, 
SOBRE OS QUAIS VOCÊ APRENDERÁ NOS PRÓXIMOS TUTORIAIS.
TAMBÉM NÃO HÁ NENHUMA RESTRIÇÃO CONTRA UM DETERMINADO VALOR QUE APARECE EM UM DICIONÁRIO VÁRIAS VEZES:
'''
d = {0: 'a', 1: 'a', 2: 'a', 3: 'a'}

print(d[0] == d[1] == d[2])

print('\n')
limpa.os.system('pause')
limpa.clearConsole()


MLB_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}

print('Americana' in MLB_team)
print('Colorado' in MLB_team)
print('Americana' not in MLB_team) 
print('\n')
limpa.os.system('pause')
limpa.clearConsole()

'''VOCÊ PODE USAR O IN OPERADOR JUNTO COM A AVALIAÇÃO DE CURTO-CIRCUITO 
PARA EVITAR GERAR UM ERRO AO TENTAR ACESSAR UMA CHAVE QUE NÃO ESTÁ NO DICIONÁRIO:'''

# MLB_team['Toronto']#<ERRADO> POIS NAO EXISTE NO DICIONARIO

print('Toronto' in MLB_team and MLB_team['Toronto'])    # CASO PRIMEIRO VALOR DE <FALSE> ELE NAO CONTINUA 
print('Seattle' in MLB_team and MLB_team['Seattle'])    # COMO <SEATLE> ESTA NA LISTA RESULTADO É <TRUE> ENTAO ELE BUSCA A CHAVE NO DICIONARIO.
print(len(MLB_team))                                    # CONTA A QUALIDADE DE VALORES-CHAVE NO DICIONARIO
print('\n')
limpa.os.system('pause')
limpa.clearConsole()

# FUNCAO <CLEAR> clear() LIMPA TODAS OS VALORES-CHAVE DO DICIONARIO

MLB_team.clear()
print(MLB_team)
'''
O .GET() MÉTODO DE DICIONÁRIO PYTHON FORNECE UMA MANEIRA CONVENIENTE 
DE OBTER O VALOR DE UMA CHAVE DE UM DICIONÁRIO SEM VERIFICAR COM ANTECEDÊNCIA SE A 
CHAVE EXISTE E SEM GERAR UM ERRO.
D.GET(<KEY>)PESQUISAS DICIONÁRIO <D> PARA <KEY>E RETORNA O VALOR ASSOCIADO SE ELE FOR ENCONTRADO. 
SE <KEY>NÃO FOR ENCONTRADO, RETORNA NONE:
'''

d = {'a': 10, 'b': 20, 'c': 30}
print(d.get('b'))
print(d.get('J'))
print('\n')

#SE <KEY> NÃO FOR ENCONTRADO E O <DEFAULT> ARGUMENTO OPCIONAL FOR ESPECIFICADO, 
# ESSE VALOR SERÁ RETORNADO EM VEZ DE NONE:
print(d.get('j','Não Encontrado'))
print('\n')

d = {'a': 10, 'b': 20, 'c': 30}
print(list(d.items())[1][0])    # d.0.1 = 'a', d.1.0 = 'b', d.3.0 = 'c'. 
                                # "1" <UM> = "B"  
                                # "0" <ZERO> INDICA SE ELE MOSTRARA O <KEY> OU O <VALUE>
                                # SE FOSSE "1" "1" [1][1] RETORNARIA 20
print(list(d.items())[1][1]) 


print(list(d.keys()))                           # D.KEYS()RETORNA UMA LISTA DE TODAS AS CHAVES EM D
print(list(d.values()))                         # D.VALUE()RETORNA UMA LISTA DE TODAS AS VALORES EM D
print((d.pop('b','Nao encontrado')))            # D.POP() SE ENCONTRAR O VALOR DENTO DO ARGUMENTO REMOVE DO DICIONARIO E RETORNA SEU VALRO

print('\n')
limpa.os.system('pause')
limpa.clearConsole()


print(d.popitem())  # D.POPITEM() REMOVE O ÚLTIMO PAR DE VALORES-CHAVE ADICIONADO DE O RETORNA COMO UMA TUPLA:
                    # SE ESTIVE VAZIO RETORNA <KEYERROR>

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

d1.update(d2) #D1 RECEBE OS VALORES DE D2 SE JA TIVER UM KEY DENTRO DE K1 OS VALORES SERAO SUBSTITUIDOS
print(d1)

d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update([('b', 200), ('d', 400)]) # TAMBEM PODEM SER ATUALIZADOS RECEBENDO TUPLAS
print(d1)

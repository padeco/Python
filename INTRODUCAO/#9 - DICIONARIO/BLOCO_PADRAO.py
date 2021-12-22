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
    (<key>, <value),
    
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
limpa.clearConsole()

print(type(MLB_team))

print(MLB_team)

print(MLB_team1)
print(MLB_team2)
print('\n')
from functools import reduce
from pprint import pprint
import time

_print = print
print = pprint

def data(data):
    '''funcao que faz a comparacao entre as datas'''
    date1 = "01/01/2012"
    date2 = data['12 months ending']
    newdate1 = time.strptime(date1, "%d/%m/%Y")
    newdate2 = time.strptime(date2, "%d/%m/%Y")
    if newdate1 <= newdate2:
        return data['12 months ending']
    
arquivo_completo = ('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\EXERCICIOS\\ex4_kumulus\\reccrimepfa-210902-120414.csv')
    
linhas = (line for line in open(arquivo_completo))
lista_linha = (s.rstrip().split(",") for s in linhas)
colunas = next(lista_linha)
para_dicio = (dict(zip(colunas, data)) for data in lista_linha)

crimes_dicio = map(lambda x:x['Rolling year total number of offences'],filter(data,para_dicio))

result_soma = reduce(lambda soma, crime: soma + int(crime), crimes_dicio, 0 )

print(f'Resultado da soma dos crimes a partir de 2012 é {result_soma}')
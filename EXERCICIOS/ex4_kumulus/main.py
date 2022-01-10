from functools import reduce
from pprint import pprint
import csv
import sys

_print = print
print = pprint

arquivo_completo = ('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\EXERCICIOS\\ex4_kumulus\\reccrimepfa-210902-120414.csv')

with open(arquivo_completo, 'r') as arquivo:
    
    arquivo_csv = iter(csv.DictReader(arquivo, delimiter=','))
    #for linha in arquivo_csv:
    print(type(arquivo_csv))
    print(sys.getsizeof(arquivo_csv))   
         
    anos = (
        map(lambda x: x['12 months ending'],
            filter(
            lambda x: x ['12 months ending']== '31/03/2013', 
               arquivo_csv
               )       )
        )

    print(list(anos))
    print(sys.getsizeof(anos))
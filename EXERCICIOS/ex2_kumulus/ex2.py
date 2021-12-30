import pandas as pd
from datetime import datetime

from pandas.io import json

df = pd.read_csv('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\Exercicios\\ex1_kumulus\\crimes3.csv')

vetor = []

lista = df['Region'].unique()

for i in lista:
    df_i = df[(df['Rolling year total number of offences'] > 10) & (df['Region'] == i)].groupby(['Offence'],as_index = False).sum()
    vetor.append({})
    vetor[-1]['Data de processo'] = datetime.now().strftime('%d-%m-%Y %H:%M')
    vetor[-1]['Regiao'] = i
    if len(df_i['Offence'].unique()) > 2:
        vetor[-1]['Crimes'] = df_i.to_dict('records')

print(json.dumps(vetor, indent=2))

random_file = open('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\Exercicios\\ex1_kumulus\\ex1.json', 'w')

random_file.write(json.dumps(vetor, indent=2))

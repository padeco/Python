import os
import csv
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()




with open('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\ex1\\crimes.csv', encoding='utf-8') as reader:
    has_header = csv.Sniffer().has_header(reader.read(1024)) # pula cabeçalho
    reader.seek(0) # ''
    tabela = csv.reader(reader) # ''

    if has_header:
        next(reader)

    for l in tabela:
        if l[1] == "Avon and Somerset":
            print( 'Região: ' + str(l[2]),'\n\tQtd roubos: ' + str(l[4]), '\tTipo de Roubo: ' + str(l[3]),'\n')
        else:
                break
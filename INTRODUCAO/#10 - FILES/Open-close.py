import limpa

limpa.clearConsole()
limpa.os.system("pause")
print('\n')
########################################################################################################################################

#FORMA DE ABRIR ARQUIVOS:

#file = open('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\INTRODUCAO\\#10 - FILES\\dog_breeds.txt', 'r')
#print(file.readline())
#print(file.read())


#FECHANDO O ARQUIVO
#FECHAR O ARQUIVO É IMPORTANTE PARA QUE NAO TENHA VAZAMENTO DE INFORMACOES E GRAVACOES INDEVIDAS
#limpa.os.system("pause")


limpa.clearConsole()
print('\n')
###################################################################################################################


#FUNCAO TRY ABRE O ARQUIVO E O MANTEM ABERTO ATE QUE FINALIZE O CODIGO 
reader = open('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\INTRODUCAO\\#10 - FILES\\dog_breeds.txt')
try:
   # Further file processing goes here
   print(reader.read())
finally:
    reader.close() 

limpa.os.system("pause")
limpa.clearConsole()
print('\n')
######################################################################################################################

#POR FIM TEMOS A FUNCAO <WITH> QUE ABRE O ARQUIVO E FECHA O ARQUIVO ASSIM QUE ELE SAI DO BLOCO WITH.

with open('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\INTRODUCAO\\#10 - FILES\\dog_breeds.txt', 'r') as arq:
    print(arq.readline())
    limpa.os.system("pause")
    limpa.clearConsole()
######################################################################################################################

with open('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\INTRODUCAO\\#10 - FILES\\dog_breeds.txt', 'r') as arq:
    print(arq.read())
    limpa.os.system("pause")
    limpa.clearConsole()
######################################################################################################################

#IMPRIME OS 5 PRIMEIROS BYTES DE CADA LINHA
with open('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\INTRODUCAO\\#10 - FILES\\dog_breeds.txt', 'r') as arq:
    print(arq.readline(5))
    print(arq.readline(5))
    print(arq.readline(5))
    print(arq.readline(5))
    print(arq.readline(5))
    print(arq.readline(5))
    limpa.os.system("pause")
    limpa.clearConsole()
######################################################################################################################

f = open('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\INTRODUCAO\\#10 - FILES\\dog_breeds.txt')
print(f.readlines())
limpa.os.system("pause")
limpa.clearConsole()
######################################################################################################################

with open('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\INTRODUCAO\\#10 - FILES\\dog_breeds.txt', 'r') as reader:
    linha = reader.readline()
    while linha != '':
        print(linha, end='')
        linha = reader.readline()
    limpa.os.system("pause")
    limpa.clearConsole()
######################################################################################################################    

with open('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\INTRODUCAO\\#10 - FILES\\dog_breeds.txt', 'r') as reader:
    for linha in reader.readlines():
        print(linha, end = '')




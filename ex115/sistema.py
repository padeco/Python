from lib.interface import *
from lib.arquivo import *
import lib.interface.limpa
lib.interface.limpa.clearConsole()

arq = 'C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\ex115\\crimes.csv'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['ler Arquivo', 'Cadastro de crimes', 'Sair'])
    if resposta == 1:
        #opcao de listar o conteudo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #opcao de cadastro de crimes
        cabeçalho('Novo Crime')
        nome = str(input('Nome: '))
        pena = leiaint('Pena: ')
        cadastrar(arq, nome, pena)
    elif resposta == 3:
        #sair do Sistema
        cabeçalho('Saindo.. Até logo')
        lib.interface.limpa.time.sleep(2)
        exit()        
    else:
        print('\033[31mErro, Opção invalida!\033[m')
    lib.interface.limpa.time.sleep(2)


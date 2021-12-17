import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
resposta = 0
def main():
    
    clearConsole()
    print('''
    ___________                                 
    \__    ___/_________________   ____   ______
      |    | /  _ \_  __ \_  __ \_/ __ \ /  ___/
      |    |(  <_> )  | \/|  | \/\  ___/ \___ \ 
      |____| \____/|__|   |__|    \___  >____  >
                                      \/     \/ ''')
    print('Selecione as opces para navegar entre os exercicios:\n')
    print('escolha a aula:')
    resposta = input()
    #teste = ('ex' + resposta + ())
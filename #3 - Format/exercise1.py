import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

resposta = 0
clearConsole()
print('Escolha qual Execicio voce quer testar:')
#if resposta ==

first_string = 'A literal string'
second_string = "A literal string"
print(second_string == first_string) #TRUE POIS NAO TEM DIFERENCA DE ASPAS SIMPLES PRA DUPLAS NESSE EXEMPLO.

print('Fim do EX: 1')
os.system("pause")
clearConsole()


#------------------------------------------------------------------------------2
third_string = 'A single quoted literal string with a " double quote'
fourth_string = "A double quoted literal string with a ' single quote"
print(third_string)
print(fourth_string)

print('Fim do EX: 2')
os.system("pause")
clearConsole()


#------------------------------------------------------------------------------3
fifth_string = 'A single quoted literal string with an \' escaped single quote' #IGNORA A ASPAS SIMPLES APOS A \ (BARRA)
sixth_string = "A double quoted literal string with a \" double quote"          #IGNORA A ASPAS DUPLAS APOS A \ (BARRA)
seventh_string = 'A literal string with a \n new line character'                #PULA A LINHA
eighth_string = 'A literal string with a \t tab character'                      #TABULA OS PROXIMAS CARACTERES SIMILAR A TECLA (TAB)

print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eighth_string)

print('Fim do EX: 3')
os.system("pause")
clearConsole()

#------------------------------------------------------------------------------4
ninth_string = r"A literal string with a \n new line character printed raw" 
# COM O 'R' ANTES DA STRING ELE DESCONSIDERA OS POSSIVEIS TIPOS DE FORMATACAO QUE PODE TER ALI DENTRO.
print(ninth_string)

print('Fim do EX: 4')
os.system("pause")
clearConsole()

#------------------------------------------------------------------------------5
#INSERIR ''' OU """ (FECHANDO DA MESMA FORMA) IRA INICIAR UMA CADEIA DE CARACTERES VERBIAM, 
#MANTENDO A FORMATACAO COMO FOI ESCRITA
tenth_string = '''A literal string              
on more than one line
sometimes known as a verbatim string'''

eleventh_string = """Another literal string
     on more than one line
using double quotes"""

print(tenth_string)
print(eleventh_string)

print('Fim do EX: 5')
os.system("pause")
clearConsole()

#------------------------------------------------------------------------------6
#INSERE ALGUM TIPO DE CARACTERE NO MEIO DE CADA VARIAVEL, DEFINIDA PELO SEP=(MEIO) END=(FINAL)
first = 'Conrad'
second = 'Grant'
third = 'Bob'
print(first, second)
print(first, second, third)
print(first, second, third, sep='-')
print(first, second, third, sep='-', end='.')

print('Fim do EX: 6')
os.system("pause")
clearConsole()

#------------------------------------------------------------------------------7

import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()
 #---------------------------------------------------------------------------------#
                                    #type motra o tipo da variavel.
print(type('Hello world'))          #string
print(type(7))                      #Int

print(type(True))                   #booliana
print(type(False))                  #booliana

print(type('True'))                 #String por conter aspas simples (')
print(type('False'))                #String por conter aspas simples (')

print('Fim do EX: 1')
os.system("pause")

clearConsole()


 #---------------------------------------------------------------------------------#
                                    #bool transforma as cadeias de caracteres em TRUE e FALSE.
                                    #Quando a função é fornecida com uma cadeia de caracteres vazia, ela retorna FALSE, 
                                    #Enquanto que qualquer outra cadeia de caracteres não vazia retorna TRUE.

print(bool('True'))                 #FALSE
print(bool('False'))                #FALSE
print(bool(''))                     #TRUE
print(bool('0'))                    #FALSE
print(bool('Hello world!'))         #FALSE

print('Fim do EX: 2')
os.system("pause")

clearConsole()


 #---------------------------------------------------------------------------------#
                                    #SIMILAR AO CODIGO ANTERIOR, POREM POR SER INT 
                                    #TUDO DIFERENTE DE 0 (ZERO) SERA CONSIDERADO TRUE   
print(bool(7))                      #TRUE
print(bool(1))                      #TRUE
print(bool(0))                      #FALSE
print(bool(-1))                     #TRUE

print('Fim do EX: 3')
os.system("pause")

clearConsole()


                                    #O que é uma expressão booliana?
                                    #À medida que adicionar lógica aos nossos aplicativos, você avaliará expressões boolianas. Um exemplo simples ilustra a ideia básica.
                                    #1 + 1 = 3
                                    #Essa é uma instrução False. Mas:
                                    #1 + 1 = 2
                                    #é uma instrução True. Em ambos os exemplos da matemática inicial, estamos avaliando a expressão inteira para ver se ela é verdadeira ou falsa.
                                    #No Python, uma expressão booliana faz a mesma coisa. Uma expressão booliana expande essa ideia para qualquer chamada de função que, por fim, retorna True ou False.
                                    #No Python, usamos o operador de igualdade == para criar uma expressão booliana que avalia dois valores quanto a igualdade. O operador de igualdade usa dois símbolos de sinal de igual.

#---------------------------------------------------------------------------------#
                                    #MOSTRA SE UM RESULTADO DE UMA OPERACAO É TRUE OU FALSE

print(1 + 1 == 3)                   #FALSE
print(1 + 1 == 2)                   #TRUE


print('Fim do EX: 4')
os.system("pause")

clearConsole()

#---------------------------------------------------------------------------------#
                                    #MOSTRA SE UM RESULTADO DE UMA OPERACAO É TRUE OU FALSE

print(3 == 4)                       #FALSE
print(3 != 4)                       #TRUE
print(3 > 4)                        #FALSE
print(3 < 4)                        #TRUE
print(3 >= 4)                       #FALSE
print(3 <= 4)                       #TRUE

print('Fim do EX: 5')
os.system("pause")

clearConsole()

#---------------------------------------------------------------------------------#
                                    #MOSTRA SE UM RESULTADO DE UMA OPERACAO É TRUE OU FALSE

primeiro_numero = 5
segundo_numero = 0
valor_verdadeiro = True
valor_falso = False

if primeiro_numero > 1 and primeiro_numero <10:
    print('Este valor esta ente 1 e 10')

if primeiro_numero> 1 or segundo_numero > 1:
    print('Pelo menos uns dos valores é maior que 1')

print(not valor_verdadeiro)
print(not valor_falso)

if not primeiro_numero > 1 and segundo_numero <10:  #primeiro_numero = 5 ou seja MAIOR que 1 = TRUE
                                                    #segundo_numero = 0 ou seja MENOR que 10 = TRUE
                                                    #porem o NOT inverte os resultados transformando em FALSE
    print('Os valores passam no teste')
else:
    print('Os Valores NÃO passam no TEST')

print('Fim do EX: 6')
os.system("pause")

clearConsole()


#Recapitulação
#Use a função bool() para converter cadeias de caracteres e inteiros em valores boolianos. 
# Cadeias de caracteres não vazias são convertidas em True e números diferentes de zero são convertidos em True. 
# Cadeias de caracteres vazias são convertidas em False. O valor 0 é convertido em False.

#O Python fornece vários operadores de comparação para testar a igualdade, 
# desigualdade e maior ou menor que.

#O Python também fornece vários operadores lógicos para garantir que uma ou ambas as expressões boolianas sejam True. 
# Ele também fornece o operador not para garantir que as expressões boolianas sejam avaliadas como False.
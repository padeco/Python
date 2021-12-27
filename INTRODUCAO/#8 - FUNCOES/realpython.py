import limpa
limpa.clearConsole()


'''*<ARGS> E **<KWARGS> PERMITEM QUE VOCÊ PASSE VÁRIOS ARGUMENTOS OU ARGUMENTOS DE PALAVRA-CHAVE PARA UMA FUNÇÃO. CONSIDERE O SEGUINTE EXEMPLO. 
ESTA É UMA FUNÇÃO SIMPLES QUE RECEBE DOIS ARGUMENTOS E RETORNA SUA SOMA'''

def my_sum(a, b):
    return a + b

############################################################################
#ESSA FUNCAO ATE FUNCCIONA, MAS VOCE PRECIS INFORMAR UMA LISTA DE ANTEMAO PARA QUE ELA FUNCIONE 

def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))

############################################################################
#CONTRARIO  A OUTRA FUNCAO VOCE NAO PRECISA DE UM LSITA, JA QUE O MY_SUM ESTA JUNTANDO OS 3 VALORES EM UM OBJETO E ENVIANDO PARA *ARG
#PS: O NOME NAO NECESARIAMENTE PRECISA CHAMAR *ARG
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))
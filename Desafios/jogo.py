

## jogo python

##vida,resistencia, ataque, XP e lvl)
import random
import os
import time



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole() # use esse comando toda vez que quiser limpar o console

vida = 50
res = 1
exp = 0
lvl = 1
ataque= 5  
dinhero= 0        


print('informe seu nickname!')
nick = input()
clearConsole()

print('Seja bem vindo ' + nick)
print('Escolha sua arma: Espada, Machado, Clava')
tipoarma = input()
atqarma = random.randint(1,5)
print('sua arma é: ' + tipoarma + ' com ataque de ' + str(atqarma))
time.sleep(5)


##while jogo
while vida > 0 :  # se vida a ZERO fim de jogo

    qtdmonstros = random.randint(1,4)
    print(qtdmonstros)
    for rodada in range(qtdmonstros):
        print('montro' + str(rodada))

   #vida = vida - 10 ## aqui entra a funcao dos monstros


    bau = random.randint(0,100)
    if bau >= 70:
        print('voce encontrou um bau!')
        dinhero = random.randint(1, 20)
        print('voce encontrou: ' + str(dinhero) + ' Gold coins')

    dinhero = dinhero

    loja = random.randint(0,100)
    if loja >= 70:
        itens = random.randint(1,3)
        print(itens)
        print(nick + ' Voce encontrou o vendedor Dormamo')
        clearConsole
        print('Dormamo quer barganhar: ')
        if itens == 1:
            print('espada (20g): 1, potion(200g): 2')
        else:
            print('machado (20g): 1, potion(200g): 2')
            if itens == 2:
                print('Clava (20g): 1, potion(200g): 2')

        compra = input()

        #if compra == 1:
            
        
       # print(': ')
       # print('Armas: ')

    print('vida: ' + str(vida))
    print('gold coins: ' + str(dinhero))
    clearConsole
    
print(' voce morreu fim de jogo!!')

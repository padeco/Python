import limpa
from classes import Pessoa

limpa.clearConsole()

p1 = Pessoa('Manoel', 29)
p1.comer('maçã')
p1.falar('lemores anões do himalaia')
p1.parar_comer()
limpa.time.sleep(2)
p1.falar('lemores anões do himalaia')
p1.comer('maçã')
#print(p1.get_ano_nascimento())
p1.get_ano_nascimento()

p2 = Pessoa.por_ano_nascimento('Maria', 1990)
print(p2.nome, p2.idade)

class Animal:
    def __init__(self, especie, idade):
        self.especie = especie
        self.idade = idade
        
        
class Cachorro(Animal):
    def falar(self):
        print('au-au')
        
class Humano(Animal):
    def falar(self):
        print('Merda')
        
        
        
a1 = Cachorro('labrador', 15)
a2 = Humano('Jose', 75)

a2.falar()
a1.falar()
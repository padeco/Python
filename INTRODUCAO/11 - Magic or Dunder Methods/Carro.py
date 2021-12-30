import limpa

limpa.clearConsole()

class Carro:
    def __init__(self,marca, modelo, ano, potencia):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.potencia = potencia

    def Ligar(self):
        print ('tic-tic')
    
    def Som(self):
        print ('Vrummm')

    def Pneu(self):
        print ('tchururutchu')
    
    def Infos(self):
        print (self.marca,self.modelo,self.ano,self.potencia)

Tesla = Carro('Tesla', 'Model X', '2021', '200cv')
Tesla.Ligar()
Tesla.Som()
Tesla.Pneu()
Tesla.Infos()
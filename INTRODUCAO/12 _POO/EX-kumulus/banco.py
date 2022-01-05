
class Cliente:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo
         
    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor
        
    def extrato (self):
        print(f'{self.cliente:.<20}R$ {self.saldo}')
        
    


class Bradesco(Cliente):
    
    def tranferir(self, valor, destino):
        
        resultado = valor + ((valor * 0.05) + 5)

        if not isinstance(destino, Itau):
            print(f'{destino} não existe, favor inserir um banco valido!')

        elif destino.cliente == self.cliente:
            print('Transação cancelada, impossivel transferir para o mesmo cliente e conta.')

        elif resultado > self.saldo:
            print(f'Transferencia de R$ {resultado} com taxas, cancelada por saldo de ${self.saldo} ser insoficiente!')

        else:
            self.sacar(resultado)
            destino.depositar(valor)

class Itau(Cliente):

    def tranferir(self, valor, destino):
        resultado = valor + (valor * 0.01)

        if not isinstance(destino, Bradesco):
            print(f'{destino} não existe, favor inserir um banco valido!')
        elif destino.cliente == self.cliente:
            print('Não é possível fazer a transação para o mesmo desconta.')

        elif resultado > self.saldo:
            print(f'Transferencia de R$ {resultado} com taxas, cancelada por saldo de ${self.saldo} ser insoficiente!')

        else:
            self.sacar(resultado)
            destino.depositar(valor)


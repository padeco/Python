from banco import *
import limpa

limpa.clearConsole()

bradesco = Bradesco('Fulano', float(10000))
itau = Itau('Ciclano', float(5000))

itau.tranferir(5000, bradesco)
itau.extrato()
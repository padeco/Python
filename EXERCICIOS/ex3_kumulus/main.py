from banco import *

c1 = Itau('Manoel', 2500)
c2 = Bradesco('Filipe', 1000)


c1.tranferir(3000, c2)
c1.extrato()

c2.tranferir(150, c1)
c2.extrato()

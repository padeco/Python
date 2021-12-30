import os
import time
import random

class Funcoes:
    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
    #####################################################################################





    def menu(self):
        saida = ''
        contador = 11
        while saida == '':
            contador -= 1
            self.clearConsole()
            print('''                                                                                              
                                                                                                    
          `7MMF'                     `7MM                                                            
            MM                         MM                                                            
            MM   ,6"Yb.  `7MMpMMMb.    MM  ,MP' .gP"Ya  `7MMpMMMb.  `7MMpdMAo.  ,pW"Wq.  `7MMpMMMb.  
            MM  8)   MM    MM    MM    MM ;Y   ,M'   Yb   MM    MM    MM   `Wb 6W'   `Wb   MM    MM  
            MM   ,pm9MM    MM    MM    MM;Mm   8M""""""   MM    MM    MM    M8 8M     M8   MM    MM  
       (O)  MM  8M   MM    MM    MM    MM `Mb. YM.    ,   MM    MM    MM   ,AP YA.   ,A9   MM    MM  
        Ymmm9   `Moo9^Yo..JMML  JMML..JMML. YA. `Mbmmd' .JMML  JMML.  MMbmmd'   `Ybmd9'  .JMML  JMML.
                                                                      MM                             
                                                                    .JMML.                           ''')
            if contador <1 :
                break
            
            print(f'Carregando... {contador}')
            time.sleep(1)
                
        
            
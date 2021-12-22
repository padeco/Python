import emoji
import os
import time
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()


message = emoji.emojize('Howdy :sun_with_face:')
print(emoji.emojize("Python é :polegar_para_cima:", language='pt'))
print(message)
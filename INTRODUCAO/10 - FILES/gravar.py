import limpa

limpa.clearConsole()


with open('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\INTRODUCAO\\#10 - FILES\\dog_breeds.txt', 'r') as reader:
    dogs = reader.readlines()

with open('C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\INTRODUCAO\\#10 - FILES\\dog_breeds.txt', 'w') as escrita:

    for breed in reversed(dogs):
        escrita.write(breed)

# É POSSIVEL TRABALHAR COM 2 ARQUIVOS OU MAIS
d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))

class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()
# Métodos adicionais implementados abaixo
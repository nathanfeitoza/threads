from threading import Thread
from random import randrange
import time

class Lista():
    def __init__(self):
        self.__lista = [1,2,3,4,5,6,7,8,9]
        self.__modificando = False

    def ler(self):
        if(self.__modificando == False):
            print('A lista está sendo modificada \n')
        else:
            print('Lista')
            print(self.__lista)

    def moficiar(self, tipo, addRemove):
        self.__modificando = True
        print('\nModificando... \n')
        if(tipo == 1):
            self.__lista.append(addRemove)
            print('Inserido: ',addRemove,'\n')
        else:
            self.__lista.remove(addRemove)
            print('Removido: ', addRemove,'\n')

        time.sleep(5)
        self.__modificando = False

lista = Lista()

for x in range(10, 20):
    threadLer = Thread(target=lista.ler())
    threadLer.start()

    modificao = randrange(1,2)
    threadAlterar = Thread(target=lista.moficiar, args=[modificao, x])
    threadAlterar.start()

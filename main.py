from threading import Thread
import time

'''
decolando = 0
pousando = 0
esperandoPousar = []
esperandoDecolar = []

def decolar(aviao):
    decolandoAviao = 0
    while(decolandoAviao <= 100):
        print('Decolando aviao: ', aviao)
        decolandoAviao += 1
    decolando = 0
    print('Finalizou decolagem aviao: ',aviao)

def pousar(aviao):
    pousandoAviao = 0
    while(pousandoAviao <= 100):
        print('Decolando aviao: ', aviao)
        pousandoAviao += 1
    pousando = 0
    print('Finalizou pouso aviao: ',aviao)

def aviao(id, acao):
    executando = 0
    liberar = decolando == 0 and pousando == 0 and esperandoDecolar == 0 and esperandoPousar == 0
    if(acao == "decolar"):
        if(liberar):
            decolar(id)
            time.sleep(0.5)
        else:
            print('Esperando decolar: ',id)
            esperandoDecolar.append(id)
    elif(acao == "pousar"):
        if(liberar):
            pousar(id)
        else:
            print('Esperando pousar: ',id);
            esperandoPousar.append(id)
'''
#def carrinho(velocidade,nome):
    #distancia = 0
    #while distancia <= 1000:
        #print("Carrinho :",nome,distancia)
        #distancia += velocidade
        #time.sleep(0.3)


class Aeroporto():
    def __init__(self):
        self.__decolando = 0
        self.___pousando = 0
        self.__esperando_pousar = 0
        self.__esperando_decolar = 0

    def decolar(self, aviao):
        if(self.__decolando == 0 and self.___pousando == 0):
            print('decolar Ok')

    def pousar(self, aviao):
        if(self.__decolando == 0 and self.)

aeroporto = Aeroporto()

aviao1 = Thread(target=aeroporto.decolar,args=["decolar"])
#aviao2 = Thread(target=aviao,args=[2,"pousar"])


aviao1.start()
#aviao2.start()
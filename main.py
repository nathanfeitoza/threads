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


class Aviao():
    def __init__(self):
        self.__decolou = 0
        self.__pousou = 0
        self.__decolando = 0
        self.___pousando = 0
        self.__esperando_pousar = []
        self.__esperando_decolar = []
        self.__excedente_pousar = []
        self.__excedente_decolar = []

    def decolar(self, aviao):
        print('Decolaram: ',self.__decolou)
        if(self.__decolando == 0 and self.___pousando == 0):
            self.__decolando = 1
            print('decolagem Ok. Aviao: ', aviao)
            self.__decolou += 1
            time.sleep(5)
            if(aviao in self.__esperando_decolar):
                self.__esperando_decolar.remove(aviao)
            self.__decolando = 0
        else:
            print('\n\n -- Lista esperando decolar: ',self.__esperando_decolar)

            if len(self.__esperando_decolar) <= 5 and (aviao in self.__esperando_decolar) == False:
                self.__esperando_decolar.append(aviao)

            if len(self.__esperando_decolar) >= 6 and (aviao in self.__excedente_decolar) == False:
                print('\n -- Excendente de decolagem --. Aviao: ', aviao,'\n')
                self.__excedente_decolar.append(aviao)
            if len(self.__esperando_decolar) == 0 and len(self.__excedente_decolar) != 0:
                self.__esperando_decolar = self.__excedente_decolar[:6]
                self.__excedente_decolar = self.__excedente_decolar[6:]

            print('Aguardando decolar. Aviao: ', aviao)
            time.sleep(2)
            self.decolar(aviao)

    def pousar(self, aviao):
        print('Pousaram: ', self.__pousou)
        if(self.__decolando == 0 and self.___pousando == 0):
            self.___pousando = 1
            print('pouso ok. Aviao: ',aviao)
            self.__pousou += 1
            time.sleep(5)
            if (aviao in self.__esperando_pousar):
                self.__esperando_pousar.remove(aviao)
            self.___pousando = 0
        else:
            print('\n\n -- Lista esperando pousar: ',self.__esperando_pousar)

            if len(self.__esperando_pousar) <= 2 and (aviao in self.__esperando_pousar) == False:
                self.__esperando_pousar.append(aviao)

            if len(self.__esperando_pousar) >= 3 and (aviao in self.__excedente_pousar) == False:
                print('\n -- Excendente de pouso --. Aviao: ', aviao,'\n')
                self.__excedente_pousar.append(aviao)
            if len(self.__esperando_pousar) == 0 and len(self.__excedente_pousar) != 0:
                self.__esperando_pousar = self.__excedente_pousar[:3]
                self.__excedente_pousar = self.__excedente_pousar[3:]

            print('Aguardando pousar. Aviao: ', aviao)
            time.sleep(2)
            self.pousar(aviao)

pista = Aviao()

for i in range(10):
    aviao_id = i + 1
    aviaoD = Thread(target=pista.decolar, args=[aviao_id])
    aviaoD.start()

for i in range(10):
    aviao_id = i + 1
    aviaoP = Thread(target=pista.pousar, args=[aviao_id])
    aviaoP.start()

#aviao1 = Thread(target=pista.decolar,args=[1])
#aviao2 = Thread(target=pista.pousar,args=[2])


#aviao1.start()
#aviao2.start()
from threading import Thread
import time

class Cliente():
    def __init__(self, cliente_id):
        self.__cliente_id = cliente_id

    def getClienteId(self):
        return self.__cliente_id

class Loja():
    def __init__(self):
        self.__caixa_dormiu = False
        self.__atendendo = False
        self.__fila_clientes = []

    def addCliente(self, cliente):
        if(len(self.__fila_clientes) <= 10):
            self.__fila_clientes.append(cliente.getClienteId())
        else:
            print('Cliente ', cliente.getClienteId(), 'foi embora')

    def pagamento(self, cliente):
        if(len(self.__fila_clientes) == 0):
            self.__caixa_dormiu = True
        else:
            if cliente.getClienteId() in self.__fila_clientes:
                self.__caixa_dormiu = False
                print('Recebendo pagamento do cliente: ', cliente.getClienteId())
                time.sleep(10)
                self.__fila_clientes.remove(cliente.getClienteId())
                print('Recebido pagamento do cliente: ', cliente.getClienteId())


terminar = True
loja = Loja()

while(terminar):
    cliente = input('Cliente: ')
    if(cliente == '-1'):
        terminar = False
    else:
        clienteObj = Cliente(cliente)

        addCliente = Thread(target=loja.addCliente, args=[clienteObj])
        pagamento = Thread(target=loja.pagamento, args=[clienteObj])

        addCliente.start()
        pagamento.start()




class node:
    def __init__(self, data, nex_node=None):
        self.data = data
        self.next = nex_node

class circle_list:
    
    def __init__(self):
        self.cab = node('raiz')
        self.cab.next = self.cab
    def addNode(self,data):
        last_node = self.search_last()
        last_node.next = node(data,self.cab)

    def search_last(self):
        q = self.cab.next
        while q.next != self.cab:
            q = q.next;   
        return q
    def print_all(self):
        q = self.cab
        i = 0
        print('Nodos en la lista:')
        print(f'index:{i} --- contenido:{q.data}')
        while q.next != self.cab:
            i += 1
            q = q.next
            print(f'index:{i} --- contenido:{q.data}')

if __name__ == '__main__':
    switch = 1
    mlist = circle_list() 
    while switch != 0:
        print('Bienvenido a la lista circular!!\n')
        switch = int(input('Seleccione una opción para continuar:\n 0. salir.\n 1. Insertar un nodo \n 2. Imprimir contenido'))
        if switch == 1 :
            message = input('Ingrese el contenido del nodo:')
            mlist.addNode(message)
        elif switch == 2 :
            mlist.print_all()

        
    

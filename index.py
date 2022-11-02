class node:
    def __init__(self, name, trade, nex_node=None):
        self.name = name
        self.trade = trade
        self.next = nex_node

class circle_list:
    
    def __init__(self):
        self.cab = node('raiz',0)
        self.cab.next = self.cab
    def addNode(self,name, trade):
        last_node = self.search_last()
        last_node.next = node(name, trade, self.cab)

    def search_last(self):
        q = self.cab.next
        while q.next != self.cab:
            q = q.next;   
        return q
    def print_all(self):
        q = self.cab
        i = 0
        print('Nodos en la lista:')
        print(f'index:{i} --- titular:{q.name}')
        while q.next != self.cab:
            i += 1
            q = q.next
            print(f'index:{i} --- nombre:{q.name} ---- transacciones: {q.trade}')
    def checkTail(self):
        if self.cab.next != self.cab:
            q = self.cab.next
            self.cab.next = self.cab.next.next
            if (q.trade > 5):
                q.trade -= 5
                q.next = self.cab
                lastItem = self.search_last()
                lastItem.next = q
            else: 
                del q;

if __name__ == '__main__':
    switch = 1
    mlist = circle_list() 
    mlist.addNode('name1',5)
    mlist.addNode('name2',2)
    mlist.addNode('name3',6)
    mlist.addNode('name4',8)
    mlist.addNode('name5',5)
    print('Bienvenido a la lista circular!!\n')
    while switch != 0:
        switch = int(input('Seleccione una opción para continuar:\n 0. salir.\n 1. Insertar un nodo \n 2. Imprimir contenido \n 3. Atenter cola\n'))
        if switch == 1 :
            name = input('Ingrese el nombre del titular de la cuenta:\n')
            trade = input('Ingrese el numero de transacciones arealizar:\n')
            mlist.addNode(name,trade)
        elif switch == 2 :
            mlist.print_all()
        elif switch == 3 :
            mlist.checkTail()

        
    

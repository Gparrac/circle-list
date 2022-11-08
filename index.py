from tkinter import *
from tkinter import ttk
import threading

import time 
class node:#creamos estructura nodo
    def __init__(self, name, trade, frame=None, nex_node=None):
        self.name = StringVar(value=name)
        self.trade = IntVar(value=trade)
        self.next = nex_node
        if self.next != None and frame != None:
            self.set_label(frame)
    def set_label(self, frame):#validador para nodo raiz
        self.card=LabelFrame(frame,text=self.name.get(),background="#2c2c2c",fg='white', width=700, height=300, relief="groove")
        self.card.pack(pady=10,padx=10,ipadx=500,ipady=0)
        Label(self.card,text="Número de transacciones:", background="#2c2c2c", fg='lightblue').pack(side=LEFT)
        Label(self.card,textvariable=self.trade, background="#2c2c2c", fg='lightblue').pack()
class circle_list:
    
    def __init__(self,window):
        #Interfaz - frames base
        self.window = window
        self.frame_register=Frame(window, width=300,height=400, background="lightblue")
        self.frame_register.pack(side='left',fill=Y, expand=0) 
        self.frame_tail = Frame(window, width=500,height=400, background="#2c2c2c")
        self.frame_tail.pack(side="right",fill=Y, expand=0,pady=10,padx=10,ipadx=500,ipady=0)  
        Label(self.frame_tail,text="Cola",background="#2c2c2c",fg="lightblue" ,font=("Arial",30)).pack(fill="x",pady=20)
        
        
        #variables
        self.cab = node('raiz',0)
        self.cab.next = self.cab
        self.name = StringVar()
        self.trades = IntVar()
        self.error = StringVar()
        self.max_count = 0

        
        #formulario
        Label(self.frame_register,text="Nuevo cliente",background="lightblue", font=("Arial",30)).pack(fill="x",pady=(20,50))
        Label(self.frame_register,text="Nombre del titular",background="lightblue").pack(fill="x")
        Entry(self.frame_register, textvariable=self.name).pack()
        Label(self.frame_register,text="Numero de turnos",background="lightblue").pack()
        Entry(self.frame_register, textvariable=self.trades).pack()
        Label(self.frame_register,textvariable=self.error,background="lightblue").pack()
        Button(self.frame_register, text="Aceptar",background="black",fg="lightblue", command=self.addNode).pack()
        
    def addNode(self):
        if self.name.get() != '' and self.trades.get() > 0 :
            self.error.set(value='')
            last_node = self.search_last()
            last_node.next = node(self.name.get(), self.trades.get(),self.frame_tail, self.cab)  
        else:
            self.name.set(value='')
            self.trades.set(value=0)
            self.error.set(value='Verifique los campos')

    def search_last(self):
        q = self.cab.next
        while q.next != self.cab:
            q = q.next;   
        return q

    def check_tail(self):
        if self.cab.next != self.cab:
            q=self.cab.next
            if q.trade.get()>0 and self.max_count < 5:
                q.trade.set(q.trade.get()-1)
                self.max_count += 1
            
            elif q.trade.get() == 0:
                q.card.destroy()
                self.max_count = 0                    
                self.cab.next = self.cab.next.next                
                del q
            else:
                q.card.destroy()
                self.max_count = 0
                q.card.destroy()  
                q.set_label(self.frame_tail)
                self.cab.next = self.cab.next.next                
                q.next = self.cab
                lastItem = self.search_last()
                lastItem.next = q
            time.sleep(1)  
        self.window.after(1000,self.check_tail)
    def check_tail_before(self):
        t = threading.Thread(target=self.check_tail)
        t.start()
        self.check_cicle(t)
    def check_cicle(self,t):
        self.window.after(1000,self.check_hilo,t)
    def check_hilo(self,t):
        if t.is_alive():
            self.window.after(1000,self.check_hilo,t)



if __name__ == '__main__':
    window = Tk()
    window.geometry('800x600')
    aplication = circle_list(window)
    aplication.name.set(value='Oscar')
    aplication.trades.set(value=6)
    aplication.addNode()
    aplication.name.set(value='David')
    aplication.trades.set(value=3)
    aplication.addNode()
    aplication.name.set(value='Laura')
    aplication.trades.set(value=5)
    aplication.addNode()  
    window.after(1000,aplication.check_tail_before)
    window.mainloop()
        
    

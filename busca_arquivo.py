import os
from tkinter import *
from tkinter import ttk

root=Tk()

class Funcoes():
    def endereco(self):
        lista =os.listdir(self.entr_caminho.get())
        elemento =self.entr_busca.get()
        valida = (elemento in lista)
      #  indice = lista.index(elemento)  falta ajustar esta parte
      #  if valida == True:
      #      self.lb_mostra.


class Aplicacao(Funcoes):
    def __init__(self):
        self.root=root
        self.Tela()
        self.Frame()
        self.Botao()
        root.mainloop()
    def Tela(self):
        self.root.title('Buscador')
        self.root.configure(background='#87CEFA')
        self.root.geometry('500x300')
        self.root.resizable(False, False)
    def Frame(self):
        self.Main=Frame(self.root,bg= '#87CEFA',highlightbackground='#759fe6', highlightthickness=1)
        self.Main.place(relx= 0.01, rely=0.01, relwidth= 0.98, relheight=0.98)
    def Botao(self):
        self.Bt_Procura = Button(self.Main, text='Procurar',command=self.endereco)
        self.Bt_Procura.place(relx=0.87, rely=0.15)

        self.entr_caminho=Entry(self.Main)
        self.entr_caminho.place(relx=0.01, rely=0.16, relwidth=0.50, relheight=0.08)

        self.lb_mostra(self.Main)
        self.lb_mostra.place(relx=0.01, rely=0.30, relwidth=0.98, relheight=0.75)

        self.entr_busca=Entry(self.Main)
        self.entr_busca.place(relx=0.55, rely=0.16,relwidth=0.30, relheight=0.08)
Aplicacao()
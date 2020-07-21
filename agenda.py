from tkinter import *
from tkinter import ttk
import sqlite3

root=Tk()

class Funçoes():
    def Novo(self):
        print('Novo')
    def Procura(self):
        print('Procurar')
    def Exibir(self):
        print('Exibindo')
    def Notas(self):
        print('Atualizando')
class Aplicacao(Funçoes):
    def __init__(self):
        self.root=root
        self.Tela()
        self.Frame()
        self.Widget()
        self.Menus()
        root.mainloop()
    def Tela(self):
        self.root.title('Agenda')
        self.root.configure(background='#87CEFA')
        self.root.geometry('700x500')
        self.root.resizable(False,False)
    def Frame(self):
        self.Main=Frame(self.root,bg= '#87CEFA',highlightbackground='#759fe6', highlightthickness=1)
        self.Main.place(relx= 0.01, rely=0.01, relwidth= 0.98, relheight=0.98)
    def Widget(self):
        self.Bt_Novo=Button(self.Main,text='Novo',command=self.Novo)
        self.Bt_Novo.place(relx=0.01, rely=0.10)

        self.Bt_Procura = Button(self.Main, text='Procurar',command=self.Procura)
        self.Bt_Procura.place(relx=0.01, rely=0.20)

        self.Bt_exibe=Button(self.Main, text='Contatos',command=self.Exibir)
        self.Bt_exibe.place(relx=0.01, rely=0.30)
    def Menus(self):
        manubar=Menu(self.root)
        self.root.config(menu=manubar)
        Menu1=Menu(manubar)
        def Quit(): self.root.destroy()
        manubar.add_cascade(label='Opçoes',menu=Menu1)
        Menu1.add_command(label='Notas da atualizaçao',command=self.Notas)
        Menu1.add_command(label='Sair',command=Quit)

Aplicacao()
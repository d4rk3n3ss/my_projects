import os
from tkinter import *
import shutil as sh


root=Tk()

class Funcoes():
    def buscar(self):
        lista =os.listdir(self.entr_caminho.get())
        elemento =self.entr_busca.get()
        valida = (elemento in lista)
        if valida ==False:
            self.lb_mostra['text']=('Arquivo nao localizado no diretorio')

        indice = lista.index(elemento)
        try:
            if valida ==True:
                self.lb_mostra['text']=str(indice)+('  -  ')+(elemento)
                self.bt_abrir = Button(self.Main, text="Copiar", command=self.Copiar)
                self.bt_abrir.place(relx=0.88, rely=0.50, relwidth=0.10)
                #self.entr_caminho.delete(0,END)
                # deleta os dados digitado
                #self.entr_busca.delete(0,END)
        except:
            self.lb_mostra['text'] = ('Verifque os se os dados digitados estao corretos')
    def Copiar(self):
        sh.copyfile(self.entr_caminho.get()+'/'+self.entr_busca.get(),self.entr_busca.get()+'alt.txt')
class Aplicacao(Funcoes):
    def __init__(self):
        self.root=root
        self.Tela()
        self.Frame()
        self.Botao()
        self.Menus()
        root.mainloop()
    def Tela(self):
        self.root.title('Buscador')
        self.root.configure(background='#000000')
        self.root.geometry('500x300')
        self.root.resizable(False, False)
    def Frame(self):
        self.Main=Frame(self.root,bg= '#0000FF',highlightbackground='#759fe6')
        self.Main.place(relx= 0.01, rely=0.01, relwidth= 0.98, relheight=0.98)
    def Botao(self):
        self.Bt_Procura = Button(self.Main, text='Procurar',command=self.buscar)
        self.Bt_Procura.place(relx=0.87, rely=0.15)

        self.entr_caminho=Entry(self.Main)
        self.entr_caminho.place(relx=0.01, rely=0.16, relwidth=0.50, relheight=0.08)

        self.lb_mostra=Label(self.Main,text='Nada a mostrar',bg= '#EFFBFB')
        self.lb_mostra.place(relx=0.01, rely=0.30, relwidth=0.85, relheight=0.65)

        self.entr_busca=Entry(self.Main)
        self.entr_busca.place(relx=0.55, rely=0.16,relwidth=0.30, relheight=0.08)
    def Menus(self):
        manubar = Menu(self.root)
        self.root.config(menu=manubar)
        filemenu = Menu(manubar)
        def Quit(): self.root.destroy()
        manubar.add_cascade(label='Opçoes', menu=filemenu)
        filemenu.add_command(label='Sair', command=Quit)
Aplicacao()
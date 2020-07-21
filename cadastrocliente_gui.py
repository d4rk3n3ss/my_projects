from tkinter import *
from tkinter import ttk
import sqlite3
import random
import string
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
from PIL import ImageTk, Image

root = Tk()

class relatorios():
    def pintcliente(self):
        webbrowser.open("Clientes.pdf")
    def gerarrelatorio(self):
        num=str(random.randrange(0,100000))
        self.c =canvas.Canvas('Clietes'+num+'.pdf')
        self.codigorel= self.codigo_entry.get()
        self.nomerel=self.nome_entry.get()
        self.fonerel=self.fone_entry.get()
        self.cidaderel=self.cidade_entry.get()

        self.c.setFont('Helvetica-Oblique',24)
        self.c.drawString(200,790,'Ficha do Cliente')

        self.c.drawString(50, 690,'Codigo:' + self.codigorel)
        self.c.drawString(50, 660, 'Nome:' + self.nomerel)
        self.c.drawString(50, 630, 'Telefone:' + self.fonerel)
        self.c.drawString(50, 600, 'Cidade:' + self.cidaderel)
        self.c.rect(20,580,550,150,fill=False,stroke=True)

        self.c.showPage()
        self.c.save()
        self.pintcliente()
class Funcs():
    def limpa_cliente(self):
        self.codigo_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.nome_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")
    def montaTabelas(self):
        self.conecta_bd()
        ### Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)               
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
    def OnDoubleClick(self, event):
        self.limpa_cliente()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_cliente()
        self.select_lista()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
    def alterar_clientes(self):
        self.variaveis()
        self.conecta_bd()
        self.conn.execute('''UPDATE clientes set nome_cliente=?,telefone=?,cidade=? where cod=?''',(self.nome,self.fone,self.cidade,self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def Busca_Cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END,'%')
        nome=self.nome_entry.get()
        self.cursor.execute('''
        select cod,nome_cliente,telefone,cidade from clientes where nome_cliente like '%s' ORDER BY nome_cliente asc'''% nome)
        buscanomecli=self.cursor.fetchall()
        for i in buscanomecli:
            self.listaCli.insert("",END,values=i)
        self.limpa_cliente()
        self.desconecta_bd()
class Application(Funcs,relatorios):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= '#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        #self.root.maxsize(width= 900, height= 700)
        self.root.minsize(width=500, height= 400)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg= '#dfe3ee',
                             highlightbackground= '#759fe6', highlightthickness=3 )
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def widgets_frame1(self):
        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame_1, text= "Limpar", bd=2, bg = '#107db2',fg = 'white',activebackground='black',activeforeground='red', font = ('verdana', 8, 'bold'), command= self.limpa_cliente)
        self.bt_limpar.place(relx= 0.2, rely=0.1, relwidth=0.1, relheight= 0.15)
        ### Criação do botao buscar
        self.bt_Buscar = Button(self.frame_1, text="Buscar", bd=2, bg = '#107db2',fg = 'white',activebackground='black',activeforeground='red'
                                , font = ('verdana', 8, 'bold'),command=self.Busca_Cliente)
        self.bt_Buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao novo
        self.bt_Novo = Button(self.frame_1, text="Novo", bd=2, bg = '#107db2',fg = 'white',activebackground='black',activeforeground='red'
                                , font = ('verdana', 8, 'bold'), command= self.add_cliente)
        self.bt_Novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao alterar

        self.imgnova=PhotoImage(file='bt_teste.gif')
        self.imgnova=self.imgnova.subsample(2,2)
        self.stylo=ttk.Style()
        self.stylo.configure('Bw.TButton', relwidth=1,relheight=1,image=self.imgnova)

        self.bt_Alterar =ttk.Button (self.frame_1,style='Bw.TButton', command=self.alterar_clientes) #text="Alterar", bd=2, bg = '#107db2',fg = 'white',activebackground='black',activeforeground='red', font = ('verdana', 8, 'bold')
        self.bt_Alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_Alterar.configure(image=self.imgnova)

        ### Criação do botao apagar
        self.bt_Apagar = Button(self.frame_1, text="Apagar", bd=2, bg = '#107db2',fg = 'white',activebackground='black',activeforeground='red'
                                , font = ('verdana', 8, 'bold'), command=self.deleta_cliente)
        self.bt_Apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ## Criação da label e entrada do codigo
        self.lb_codigo = Label(self.frame_1, text = "Código", bg= '#dfe3ee', fg = '#107db2')
        self.lb_codigo.place(relx= 0.05, rely= 0.05 )

        self.codigo_entry = Entry(self.frame_1 )
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08)

        ## Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text="Nome", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        ## Criação da label e entrada do telefone
        self.lb_nome = Label(self.frame_1, text="Telefone", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.05, rely=0.6)

        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        ## Criação da label e entrada da cidade
        self.lb_nome = Label(self.frame_1, text="Cidade", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3,
                                     column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
    def Menus(self):
        manubar=Menu(self.root)
        self.root.config(menu=manubar)
        filemenu=Menu(manubar)
        filemenu2=Menu(manubar)
        filemenu3=Menu(manubar)
        def Quit(): self.root.destroy()
        manubar.add_cascade(label='Opçoes',menu=filemenu)
        manubar.add_cascade(label='Sobre',menu=filemenu2)
        manubar.add_cascade(label='Desenvolvedor',menu=filemenu3)

        filemenu.add_command(label='Relatorio',command=self.gerarrelatorio)
        filemenu.add_command(label='Sair',command=Quit)
        filemenu3.add_command(label='Contato')
        filemenu2.add_command(label='Duvidas sobre o sistema')

Application()
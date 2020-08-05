from tkinter import *
from tkinter import ttk
from time import strftime
import sqlite3
from tkcalendar import Calendar,DateEntry



root=Tk()

class Validadores():
    def ValidaHora(self,text):
        if text=="": return True
        try:
            value=int(text)
        except ValueError:
            return False
        return 0 <= value <=10000

    def ValidaTele(self,text):
        if text=="":return True
        try:
            value=int(text)
        except (ValueError):
            return False
        return 0 <= value <=1000000000

class Funçoes(Validadores):
    def conecta_bd(self):
        self.conn = sqlite3.connect("AGENDAMENTOS.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")
    def montaTabelas(self):
        self.conecta_bd()
        ### Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Agendas (
                COD INTEGER PRIMARY KEY,
                NOME_CLIENTE CHAR(40) NOT NULL,
                TELEFONE INTEGER(20),
                DATA date,
                HORA time              
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def Calendario(self):
        self.cal=Calendar(self.Main,fg='black',locale='pt_br')
        self.cal.place(relx=0.66, rely=0.01)
        self.btsalva=Button(self.Main,text='Salvar',command=self.Salvar,bg='#00FF7F')
        self.btsalva.place(relx=0.66, rely=0.33,relwidth=0.32)
    def Agendar(self):
        self.conecta_bd()
        self.montaTabelas()
        self.entrynome=Entry(self.Main)
        self.entrynome.place(relx=0.25, rely=0.10,relwidth=0.40)
        self.lbnome=Label(self.Main,text='Nome',background='white')
        self.lbnome.place(relx=0.15, rely=0.10)

        self.entrytele=Entry(self.Main,validate='key',validatecommand=self.vdTele)
        self.entrytele.place(relx=0.25, rely=0.20, relwidth=0.40)
        self.lbtele = Label(self.Main, text='Telefone', background='white')
        self.lbtele.place(relx=0.15, rely=0.20)

        self.entryhora=Entry(self.Main,validate='key',validatecommand=self.vdhora)
        self.entryhora.place(relx=0.25, rely=0.30, relwidth=0.05)
        self.lbhora=Label(self.Main,text='Hora',background='white')
        self.lbhora.place(relx=0.15, rely=0.30)

        self.entrydata=Entry(self.Main)
        self.entrydata.place(relx=0.40, rely=0.30,relwidth=0.10)
        self.lbdata=Label(self.Main,text='Data',background='white')
        self.lbdata.place(relx=0.35, rely=0.30)


        self.bt_calendario=Button(self.Main,text='Calendario',command=self.Calendario)
        self.bt_calendario.place(relx=0.55, rely=0.30)
    def Salvar(self):
        dataini=self.cal.get_date()
        self.entrydata.delete(0,END)
        self.entrydata.insert(END,dataini)
        self.conecta_bd()
        self.conn.execute('''
        insert into Agendas (NOME_CLIENTE,TELEFONE,DATA,HORA) values (?,?,?,?)''',(self.entrynome.get(),self.entrytele.get(),self.entrydata.get(),self.entryhora.get()))
        self.conn.commit()
        self.desconecta_bd()
        self.entrynome.destroy()
        self.lbnome.destroy()
        self.entryhora.destroy()
        self.lbhora.destroy()
        self.entrytele.destroy()
        self.lbtele.destroy()
        self.entrydata.destroy()
        self.lbdata.destroy()
        self.bt_calendario.destroy()
        self.btsalva.destroy()
        self.cal.destroy()
        self.Tarefas()
    def OnDoubleClick(self, event):
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1,col2, col3, col4,col5 = self.listaCli.item(n, 'values')
            self.entrynome.insert(END, col2)
            self.entrytele.insert(END, col3)
            self.entrydata.insert(END, col4)
            self.entryhora.insert(END, col5)
    def Tarefas(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        dia=self.data_e_hora=strftime('%d/%m/%Y')
        lista=self.conn.execute('''
       SELECT * FROM Agendas where data like ('%s')ORDER BY NOME_CLIENTE ASC'''% dia)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
    def VerMes(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        meses = self.data_e_hora = strftime('/%m/%Y')
        mes=('%')+meses
        lista = self.conn.execute('''
        SELECT * FROM Agendas where data like ('%s')ORDER BY data ASC''' % mes)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
    def Notas(self):
        print('Atualizando')
    def Validaentrada(self):
        self.vdhora=(self.root.register(self.ValidaHora),"%P")
        self.vdTele=(self.root.register(self.ValidaTele),"%P")
class Aplicacao(Funçoes,Validadores):
    def __init__(self):
        self.root=root
        self.Validaentrada()
        self.Tela()
        self.Frame()
        self.Widget()
        self.Menus()
        self.lista_frame()
        root.mainloop()
    def Tela(self):
        self.root.title('Agenda')
        self.root.configure(background='black')
        self.root.geometry('800x600')
        self.root.resizable(False,False)
    def Frame(self):
        self.Main=Frame(self.root,bg= 'white',highlightbackground='black')
        self.Main.place(relx= 0.01, rely=0.01, relwidth= 0.98, relheight=0.98)
        self.Main1=Frame(self.root,bg= 'black')
        self.Main1.place(relx= 0.15, rely=0.40, relwidth= 0.80, relheight=0.45)
    def Widget(self):
        self.bt_imgagn=PhotoImage(file='agenda.png')
        self.bt_imgagn=self.bt_imgagn.subsample(4,4)
        self.stylo=ttk.Style()
        self.stylo.configure('Bw.TButton',image=self.bt_imgagn,background='white',foreground='white',bordercolor='white')
        self.Bt_Novo=ttk.Button(self.Main,style='Bw.TButton',command=self.Agendar)
        self.Bt_Novo.place(relx=0.01, rely=0.10,relwidth=0.10,relheight=0.15)
        self.Bt_Novo.configure(image=self.bt_imgagn)

        self.bt_imgtaref=PhotoImage(file='tarefas.png')
        self.bt_imgtaref=self.bt_imgtaref.subsample(4,4)
        self.stylo=ttk.Style()
        self.stylo.configure('Bw.TButton',image=self.bt_imgtaref)
        self.Bt_tarefa =ttk.Button(self.Main,command=self.Tarefas)
        self.Bt_tarefa.place(relx=0.01, rely=0.35,relwidth=0.10,relheight=0.15)
        self.Bt_tarefa.configure(image=self.bt_imgtaref)

        self.bt_imgmes=PhotoImage(file='mes.png')
        self.bt_imgmes=self.bt_imgmes.subsample(4,4)
        self.stylo=ttk.Style()
        self.stylo.configure('Bw.TButton',image=self.bt_imgmes)
        self.Bt_exibe=ttk.Button(self.Main,command=self.VerMes)
        self.Bt_exibe.place(relx=0.01, rely=0.60,relwidth=0.10,relheight=0.15)
        self.Bt_exibe.configure(image=self.bt_imgmes)

        self.lb_relogio = Label(self.Main,background='white',font = ('verdana',12))
        self.lb_relogio.place(relx=0.40, rely=0.85,relwidth=0.25, relheight=0.08)

        def tic():
            self.data_e_hora = strftime('%d/%m/%y %H:%M')
            self.lb_relogio['text'] = (self.data_e_hora)
        def tac():
            tic()
            self.lb_relogio.after(1000,tac)
        tac()
    def Menus(self):
        manubar=Menu(self.root)
        self.root.config(menu=manubar)
        Menu1=Menu(manubar)
        def Quit(): self.root.destroy()
        manubar.add_cascade(label='Opçoes',menu=Menu1)
        Menu1.add_command(label='Notas da atualizaçao',command=self.Notas)
        Menu1.add_command(label='Sair',command=Quit)

    def lista_frame(self):
        self.listaCli = ttk.Treeview(self.Main1, height=3,
                                     column=("col1", "col2", "col3", "col4","col5"))
        self.listaCli.heading("#0",text="")
        self.listaCli.heading("#1", text="C")
        self.listaCli.heading("#2", text="NOME")
        self.listaCli.heading("#3", text="TELEFONE")
        self.listaCli.heading("#4", text="DATA")
        self.listaCli.heading("#5", text="HORA")
        self.listaCli.column("#0",width=0)
        self.listaCli.column("#1", width=0)
        self.listaCli.column("#2", width=40)
        self.listaCli.column("#3", width=10)
        self.listaCli.column("#4", width=10)
        self.listaCli.column("#5", width=10)
        self.listaCli.place(relx=0.0001, rely=0.001, relwidth=0.96, relheight=1)

        self.scroolLista = Scrollbar(self.Main1, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.001, relwidth=0.04, relheight=1)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

Aplicacao()
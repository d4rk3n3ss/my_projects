from tkinter import *
from tkinter import ttk
from time import strftime
import sqlite3
from tkcalendar import Calendar,DateEntry



root=Tk()

class Funçoes():
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
        self.cal.place(relx=0.55, rely=0.30)
        self.btsalva=Button(self.Main,text='Salvar',command=self.Salvar)
        self.btsalva.place(relx=0.45, rely=0.45)
    def Agendar(self):
        self.conecta_bd()
        self.montaTabelas()
        self.entrynome=Entry(self.Main)
        self.entrynome.place(relx=0.40, rely=0.10,relwidth=0.40)
        self.lbnome=Label(self.Main,text='Nome',background='white')
        self.lbnome.place(relx=0.30, rely=0.10)

        self.entrytele=Entry(self.Main)
        self.entrytele.place(relx=0.40, rely=0.20, relwidth=0.40)
        self.lbtele = Label(self.Main, text='Telefone', background='white')
        self.lbtele.place(relx=0.30, rely=0.20)

        self.entryhora=Entry(self.Main)
        self.entryhora.place(relx=0.40, rely=0.30, relwidth=0.05)
        self.lbhora=Label(self.Main,text='Hora',background='white')
        self.lbhora.place(relx=0.30, rely=0.30)

        self.entrydata=Entry(self.Main)
        self.entrydata.place(relx=0.55, rely=0.30,relwidth=0.12)
        self.lbdata=Label(self.Main,text='Data',background='white')
        self.lbdata.place(relx=0.50, rely=0.30)


        self.bt_calendario=Button(self.Main,text='Calendario',command=self.Calendario)
        self.bt_calendario.place(relx=0.70, rely=0.30)
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
    def Tarefas(self):
        self.conecta_bd()
        dia=self.data_e_hora=strftime('%d/%m/%Y')

        show=self.conn.execute('''
       SELECT CONVERT(VARCHAR,data,103) AS Hoje, *
        from Agendas
        WHERE CONVERT(VARCHAR,data,103) = '?'

        ''',dia)

        for i in show:
            print(i)
        self.desconecta_bd()
    def VerMes(self):
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
        self.root.configure(background='black')
        self.root.geometry('700x500')
        self.root.resizable(False,False)
    def Frame(self):
        self.Main=Frame(self.root,bg= 'white',highlightbackground='black')
        self.Main.place(relx= 0.01, rely=0.01, relwidth= 0.98, relheight=0.98)
    def Widget(self):


        self.bt_imgagn=PhotoImage(file='agenda.png')
        self.bt_imgagn=self.bt_imgagn.subsample(4,4)
        self.stylo=ttk.Style()
        self.stylo.configure('Bw.TButton',image=self.bt_imgagn,background='white',foreground='white',bordercolor='white')
        self.Bt_Novo=ttk.Button(self.Main,style='Bw.TButton',command=self.Agendar)
        self.Bt_Novo.place(relx=0.10, rely=0.10,relwidth=0.10,relheight=0.15)
        self.Bt_Novo.configure(image=self.bt_imgagn)

        self.bt_imgtaref=PhotoImage(file='tarefas.png')
        self.bt_imgtaref=self.bt_imgtaref.subsample(4,4)
        self.stylo=ttk.Style()
        self.stylo.configure('Bw.TButton',image=self.bt_imgtaref)
        self.Bt_tarefa =ttk.Button(self.Main,command=self.Tarefas)
        self.Bt_tarefa.place(relx=0.10, rely=0.35,relwidth=0.10,relheight=0.15)
        self.Bt_tarefa.configure(image=self.bt_imgtaref)

        self.bt_imgmes=PhotoImage(file='mes.png')
        self.bt_imgmes=self.bt_imgmes.subsample(4,4)
        self.stylo=ttk.Style()
        self.stylo.configure('Bw.TButton',image=self.bt_imgmes)
        self.Bt_exibe=ttk.Button(self.Main,command=self.VerMes)
        self.Bt_exibe.place(relx=0.10, rely=0.60,relwidth=0.10,relheight=0.15)
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

Aplicacao()
import pyodbc

server = 'DESKTOP-AK0JHPS\SQLEXPRESS'
database = 'MYDB'
string_conexao = 'Driver={SQL Server Native CLient 11.0};Server=' + server + ';Database=' + database + ';Trusted_Connection=yes;'
c = pyodbc.connect(string_conexao)
cur=c.cursor()


def menu():
    print('Agendar uma consulta ? b :')
    print('Ver consultas marcadas ? c :')
    print('Dias disponiveis ? d :')
    print('Sair do programa ? s :')


def show_consulta(dataconsulta):
    cur.execute(f'''
        SELECT AGENDA_DATA,AGENDA_HORA,CLIENTE,DOUTOR
        FROM AGENDA
        where AGENDA_DATA LIKE ('%{dataconsulta}%')
        ''')
    for i in cur.fetchone():
        print(i)

def inser_agenda(novadata,hora,cliente,doutor):
    cur.execute(f'''
        INSERT INTO AGENDA VALUES ('{novadata}','{hora}',{cliente},{doutor})
        ''')
    cur.commit()

while True:
    menu()
    opc=input('Qual opçao desejada ?')
    if opc not in ['a','c','d','s']:
        print('Opçao invalida tente novamente')
        continue

    elif opc=='a':
        consulta=input('Qual a data a ser consultada ? YY/MM/DD HH:MM')
        show_consulta(consulta)
    elif opc=='c':
        datanova=str(input('Insira a nova data :  yy/mm/dd hh:mm '))
        hora=str(input('Hora do agendamento'))
        cliente=input('Id do cliente')
        doutor=input('id do doutor')
        inser_agenda(datanova,hora,cliente,doutor)

    elif opc =='d':
        print('VOce escolheu "d"')

    elif opc =='s':
        break
cur.close()
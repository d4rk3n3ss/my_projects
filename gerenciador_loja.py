import pyodbc

server = 'DESKTOP-AK0JHPS\SQLEXPRESS'
database = 'MYDB'
string_conexao = 'Driver={SQL Server Native CLient 11.0};Server=' + server + ';Database=' + database + ';Trusted_Connection=yes;'
c = pyodbc.connect(string_conexao)
cur=c.cursor()

def menu():
    print('''OQUE DESEJA FAZER  ?
    VERIFICAR PEDIDOS?  P
    CONFERIR ESTOQUE ?  E
    REALIZAR UMA VENDA ? V
    OPÇOES PARA CLIENTE ? C
    CADASTRAR NOVO PRODUTO NO ESTOQUE ? X
    SAIR DO PROGRAMA ?  S''')


def REALIZAR_VENDA(PRODUTO,VENDEDOR,CLIENTE,VALOR_APAGAR,PAGO):
    cur.execute(f'''
    INSERT INTO PEDIDOS VALUES ({PRODUTO},{VENDEDOR},{CLIENTE},GETDATE(),{VALOR_APAGAR},{PAGO})
    ''')
    cur.commit()

def INSERT_PRODUTO(NOME,DESCRICAO,VALOR_VENDA,VALOR_FORNECEDOR,ESTOQUE):
    cur.execute(f'''
    INSERT INTO ESTOQUE VALUES ('{NOME}','{DESCRICAO}',{VALOR_VENDA},{VALOR_FORNECEDOR},{ESTOQUE})
    ''')
    cur.commit()


def show_pedidos():
    cur.execute('''
    select c.NOME,c.ENDERECO,c.TELEFONE,p.DATACOMPRA,v.NOME
from pedidos p
inner join CLIENTES c
on p.ID_CLIENTE = c.ID_CLIENTE
inner join VENDEDORES v
on v.ID_VENDEDOR = p.ID_VENDEDOR''')
    for i in cur.fetchone():
       print(i)

def show_estoque(nome):
    cur.execute(f'''
    SELECT *
    FROM ESTOQUE
    where nome like ('%{nome}%')
''')
    if cur.rowcount !=0:
        for x in cur.fetchone():
            print(x)

    else:
        print('Nada foi encontrado')

def insert_cliente(NOMECLIENTE,ENDERECO,TELEFONE,CPF):
    cur.execute(f'''
    INSERT INTO CLIENTES VALUES ('{NOMECLIENTE}','{ENDERECO}',{TELEFONE},{CPF})
    ''')
    cur.commit()

def show_clientes(nome):
    cur.execute(f'''
    SELECT ID_CLIENTE,NOME,ENDERECO,CPF,TELEFONE
    FROM CLIENTES
    where nome like ('%{nome}%')
''')
    if cur.rowcount !=0:
        for x in cur.fetchone():
            print(x)
    else:
        print('Nao tem cadastro deste cliente em nosso sistema')

while True:
    menu()
    opc = input(' Qual o opçao desejada :')
    if opc not in ['p','e', 's','v','c','x']:
        print('Opçao invalida !! Tente outra opçao ')
        continue

    elif opc == 's':
        break

    elif opc == 'v':
        PRODUTO= int(input('Qual produto ? ID : '))
        VENDEDOR = int(input('Qual vendedor ? ID : '))
        CLIENTE = int(input('Qual o ID do cliente ? :'))
        VALOR_APAGAR=input('Qual valor a pagar ? : ')
        PAGO=input('Valor pago : ')
        REALIZAR_VENDA(PRODUTO,VENDEDOR,CLIENTE,VALOR_APAGAR,PAGO)

    elif opc =='p':
        show_pedidos()

    elif opc =='e':
        nome=input('Qual produto deseja verificar ? :')
        show_estoque(nome)
    elif opc=='x':
        produto=str(input('Nome do novo produto :'))
        descricao=str(input('Descricao do novo produto :'))
        valor=int(input('Valor para venda? :'))
        valor_for=int(input('Valor comprado do fornecedor :'))
        qtd=int(input('Quantidade comprada: '))
        INSERT_PRODUTO(produto,descricao,valor,valor_for,qtd)

    elif opc =='c':
        opc=input('''Oque deseja realizar ?')
    VERIFICAR CLIENTE ? V')
    CADASTRAR NOVO CLIENTE ? C' 
    VOLTAR AO MENU PRINCIPAL S :''')

        if opc not in ['c','v','s']:
            print('opcao invalida')
            continue
        elif opc =='c':
            NOMECLIENTE=input('Nome do novo cliente ?: ')
            ENDERECO=str(input('Endereço do novo cliente ?: '))
            TELEFONE=int(input('Telefone do novo cliente :'))
            CPF=int(input('cpf do novo cliente :'))
            insert_cliente(NOMECLIENTE,ENDERECO,TELEFONE,CPF)
        elif opc =='v':
            nomecliente=str(input('Qual o nome do cliente ? :'))
            show_clientes(nomecliente)
        elif opc =='s':
            menu()
c.close()
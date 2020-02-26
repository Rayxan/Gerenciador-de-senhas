import sqlite3

MASTER_PASSWORD = "123"

senha = input("Insira a senha do admin: ")
if senha != MASTER_PASSWORD:
    print("Senha Invalida! Encerrando...")
    exit()

conn = sqlite3.connect('passwords.db') #Conectando-se ao banco (se nao existir db, eh criado)

cursor = conn.cursor() # cria tabela que guarda users (se a tabela nao existir)

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

''')

def menu():
    print("*******************************************")
    print("[i] : inserir nova senha")
    print("[l] : listar servicos salvos")
    print("[r] : recuperar uma senha")
    print("[s] : sair")
    print("*******************************************")

def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')
    if cursor.rowcount == 0:
        print("Servico nao cadastrado (use [l] para verificar os servicos")
    else:
        for user in cursor.fetchall(): #mostar todos os usuários que tem cadastrados (tupla)
            print(user)

def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}','{password}')    
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall(): # mostra todos os servicos cadastrados (tupla)
        print(service)


while True: #laco infinito
    menu()
    op = input("O que deseja fazer? --> ")
    if op not in ['i','l','r','s']:
        print("Opcao invalida!")
        continue

    if op == 'i':
        service = input("Digite o nome do servico? --> ")
        username = input("Digite o nome do usuario? --> ")
        password = input("Digite a senha --> ")
        insert_password(service, username, password)

    if op == 'r':
        service = input("Qual o servico para o qual quer a senha --> ")
        get_password(service)

    if op == 'l':
        show_services()
    
    if op == 's':
        break

conn.close()
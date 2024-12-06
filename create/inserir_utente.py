import os
import sqlite3

# Define o caminho para o base de dados, subindo um nível do diretório atual
base_dir = os.path.dirname(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'database', 'utentes.db')

# Função para inserir um novo utente na base de dados
def inserir(nome, idade, numero_bi, estado):
    # Conecta a base de dados
    conn = sqlite3.connect(db_path)
    curr = conn.cursor()

    # Cria a tabela 'utentes' se ela ainda não existir
    curr.execute(f'''
                CREATE TABLE IF NOT EXISTS utentes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                numero_bi TEXT NOT NULL,
                estado TEXT NOT NULL             
    )''')

    # Insere os dados do utente na tabela
    curr.execute('INSERT INTO utentes (nome, idade, numero_bi, estado) VALUES (?, ?, ?, ?)', (nome, idade, numero_bi, estado))

    # Salva as alterações na base e fecha a conexão
    conn.commit()
    conn.close()

# Função para transferir dados de utentes internados para a tabela 'utentes_internados'
def inserir_internados():
    # Conecta ao base de dados
    conn = sqlite3.connect(db_path)
    curr = conn.cursor()

    # Cria a tabela 'utentes_internados' se ela ainda não existir
    curr.execute(f'''
                CREATE TABLE IF NOT EXISTS utentes_internados(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                numero_bi TEXT NOT NULL,
                estado TEXT NOT NULL             
    )''')

    # Limpa todos os dados da tabela 'utentes_internados'
    curr.execute("DELETE FROM utentes_internados")
    curr.execute("DELETE FROM sqlite_sequence WHERE name='utentes_internados'")  # Reinicia a sequência de IDs

    # Insere na tabela 'utentes_internados' os dados dos utentes com estado 'internado'
    curr.execute("""INSERT INTO utentes_internados (nome, idade, numero_bi, estado)
                    SELECT nome, idade, numero_bi, estado
                    FROM utentes
                    WHERE estado = 'internado';
                """)

    # Salva as alterações no base e fecha a conexão
    conn.commit()
    conn.close()

# Função para transferir dados de utentes de alta para a tabela 'utentes_alta'
def inserir_altas():
    # Conecta ao base de dados
    conn = sqlite3.connect(db_path)
    curr = conn.cursor()

    # Cria a tabela 'utentes_alta' se ela ainda não existir
    curr.execute(f'''
                CREATE TABLE IF NOT EXISTS utentes_alta(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                numero_bi TEXT NOT NULL,
                estado TEXT NOT NULL             
    )''')

    # Limpa todos os dados da tabela 'utentes_alta'
    curr.execute("DELETE FROM utentes_alta")
    curr.execute("DELETE FROM sqlite_sequence WHERE name='utentes_alta'")  # Reinicia a sequência de IDs

    # Insere na tabela 'utentes_alta' os dados dos utentes com estado 'alta'
    curr.execute("""INSERT INTO utentes_alta (nome, idade, numero_bi, estado)
                    SELECT nome, idade, numero_bi, estado
                    FROM utentes
                    WHERE estado = 'alta';
                """)

    # Salva as alterações na base de dados e fecha a conexão
    conn.commit()
    conn.close()

# Função para receber dados do usuário e inserir na base de dados
def input_user():
    # Loop para obter o nome do utente
    while True:
        try:
            nome = input("Introduza o nome do utente: \n=>")
            break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    # Loop para obter a idade do utente
    while True:
        try:
            idade = int(input("Introduza a idade do utente (só aceita números inteiros): \n=>"))
            break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    # Loop para obter o número de BI do utente
    while True:
        try:
            numero_bi = input("Introduza o numero do BI do utente: \n=>")
            break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    # Loop para obter o estado do utente ('alta' ou 'internado')
    while True:
        try:
            estado = input("O utente está internado ou de alta: \n=>")
            estado = estado.lower()  # Converte para minúsculas para consistência
            if estado == 'alta' or estado == 'internado':  # Valida o estado
                break
            else:
                print("Escreva 'alta' ou 'internado'")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    # Tenta inserir os dados no base de dados e atualizar as tabelas
    try:
        inserir(nome, idade, numero_bi, estado)  # Insere o novo utente na tabela principal
        inserir_internados()  # Atualiza a tabela de internados
        inserir_altas()  # Atualiza a tabela de alta
        
    except Exception as e:
        print(f"Erro: {e}")

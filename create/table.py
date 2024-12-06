import os
import sqlite3

base_dir = os.path.dirname(os.path.dirname(__file__))  # Sobe um nível no diretório
db_path = os.path.join(base_dir, 'database', 'utentes.db')# Caminho para a base de dados

conn= sqlite3.connect(db_path)

curr = conn.cursor()
#Variavel com o nome da tabela 
nome_tabela = input("Escreva o nome da tabela:")

# Cria a tabela com a variavel nome_tabela
curr.execute(f'''
                CREATE TABLE IF NOT EXISTS {nome_tabela}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                numero_bi TEXT NOT NULL,
                estado TEXT NOT NULL             
)''')
#Salva 
conn.commit()
#Fecha a conexao
conn.close()
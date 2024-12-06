import os
import sqlite3

# Função para ler todos os registros da tabela 'utentes_alta'
def read_utentes_altas():
    # Define o diretório base, subindo um nível a partir do diretório atual
    base_dir = os.path.dirname(os.path.dirname(__file__))
    # Monta o caminho completo para o banco de dados 'utentes.db'
    db_path = os.path.join(base_dir, 'database', 'utentes.db')

    # Conecta ao banco de dados
    conn = sqlite3.connect(db_path)
    curr = conn.cursor()  # Cria um cursor para executar comandos SQL

    # Cria a tabela 'utentes_alta' caso ela ainda não exista
    curr.execute(f'''
                    CREATE TABLE IF NOT EXISTS utentes_alta(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    numero_bi TEXT NOT NULL,
                    estado TEXT NOT NULL             
        )''')

    # Seleciona todos os registros da tabela 'utentes_alta'
    curr.execute('''SELECT * FROM utentes_alta''')
    resultados = curr.fetchall()  # Obtém todos os resultados da consulta em uma lista de tuplas

    # Itera pelos resultados e imprime cada registro
    for i in resultados:
        print(i)

    # Fecha a conexão com o banco de dados
    conn.close()

import sqlite3
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

base_dir = os.path.dirname(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'database', 'utentes.db')

from create.inserir_utente import inserir_altas, inserir_internados

def update_all():
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

    curr.execute('''SELECT * FROM utentes''')
    resultados = curr.fetchall()  # Obtém todos os resultados da consulta em uma lista de tuplas

    # Itera pelos resultados e imprime cada registro
    for i in resultados:
        print(i)

    opc = int(input("Selecione um id para alterar\n=>"))
    
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

    curr.execute(f'''UPDATE alunos
                 SET nome = {nome} AND idade = {idade} AND numero_bi = {numero_bi} AND estado = {estado}
                 WHERE id = {opc}   
                ''')
    conn.commit()
    conn.close
    



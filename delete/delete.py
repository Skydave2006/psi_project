import sqlite3
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

base_dir = os.path.dirname(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'database', 'utentes.db')

from create.inserir_utente import inserir_altas, inserir_internados



def apagar():
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

    try:
        while True:
            opc = int(input("Selecione um id para apagar\n=>"))
            veri = input("Comfirmação(S/N):").upper()
            
            if veri == "S":
                curr.execute(f"DELETE FROM utentes WHERE id = {opc}")
                conn.commit()

                inserir_internados()
                inserir_altas()
                conn.commit()

                break

            elif veri == "N":
                print("Cancelado!!!")
                break
            
            else:
                print("Insira sim(S) ou não(N).")

    except Exception as e:
        print(f"Erro:{e}")
    

    finally:
        conn.close()

apagar()

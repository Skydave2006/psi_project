import sqlite3 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

# Current file directory
current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
db_path = os.path.join(base_dir, 'database', 'corridas.db')



# Connect to the SQLite database
conn = sqlite3.connect(db_path)
curr = conn.cursor()

def from_piloto_to_carro():
    # curr.execute('''
    #             SELECT * FROM carros INNER JOIN pilotos ON carros.id_piloto = pilotos.id
    # ''')
    curr.execute('''
                SELECT * FROM pilotos INNER JOIN carros ON pilotos.id = carros.id_piloto
    ''')
    resultados = curr.fetchall()
    for a in resultados:
        print(a)
    print("mclaren")

def read_carros():
    print()
    curr.execute('''SELECT * FROM carros''')
    resultados = curr.fetchall()  # Obtém todos os resultados da consulta em uma lista de tuplas

    # Itera pelos resultados e imprime cada registro
    for i in resultados:
        print(i)

def read_pilotos():
    print()
    curr.execute('''SELECT * FROM pilotos''')
    resultados = curr.fetchall()  # Obtém todos os resultados da consulta em uma lista de tuplas

    # Itera pelos resultados e imprime cada registro
    for i in resultados:
        print(i)

from_piloto_to_carro()

conn.commit()
conn.close()  
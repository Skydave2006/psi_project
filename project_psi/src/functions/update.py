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

def update_carros():
    curr.execute('''
                UPDATE carros
                SET marca = ?, numero_do_carro = ?, id_piloto = ?
                WHERE id = ?   
                ''',("Lexus",45,5,1))

def update_pilotos():
    curr.execute('''
                UPDATE pilotos
                SET nome = ?, idade = ?, nacionalidade = ?
                WHERE id = ?   
                ''',("Sabrina",45,"EUA",1))

#INSERT INTO carros (marca, numero_do_carro, id_piloto)
#INSERT INTO pilotos (nome, idade, nacionalidade)



conn.commit()
conn.close()  
import sqlite3 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

# ficheiro
current_dir = os.path.dirname(__file__)
#para o folder
base_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
#caminho para a base de dados
db_path = os.path.join(base_dir, 'database', 'corridas.db')



# conexão com a database
conn = sqlite3.connect(db_path)
curr = conn.cursor()

# update carro
def update_carros():
    curr.execute('''
                UPDATE carros
                SET marca = ?, numero_do_carro = ?, id_piloto = ?
                WHERE id = ?   
                ''',("Lexus",45,5,1))
    
# update piloto
def update_pilotos():
    curr.execute('''
                UPDATE pilotos
                SET nome = ?, idade = ?, nacionalidade = ?
                WHERE id = ?   
                ''',("Sabrina",45,"EUA",1))





conn.commit()
conn.close()  
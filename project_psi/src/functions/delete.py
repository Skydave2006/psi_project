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

def drop_table():
    curr.execute('''DROP TABLE corrida''')

def delete_from_carros():
    print()
    curr.execute('''DELETE * FROM carros WHERE id = 1''')

def delete_from_pilotos():
    print()
    curr.execute('''DELETE * FROM pilotos WHERE id = 1''')
    


conn.commit()
conn.close()   
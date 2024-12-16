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

def create_tables():

    curr.execute(f'''
                CREATE TABLE IF NOT EXISTS carros(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                marca TEXT NOT NULL,
                numero_do_carro INTEGER NOT NULL,
                id_piloto INTENGER NULL
                            
    )''')

    curr.execute(f'''
                CREATE TABLE IF NOT EXISTS pilotos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                nacionalidade TEXT NOT NULL             
    )''')
    curr.execute(f'''
                CREATE TABLE IF NOT EXISTS corrida(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_piloto INTEGER NULL,
                id_carro INTEGER NULL
                            
    )''')  
create_tables()
def insert_into_carros():
    print("carros")
       
    curr.execute('INSERT INTO pilotos (nome, idade, nacionalidade) VALUES (?, ?, ?)',("Armando",40,"Portugues"))


def insert_into_pilotos():

    curr.execute('INSERT INTO carros (marca, numero_do_carro, id_piloto) VALUES (?, ?, ?)',("Ferrari",44,""))
    print("pilotos")
    conn.commit()

def insert_into_corrida():
    curr.execute('INSERT INTO corrida ( id_piloto, id_carro) VALUES (?, ?)',(3,2))
    
    print("corridas")




conn.commit()
conn.close()  

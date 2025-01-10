import sqlite3 
import sys
import os
#para o repositorio mãe
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

# ve os pilotos que tem um carro
def from_piloto_to_carro():
    
    curr.execute('''
                SELECT * FROM pilotos INNER JOIN carros ON pilotos.id = carros.id_piloto
    ''')


    resultados = curr.fetchall()

    for a in resultados:
        print(a)


    print("mclaren")
#função para ver os carros existentes
def read_carros():
    
    curr.execute('''SELECT * FROM carros''')
    resultados = curr.fetchall()  # Obtém todos os resultados da base de dados

    # imprime cada registro
    for i in resultados:
        print(i)
        
#função para ver os pilotos existentes
def read_pilotos():
    
    curr.execute('''SELECT * FROM pilotos''')
    resultados = curr.fetchall()  # Obtém todos os resultados da base de dados

    # imprime cada registro
    for i in resultados:
        print(i)

from_piloto_to_carro()

conn.commit()
conn.close()  
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from create.inserir_utente import input_user
from read.read_all import read_all,read_menores
from read.read_utentes_altas import read_utentes_altas
from read.read_utentes_internados import read_utentes_internados
from read.read_nome import read_nome_all,read_nome_alta,read_nome_internados
from delete.delete import apagar
from update.update import update_all




def menu_utentes():   
    
    while True:
        input_menu = int(input('''*******MENU*******\n
                               1-Inserir utente\n
                               2-Ver todos os utentes\n
                               3-Ver utentes em alta\n
                               4-Ver utentes internados\n
                               5-Ver só nomes dos utentes\n
                               6-Ver menores\n
                               7-Apagar utente\n
                               8-Atualizar utente\n
                               0-Sair\n
                               Insira o numero que deseja\n
                               =>
                               '''))
        
        match input_menu:
            case 1:
                input_user()#função de inserir dados na base de dados

            case 2:
                read_all()#função de ver todos os utentes
            case 3:
                read_utentes_altas()#função de ver os utentes que tem alta
            case 4:
                read_utentes_internados()#função de ver os utentes internados
            case 5:
                while True:
                    
                    opcao = input("Pretende ver os que estão em alta ou internados:")
                    opcao = opcao.lower()# Converte para minúsculas para consistência
                    try:
                        if opcao== 'alta':# Valida o estado
                            read_nome_alta()
                            break
                        if opcao == 'internados':# Valida o estado
                            read_nome_internados()
                            break
                    except Exception as e:
                        print(f"Ocorreu um erro:{e}\nEscreva \"alta\" ou \"internado\"")
                        
            case 6:
                read_menores()# Função de ver utentes menores de idade

            case 7:
                apagar()

            case 8:
                update_all()
            case 0:#Sai do ciclo do menu
                break
            case _:
                print("Selecione um numero do menu")# Caso não seja escolhido nenhuma opção



            



            
        
        
            
        
        
            
        



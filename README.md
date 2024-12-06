# Estrutura do Projeto

- trabalho-psi/
  - app/
    - main.py
  - create/
    - inserir_utente.py
    - table.py
    - __init__.py
  - database/
    - utentes.db
  - menu/
    - menu.py
  - read/
    - read_all.py
    - read_utentes_altas.py
    - read_utentes_internados.py


1. main.py (app)
Este arquivo é o ponto de entrada do sistema. O código dentro dele esta a servir como ponto de comando para o resto da aplicação.


2. inserir_utente.py (create)
Este arquivo contém funções relacionadas à inserção de dados no banco de dados. O processo inclui adicionar utentes (pacientes) e atualizá-los em diferentes tabelas com base no seu estado (internado ou de alta).

Funções:
inserir(nome, idade, numero_bi, estado):

Responsável por inserir um novo utente na tabela utentes. Recebe os parâmetros: nome, idade, numero_bi (número de identidade), e estado (indicando se o utente está internado ou de alta).
inserir_internados():

Atualiza a tabela utentes_internados com todos os utentes que têm o estado "internado".
Exclui registros antigos e os substitui com os dados atualizados da tabela utentes.
inserir_altas():

Similar a inserir_internados, mas para os utentes com estado "alta". Atualiza a tabela utentes_alta.
input_user():

Função para interagir com o usuário, pedindo informações sobre o utente (nome, idade, número do BI e estado). Depois de obter esses dados, ela chama as funções de inserção no banco.
3. table.py (create)
Este arquivo contem definições de tabelas e operações de banco de dados, como a criação de tabelas e a definição de suas colunas.

id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
idade INTEGER NOT NULL,
numero_bi TEXT NOT NULL,
estado TEXT NOT NULL

4. __init__.py (create)
Este arquivo é usado para marcar o diretório como um pacote Python e possibilitar a importação de funções ou módulos entre diretórios. Ele pode ser vazio ou conter inicializações específicas.

5. menu.py (menu)
Este arquivo contém a lógica de exibição do menu para o usuário, fornecendo opções de interação com o sistema.

Funções:
menu_utentes():
Exibe o menu para o usuário, onde ele pode escolher entre diferentes ações como visualizar os utentes, atualizar estados ou sair do programa.
6. read_all.py (read)
Este arquivo é responsável por ler os dados do banco de dados. Ele provavelmente está implementando a função para visualizar todos os utentes cadastrados.

Funções:
read_all():
Função que consulta todos os registros da tabela utentes e os imprime ou os retorna de alguma forma.
7. read_utentes_altas.py (read)
Arquivo responsável por ler os dados específicos dos utentes com estado "alta". Ele provavelmente exibe ou retorna os registros dos utentes que tiveram alta do hospital.

Funções:
read_utentes_altas():
Função que consulta e retorna ou exibe os registros da tabela utentes_alta.
8. read_utentes_internados.py (read)
Semelhante ao arquivo anterior, mas para utentes com o estado "internado".

Funções:
read_utentes_internados():
Função que consulta e retorna ou exibe os registros da tabela utentes_internados.

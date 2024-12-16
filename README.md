Funcionalidades
1. create.py - Gerenciamento de tabelas e inserção de dados
Função create_tables:
Cria as tabelas no banco de dados:

carros: Armazena os dados dos carros.
pilotos: Armazena os dados dos pilotos.
corrida: Armazena os dados das corridas.

Função insert_into_carros:
Insere registros na tabela carros.

Função insert_into_pilotos:
Insere registros na tabela pilotos.

Função insert_into_corrida:
Insere registros na tabela corrida.

2. read.py - Leitura de dados
Função from_piloto_to_carro:
Retorna os carros associados a um piloto específico.

Função read_carros:
Lê e retorna todos os registros da tabela carros.

Função read_pilotos:
Lê e retorna todos os registros da tabela pilotos.

3. update.py - Atualização de dados
Função update_carros:
Atualiza informações de um registro na tabela carros.

Função update_pilotos:
Atualiza informações de um registro na tabela pilotos.

4. main.py - Ponto de entrada da aplicação
Arquivo principal onde o sistema é executado.
Configura as chamadas para as funções contidas nos módulos de criação, leitura, atualização e exclusão de dados.



Estrutura do repositório

project_psi
├── database
│   └── corridas.db        # Banco de dados SQLite contendo as tabelas e dados
├── src
│   ├── app
│   │   └── main.py        # Arquivo principal para execução do sistema
│   ├── functions
│       ├── create.py      # Funções para criação de tabelas e inserção de dados
│       ├── delete.py      # Funções para exclusão de dados
│       ├── read.py        # Funções para leitura de dados
│       └── update.py      # Funções para atualização de dados

import sqlite3

db_path = 'fixflow.db'

try:
    connection = sqlite3.connect(db_path)
    print(f'Banco de dados {db_path} criado com sucesso!')

except sqlite3.Error as e:
    print(f'Erro ao criar banco de dados {db_path}: {e}')

finally:
    if connection:
        connection.close()
        print(f'Conexão com o banco de dados {db_path} fechada!')
        connection = None
        print('Conexão fechada!')
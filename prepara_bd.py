from app.models.BancoDeDados import BancoDeDados

if __name__ == '__main__':
    bd = BancoDeDados('./instance/app.db')
    
    cria_tabela_pessoa_query = '''
    CREATE TABLE IF NOT EXISTS Pessoa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL,
        tipo TEXT NOT NULL
    );
    '''
    
    bd.cria_tabela(cria_tabela_pessoa_query)
    bd.insere_pessoa('Joaozinho', '123', 'M')
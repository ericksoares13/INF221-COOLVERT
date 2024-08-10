import sqlite3

class BancoDeDados: 
    def __init__(self, nome):
        self.nome = nome
        self.__con = None
        self.__insere_pessoa_query = 'INSERT INTO Pessoa (nome, senha, tipo) VALUES (?, ?, ?)'
        
    def __conecta(self):
        self.__con = sqlite3.connect(self.nome)
    
    def __fecha(self):
        if self.__con:
            self.__con.close()
            self.__con = None
    
    def __executa_query(self, query, parametros=()):
        self.__conecta()
        cursor = self.__con.cursor()
        cursor.execute(query, parametros)
        self.__con.commit()
        resultado = cursor.fetchall()
        cursor.close()
        self.__fecha()
        return resultado
        
    def __executa_query_sem_retorno(self, query, parametros=()):
        self.__conecta()
        cursor = self.__con.cursor()
        cursor.execute(query, parametros)
        self.__con.commit()
        cursor.close()
        self.__fecha()
        
    def cria_tabela(self, query):
        self.__executa_query_sem_retorno(query)
        
    def insere_pessoa(self, nome, senha, tipo):
        self.__executa_query_sem_retorno(self.__insere_pessoa_query, (nome, senha, tipo))
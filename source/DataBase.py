from PyQt5.QtSql import QSqlDatabase, QSqlQuery


invalidConnection = "Conexão com o banco de dados não está aberta."


class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = None

    def connect(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.db_name)

        if not self.db.open():
            print("Não foi possível conectar ao banco de dados.")
            return False

        print("Conexão com o banco de dados estabelecida.")
        return True

    def create_table(self):
        if not self.db.isOpen():
            print(invalidConnection)
            return

        query = QSqlQuery()
        query.exec_(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        """
        )

        if query.lastError().type() != 0:
            print(f"Erro ao criar a tabela: {query.lastError().text()}")
        else:
            print("Tabela criada com sucesso.")

    def insert_data(self, nome):
        if not self.db.isOpen():
            print(invalidConnection)
            return

        query = QSqlQuery()
        query.prepare("INSERT INTO usuarios (nome) VALUES (?)")
        query.addBindValue(nome)

        if not query.exec_():
            print(f"Erro ao inserir dados: {query.lastError().text()}")
        else:
            print("Dados inseridos com sucesso.")

    def consult_data(self):
        if not self.db.isOpen():
            print(invalidConnection)
            return

        query = QSqlQuery()
        query.exec_("SELECT * FROM usuarios")

        if query.lastError().type() != 0:
            print(f"Erro ao consultar dados: {query.lastError().text()}")
        else:
            while query.next():
                _id = query.value(0)
                nome = query.value(1)
                print(f"ID: {_id}, Nome: {nome}")

    def disconnect(self):
        if self.db:
            self.db.close()
            print("Conexão com o banco de dados fechada.")

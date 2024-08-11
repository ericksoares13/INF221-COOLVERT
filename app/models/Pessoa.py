from app import bd

class Pessoa(bd.Model):
    __tablename__ = 'pessoa'
    
    id = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    nome = bd.Column(bd.String(80), nullable=False)
    email = bd.Column(bd.String(80), unique=True, nullable=False)
    senha = bd.Column(bd.String(80), nullable=False)
    tipo = bd.Column(bd.CHAR, nullable=False)

    def __repr__(self):
        return f'<({self.id}) {self.nome} {self.email} {self.senha} {self.tipo}>'
    
    def verifica_senha(self, senha):
        return self.senha == senha
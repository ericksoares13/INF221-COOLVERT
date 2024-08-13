from app import bd

class Contratante(bd.Model):
    __tablename__ = 'contratante'
    
    id = bd.Column(bd.Integer, bd.ForeignKey('pessoa.id'), primary_key=True)
    nome_estabelecimento = bd.Column(bd.String(80), nullable=False)
    cidade = bd.Column(bd.String(80), nullable=False)
    
    def __repr__(self):
        return f'<({self.id}) {self.nome_estabelecimento}>'
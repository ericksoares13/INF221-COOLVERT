from app import bd

class Musico(bd.Model):
    __tablename__ = 'musico'
    
    id = bd.Column(bd.Integer, bd.ForeignKey('pessoa.id'), primary_key=True)
    nome_pessoal = bd.Column(bd.String(80), nullable=False)
    nome_artistico = bd.Column(bd.String(80), nullable=False)
    
    def __repr__(self):
        return f'<({self.id}) {self.nome_pessoal} {self.nome_artistico}>'
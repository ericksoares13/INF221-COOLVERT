from app import bd

class Usuario(bd.Model):
    __tablename__ = 'usuario'
    
    id = bd.Column(bd.Integer, bd.ForeignKey('pessoa.id'), primary_key=True)
    celular = bd.Column(bd.String(13), nullable=False)
    documento = bd.Column(bd.String(20), nullable=False)

    def __repr__(self):
        return f'<({self.id}) {self.nome} {self.documento}>'
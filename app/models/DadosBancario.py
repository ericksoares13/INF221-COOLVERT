from app import bd

class DadosBancario(bd.Model):
    __tablename__ = 'dadosBancario'
    
    id = bd.Column(bd.Integer, bd.ForeignKey('usuario.id'), primary_key=True)
    numCartao = bd.Column(bd.String(20), nullable=False)
    nomeCartao = bd.Column(bd.String(50), nullable=False)
    codSeguranca = bd.Column(bd.Integer, nullable=False)
    validade = bd.Column(bd.String(5), nullable=False)

    def __repr__(self):
        return f'<({self.id}) {self.agencia} {self.conta} {self.numCartao}>'
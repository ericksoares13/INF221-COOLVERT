from app import bd
from datetime import datetime, UTC

class Mensagem(bd.Model):
    __tablename__ = 'mensagem'
    
    id = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    match = bd.Column(bd.Integer, bd.ForeignKey('match.id'), nullable=False)
    dono = bd.Column(bd.Integer, bd.ForeignKey('usuario.id'), nullable=False)
    mensagem = bd.Column(bd.String(200), nullable=False)
    horario = bd.Column(bd.DateTime, default=datetime.now(UTC))

    def __repr__(self):
        return f'<({self.horario}) {self.dono}: {self.mensagem}>'
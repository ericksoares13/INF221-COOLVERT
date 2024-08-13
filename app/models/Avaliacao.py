from app import bd
from enum import Enum
from sqlalchemy import Enum as SQLAEnum
    
class ParteAvaliacaoEnum(Enum):
    PAGAMENTO = "Pagamento"
    PONTUALIDADE = "Pontualidade"
    QUALIDADE_SOM = "Qualidade equipamento de som"
    VERACIDADE_INFORMACOES = "Veracidade das informações"
    DIVULGACAO_SHOW = "Divulgação do show"
    
class Avaliacao(bd.Model):
    __tablename__ = 'avaliacao'
    
    dono = bd.Column(bd.Integer, bd.ForeignKey('usuario.id'), primary_key=True)
    perfil = bd.Column(bd.Integer, bd.ForeignKey('perfil.id'), primary_key=True)
    parte_avaliacao = bd.Column(SQLAEnum(ParteAvaliacaoEnum), primary_key=True)
    estrelas = bd.Column(bd.Integer, nullable=False)
    comentario = bd.Column(bd.String(250), default='')

    def __repr__(self):
        return f'<(De {self.dono} para {self.perfil}) {self.estrelas}: {self.comentario}>'
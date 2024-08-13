from app import bd
from enum import Enum
from sqlalchemy import Enum as SQLAEnum

class EstiloMusical(bd.Model):
    __tablename__ = 'estiloMusical'
    
    id = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    nome = bd.Column(bd.String(20), nullable=False, unique=True)
    
class TipoPagamentoEnum(Enum):
    FIXO = "Fixo"
    COUVERT = "Couvert"

class MomentoPagamentoEnum(Enum):
    APOS_EVENTO = "Após o evento"
    ANTECIPADO = "Antecipado"

class Demanda(bd.Model):
    __tablename__ = 'demanda'
    
    id = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    data_show = bd.Column(bd.Date, nullable=False)
    raio_procurado = bd.Column(bd.Integer, nullable=False)
    fornece_equipamento = bd.Column(bd.Boolean, default=False)
    publico_esperado = bd.Column(bd.Integer, nullable=False)
    duracao_show = bd.Column(bd.String(5), nullable=False)
    visivel = bd.Column(bd.Boolean, default=True)
    
    tipo_pagamento = bd.Column(SQLAEnum(TipoPagamentoEnum), nullable=False)
    momento_pagamento = bd.Column(SQLAEnum(MomentoPagamentoEnum), nullable=False)

    estilos = bd.relationship('EstiloMusical', secondary='demanda_estilos')
    dono = bd.Column(bd.Integer, bd.ForeignKey('contratante.id'), nullable=False)
    
    def __repr__(self):
        return f'<({self.data_show}) {self.publico_esperado} {self.duracao_show}>'

class DemandaEstilos(bd.Model):
    __tablename__ = 'demanda_estilos'

    demanda = bd.Column(bd.Integer, bd.ForeignKey('demanda.id'), primary_key=True)
    estilo_musical = bd.Column(bd.Integer, bd.ForeignKey('estiloMusical.id'), primary_key=True)
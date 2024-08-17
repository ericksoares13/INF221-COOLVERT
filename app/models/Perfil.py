from app import bd
from enum import Enum
from sqlalchemy import Enum as SQLAEnum

class Perfil(bd.Model):
    __tablename__ = 'perfil'
    
    id = bd.Column(bd.Integer, bd.ForeignKey('usuario.id'), primary_key=True)
    descricao = bd.Column(bd.String(250), nullable=False)       # também foi adicionada a músico
    nome_instagram = bd.Column(bd.String(25), nullable=False)
    link_instagram = bd.Column(bd.String(200), nullable=False)
    link_spotify = bd.Column(bd.String(200), nullable=False)
    link_youtube = bd.Column(bd.String(200), nullable=False)
    
    def __repr__(self):
        return f'<({self.id}) {self.descricao}>'
    
class TipoFotoEnum(Enum):
    PERFIL = "Perfil"
    INSTAGRAM = "Instagram"
    PORTFOLIO = "portfólio"
    
class Imagem(bd.Model):
    __tablename__ = 'imagem'
    
    id = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    dono = bd.Column(bd.Integer, bd.ForeignKey('usuario.id'), nullable=False)
    nome = bd.Column(bd.String(25), nullable=False, unique=True)
    tipo_foto = bd.Column(SQLAEnum(TipoFotoEnum), nullable=False)
    caminho = bd.Column(bd.String(255), nullable=False)

    def __repr__(self):
        return f'<({self.id}) {self.nome} {self.tipo_foto}>'
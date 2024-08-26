from unittest.mock import MagicMock

# Mocks das classes dependentes
class Mensagem:
    def __init__(self, match, dono, mensagem):
        self.match = match
        self.dono = dono
        self.mensagem = mensagem

    query = MagicMock()

class Imagem:
    def __init__(self, dono, nome, tipo_foto, caminho):
        self.dono = dono
        self.nome = nome
        self.tipo_foto = tipo_foto
        self.caminho = caminho

    query = MagicMock()

class TipoFotoEnum:
    PERFIL = 'PERFIL'

class Pessoa:
    query = MagicMock()

class Contratante:
    query = MagicMock()

# Código original
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Código copiado de app.__init__.py para remover as dependenias
app = Flask(__name__)
app.secret_key = "default_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
bd = SQLAlchemy(app)

# Classe BancoDeDados
class BancoDeDados:
    @staticmethod
    def EnviaMensagem(obj):
        with app.app_context():
            mensagem = Mensagem(match=obj['match'], dono=obj['dono'], mensagem=obj['mensagem'])
            bd.session.add(mensagem)
            bd.session.commit()

    @staticmethod
    def GetChat(id_match):
        with app.app_context():
            return sorted(list(Mensagem.query.filter_by(match=id_match).all()), key=lambda x: x.horario)

    @staticmethod
    def CriaImagem(obj):
        with app.app_context():
            imagem = Imagem(dono=obj['dono'], nome=obj['nome'], tipo_foto=TipoFotoEnum(obj['tipo_foto']), caminho=obj['caminho'])
            bd.session.add(imagem)
            bd.session.commit()

    @staticmethod
    def GetImagemPerfil(dono):
        with app.app_context():
            return Imagem.query.filter_by(dono=dono, tipo_foto=TipoFotoEnum.PERFIL).first()

    @staticmethod
    def GetUser(id_user):
        with app.app_context():
            return Pessoa.query.get(id_user)

    @staticmethod
    def GetContratante(id_contratante):
        with app.app_context():
            return Contratante.query.get(id_contratante)

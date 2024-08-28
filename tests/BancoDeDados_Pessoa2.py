from mock_models import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "default_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
bd = SQLAlchemy(app)


class BancoDeDados:
    @staticmethod
    def Login(obj):
        with app.app_context():
            pessoa = None
            pessoa = Pessoa.query.filter_by(email=obj['identificador']).first()
            if pessoa is None:
                pessoa = Pessoa.query.filter_by(nome=obj['identificador']).first()
            if pessoa and pessoa.verifica_senha(obj['senha']):
                return pessoa
            else: 
                return None
    
    @staticmethod
    def VerificaEmail(email):
        with app.app_context():
            return False if Pessoa.query.filter_by(email=email).first() else True
    
    @staticmethod
    def VerificaNomeUsuario(nome):
        with app.app_context():
            return False if Pessoa.query.filter_by(nome=nome).first() else True
        
    @staticmethod
    def VerificaEstiloMusical(nome):
        with app.app_context():
            return False if EstiloMusical.query.filter_by(nome=nome).first() else True
        
    @staticmethod
    def CriaEstiloMusical(nome):
        with app.app_context():
            estiloMusical = EstiloMusical(nome=nome)
            bd.session.add(estiloMusical)
            bd.session.commit()
    
    @staticmethod
    def GetEstilosMusicais(id_demanda):
        with app.app_context():
            estilos = DemandaEstilos.query.filter_by(demanda=id_demanda).all()
            estilos_musicais = []
            for estilo in estilos:
                estilos_musicais.append(EstiloMusical.query.with_entities(EstiloMusical.nome).filter_by(id=estilo.estilo_musical).first()[0])
            return estilos_musicais

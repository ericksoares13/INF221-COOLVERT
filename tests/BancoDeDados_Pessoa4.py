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
    def GetNomeUsuario(user_id):
        with app.app_context():
            pessoa = Pessoa.query.get(user_id)
            return pessoa.nome if pessoa else None

    @staticmethod
    def CriaMatch(obj):
        with app.app_context():
            match = Match(id_musico=obj['id_musico'], id_demanda=obj['id_demanda'])
            bd.session.add(match)
            bd.session.commit()
            return match.id

    @staticmethod
    def GetMatch(id_match):
        with app.app_context():
            return Match.query.get(id_match)

    @staticmethod
    def GetMatches(id_demanda):
        with app.app_context():
            return list(Match.query.filter_by(id_demanda=id_demanda).all())

    @staticmethod
    def GetMatchesMusico(id_musico):
        with app.app_context():
            return list(Match.query.filter_by(id_musico=id_musico).all())

    @staticmethod
    def GetMusicos(id_demanda):
        with app.app_context():
            return [id[0] for id in Match.query.with_entities(Match.id_musico).filter_by(id_demanda=id_demanda).all()]

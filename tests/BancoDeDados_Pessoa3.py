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
    def CriaDemanda(obj):
        with app.app_context():
            nova_demanda = Demanda(
                data_show=obj["data_show"],
                raio_procurado=obj["raio_procurado"],
                fornece_equipamento=obj["fornece_equipamento"],
                publico_esperado=obj["publico_esperado"],
                duracao_show=obj["duracao_show"],
                dono=obj["dono"],
                tipo_pagamento=TipoPagamentoEnum(obj["tipo_pagamento"]),
                momento_pagamento=MomentoPagamentoEnum(obj["momento_pagamento"]),
            )
            for nome_estilo in obj["estilos"]:
                estilo_musical = EstiloMusical.query.filter_by(nome=nome_estilo).first()
                nova_demanda.estilos.append(estilo_musical)
            contratante = Contratante.query.get(obj["dono"])
            bd.session.add(nova_demanda)
            bd.session.commit()

    @staticmethod
    def GetDemandas(id_dono=None):
        with app.app_context():
            if id_dono is None:
                return list(Demanda.query.filter_by(visivel=True).all())
            else:
                return list(Demanda.query.filter_by(dono=id_dono).all())

    @staticmethod
    def GetDemanda(id_demanda):
        with app.app_context():
            return Demanda.query.get(id_demanda)

    @staticmethod
    def FechaDemanda(id_match):
        with app.app_context():
            match = Match.query.get(id_match)
            if match:
                demanda = Demanda.query.get(match.id_demanda)
                if demanda:
                    demanda.visivel = False
                    bd.session.commit()

    @staticmethod
    def LiberaDemanda(id_match):
        with app.app_context():
            match = Match.query.get(id_match)
            if match:
                demanda = Demanda.query.get(match.id_demanda)
                if demanda:
                    demanda.visivel = True
                    bd.session.commit()

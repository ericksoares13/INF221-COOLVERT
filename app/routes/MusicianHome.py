from app import app
from flask import render_template, request, session

from app.models.BancoDeDados import BancoDeDados


MUSICIAN_HOME_HTML = "musicianHome.html"


@app.route("/homeMusico", methods=["POST"])
def home_musico():
    return render_template(MUSICIAN_HOME_HTML, demands=get_demandas())


@app.route("/homeMusico", methods=["GET"])
def get_home_musico():
    return render_template(MUSICIAN_HOME_HTML, demands=get_demandas())


@app.route("/procurarMusico", methods=["POST", "GET"])
def procurar_musico():
    return render_template(MUSICIAN_HOME_HTML, demands=get_demandas())


@app.route("/perfilMusico", methods=["POST", "GET"])
def perfil_musico():
    return render_template(MUSICIAN_HOME_HTML, demands=get_demandas())


@app.route("/candidatarDemanda", methods=["POST"])
def candidatar_demanda():
    demanda_id = request.form.get('demanda_id')
    musico_id = session.get("usuárioLogado")["id"]
    BancoDeDados.CriaMatch({
        'id_musico': musico_id,
        'id_demanda': demanda_id,
    })
    return render_template(MUSICIAN_HOME_HTML, demands=get_demandas(), notification=True)


@app.route("/candidatarDemanda", methods=["GET"])
def get_candidatar_demanda():
    return render_template(MUSICIAN_HOME_HTML, demands=get_demandas())


def get_demandas():
    demandas = BancoDeDados.GetDemandas()
    musico_id = session.get("usuárioLogado")["id"]
    matches = [match.id_demanda for match in BancoDeDados.GetMatchesMusico(musico_id)]
    resultado = []

    for demanda in demandas:
        contratante = BancoDeDados.GetContratante(demanda.dono)
        imagem = BancoDeDados.GetImagemPerfil(contratante.id)
        dia, mes, ano = demanda.data_show.day, demanda.data_show.month, demanda.data_show.year
        resultado.append({
            'id': demanda.id,
            'situation': 'Match' if demanda.id in matches else 'Disponível',
            'image': imagem.caminho if imagem is not None else "",
            'contratante': contratante.nome_estabelecimento,
            'cidade': contratante.cidade,
            'estado': contratante.estado,
            'data': f"{dia:02d}/{mes:02d}/{ano:04d}",
            'estilos': BancoDeDados.GetEstilosMusicais(demanda.id),
            'equipamento': demanda.fornece_equipamento,
            'publico': demanda.publico_esperado,
            'duracao': demanda.duracao_show,
            'tipo_pagamento': demanda.tipo_pagamento.value,
            'momento_pagamento': demanda.momento_pagamento.value,
        })

    return resultado

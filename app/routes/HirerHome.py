from app import app
from flask import render_template, redirect, url_for, session, request
from app.models.BancoDeDados import BancoDeDados
from datetime import datetime


HIRER_HOME_HTML = "hirerHome.html"


@app.route("/homeContratante", methods=["POST"])
def home_contratante():
    return render_template(HIRER_HOME_HTML, demanda_estilos=get_demandas())


@app.route("/homeContratante", methods=["GET"])
def get_home_contratante():
    return render_template(HIRER_HOME_HTML, demanda_estilos=get_demandas())


@app.route("/homeContratantePosDemanda", methods=["GET"])
def get_home_contratante_pos_demanda():
    return render_template("hirerHome.html", demanda_estilos=get_demandas(), demanda='true')


@app.route("/procurarContratante", methods=["POST"])
def procurar():
    return render_template(HIRER_HOME_HTML, demanda_estilos=get_demandas())


@app.route("/procurarContratante", methods=["GET"])
def get_procurar():
    return render_template(HIRER_HOME_HTML, demanda_estilos=get_demandas())


@app.route("/cadastroDemanda", methods=["POST"])
def cadastro_demanda():
    return redirect(url_for("get_cadastrar_demanda"))


@app.route("/cadastroDemanda", methods=["GET"])
def get_cadastro_demanda():
    return redirect(url_for("get_cadastrar_demanda"))


@app.route("/verMusicos", methods=["GET"])
def ver_musicos():
    demanda_id = request.args.get("demanda_id")
    musicos = BancoDeDados().GetMatches(demanda_id)
    return render_template("verMusicos.html", musicos=musicos)


def get_estilos(demanda_id):
    estilos = BancoDeDados().GetEstilosMusicais(demanda_id)
    return estilos


def get_demandas():
    contratante_id = session.get("usuárioLogado")["id"]
    demandas = BancoDeDados().GetDemandas(contratante_id)
   
    demanda_estilos = []
    for demanda in demandas:
        demanda.data_show = datetime.strftime(demanda.data_show, "%d/%m/%Y")
        demanda.momento_pagamento = demanda.momento_pagamento.value
        estilos = get_estilos(demanda.id)
        num_matches = len(BancoDeDados().GetMatches(demanda.id))
        demanda_estilos.append((demanda, estilos, num_matches))

    return demanda_estilos
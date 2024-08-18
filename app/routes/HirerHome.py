from app import app
from flask import render_template, redirect, url_for, session, request
from app.models.BancoDeDados import BancoDeDados


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
    musicos = BancoDeDados().GetMusicos(demanda_id)
    return render_template("verMusicos.html", musicos=musicos)


def get_estilos(demanda_id):
    estilos = BancoDeDados().GetEstilosMusicais(demanda_id)
    return estilos


def get_demandas():
    contratante_id = session.get("usuárioLogado")["id"]
    demandas = BancoDeDados().GetDemandas(contratante_id)
   
    demanda_estilos = []
    for demanda in demandas:
        dia, mes, ano = demanda.data_show.day, demanda.data_show.month, demanda.data_show.year
        demanda.data_show = f"{dia:02d}/{mes:02d}/{ano:04d}"
        musicos = BancoDeDados().GetMusicos(demanda.id)
        imagens = [BancoDeDados.GetImagemPerfil(musico) for musico in musicos]
        imagens_caminho = [imagem.caminho for imagem in imagens if imagem.caminho][:9]

        demanda_estilos.append({
            'id': demanda.id,
            'images': imagens_caminho,
            'data_show': f"{dia:02d}/{mes:02d}/{ano:04d}",
            'estilos': BancoDeDados.GetEstilosMusicais(demanda.id),
            'fornece_equipamento': demanda.fornece_equipamento,
            'publico_esperado': demanda.publico_esperado,
            'duracao_show': demanda.duracao_show,
            'tipo_pagamento': demanda.tipo_pagamento.value,
            'momento_pagamento': demanda.momento_pagamento.value,
        })

    return demanda_estilos

from app import app
from flask import render_template

from app.models.BancoDeDados import BancoDeDados


@app.route("/homeMusico", methods=["POST"])
def home_musico():
    return render_template("musicianHome.html", demands=get_demandas())


@app.route("/homeMusico", methods=["GET"])
def get_home_musico():
    return render_template("musicianHome.html", demands=get_demandas())


def get_demandas():
    demandas = BancoDeDados.GetDemandas()
    resultado = []

    for demanda in demandas:
        contratante = BancoDeDados.GetContratante(demanda.dono)
        imagem = BancoDeDados.GetImagemPerfil(contratante.id)
        dia, mes, ano = demanda.data_show.day, demanda.data_show.month, demanda.data_show.year
        resultado.append({
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

from app import app
from app.models.BancoDeDados import BancoDeDados
from flask import render_template, request, session, redirect, url_for
from datetime import datetime, date

REGISTER_DEMANDS_HTML = "registerDemands.html"


@app.route("/cadastrarDemanda", methods=["POST"])
def cadastrar_demanda():
    data_show = request.form.get("data_show")
    raio_procurado = request.form.get("raio_procurado")
    estilos_marcados = request.form.getlist("estilo")
    equipamento_som = request.form.get("equipamento_som")
    publico_esperado = request.form.get("publico_esperado")
    duracao_show = request.form.get("duracao_show")
    pagamento = request.form.get("pagamento")
    modo_pagamento = request.form.get("modo_pagamento")
    confirmacao = False

    if data_show == "":
        return render_template(
            REGISTER_DEMANDS_HTML,
            data_show=data_show,
            raio_procurado=raio_procurado,
            estilo=estilos_marcados,
            equipamento_som=equipamento_som,
            publico_esperado=publico_esperado,
            duracao_show=duracao_show,
            pagamento=pagamento,
            modo_pagamento=modo_pagamento,
            confirmacao=confirmacao,
            error="Campos obrigatórios não preenchidos.",
        )

    try:
        data_py = datetime.strptime(data_show, "%d/%m/%Y")

        if data_py.date() < datetime.now().date():
            return render_template(
                REGISTER_DEMANDS_HTML,
                data_show=data_show,
                raio_procurado=raio_procurado,
                estilo=estilos_marcados,
                equipamento_som=equipamento_som,
                publico_esperado=publico_esperado,
                duracao_show=duracao_show,
                pagamento=pagamento,
                modo_pagamento=modo_pagamento,
                confirmacao=confirmacao,
                error="A data informada é anterior ao dia atual.",
            )
    except ValueError:
        return render_template(
            REGISTER_DEMANDS_HTML,
            data_show=data_show,
            raio_procurado=raio_procurado,
            estilo=estilos_marcados,
            equipamento_som=equipamento_som,
            publico_esperado=publico_esperado,
            duracao_show=duracao_show,
            pagamento=pagamento,
            modo_pagamento=modo_pagamento,
            confirmacao=confirmacao,
            error="A data informada é inválida.",
        )

    if (
        (len(estilos_marcados) == 0)
        or (publico_esperado == "")
        or (duracao_show == "")
        or pagamento is None
        or modo_pagamento is None
    ):
        return render_template(
            REGISTER_DEMANDS_HTML,
            data_show=data_show,
            raio_procurado=raio_procurado,
            estilo=estilos_marcados,
            equipamento_som=equipamento_som,
            publico_esperado=publico_esperado,
            duracao_show=duracao_show,
            pagamento=pagamento,
            modo_pagamento=modo_pagamento,
            confirmacao=confirmacao,
            error="Campos obrigatórios não preenchidos.",
        )

    confirmacao = True

    dia, mes, ano = [int(x) for x in data_show.split("/")]
    contratante = session.get("usuárioLogado")

    demanda = {
        "data_show": (ano, mes, dia),
        "raio_procurado": raio_procurado,
        "fornece_equipamento": True if equipamento_som == "on" else False,
        "publico_esperado": publico_esperado,
        "duracao_show": duracao_show,
        "tipo_pagamento": "Fixo" if pagamento == "fixo" else "Couvert",
        "momento_pagamento": "Antecipado"
        if modo_pagamento == "antecipado"
        else "Após o evento",
        "estilos": estilos_marcados,
        "dono": contratante["id"],
    }

    session["demanda"] = demanda

    return render_template(
        REGISTER_DEMANDS_HTML,
        data_show=data_show,
        raio_procurado=raio_procurado,
        estilo=estilos_marcados,
        equipamento_som=equipamento_som,
        publico_esperado=publico_esperado,
        duracao_show=duracao_show,
        pagamento=pagamento,
        modo_pagamento=modo_pagamento,
        confirmacao=confirmacao,
    )


@app.route("/cadastrarDemanda", methods=["GET"])
def get_cadastrar_demanda():
    return render_template(REGISTER_DEMANDS_HTML)


@app.route("/confirmarDemanda", methods=["POST"])
def confirmar_demanda():
    demanda = session.get("demanda", {})
    ano, mes, dia = demanda.get("data_show")
    demanda["data_show"] = date(ano, mes, dia)
    BancoDeDados().CriaDemanda(demanda)
    return redirect(url_for("get_home_contratante_pos_demanda"))

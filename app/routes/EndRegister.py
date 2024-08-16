from flask import render_template, request, redirect, url_for, session
from app import app
from datetime import date
from app.models.BancoDeDados import BancoDeDados

FINAL_CADASTRO_HTML = "endRegister.html"


@app.route("/setinhaFimCadastro", methods=["GET"])
def seta_fim_cadastro():
    return redirect(url_for("get_cadastro"))


@app.route("/finalCadastro", methods=["POST"])
def valida_dados():
    numero = request.form.get("numeroCartao")
    nome = request.form.get("nomeCartao")
    cod_seg = request.form.get("codigoSeguranca")
    data = request.form.get("dataExpiracao")

    if (
        numero.strip() == ""
        or nome.strip() == ""
        or cod_seg.strip() == ""
        or data.strip() == ""
    ):
        return render_template(
            FINAL_CADASTRO_HTML,
            error="Campos obrigatórios não preenchidos.",
            dataExpiracao=data,
            nomeCartao=nome,
            numeroCartao=numero,
            codigoSeguranca=cod_seg,
        )

    mes, ano = map(int, data.split("/"))
    if ano <= 49:
        ano += 2000
    else:
        ano += 1900

    if data.strip() != "" and (
        date.today().year > ano
        or (date.today().year == ano and date.today().month > mes)
        or mes > 12
    ):
        return render_template(
            FINAL_CADASTRO_HTML,
            error="A data de expiração do cartão é inválida.",
            dataExpiracao=data,
            nomeCartao=nome,
            numeroCartao=numero,
            codigoSeguranca=cod_seg,
        )

    pessoa = session.get("pessoa")
    tipo = pessoa["tipo"]
    if tipo == "M":
        pessoa_id = BancoDeDados.CriaMusico(pessoa)
    else:
        pessoa_id = BancoDeDados.CriaContratante(pessoa)

    dados_cartao = {
        "id": pessoa_id,
        "num_cartao": numero,
        "nome_cartao": nome,
        "cod_seguranca": cod_seg,
        "validade": data,
    }

    BancoDeDados.CriaDadosBancario(dados_cartao)
    return redirect(url_for("get_entrar_login"))


@app.route("/finalCadastro", methods=["GET"])
def get_final_cadastro():
    return render_template(FINAL_CADASTRO_HTML)

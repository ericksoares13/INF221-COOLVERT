from flask import render_template, request, redirect, url_for, session
from app import app
import re
from datetime import date
from app.models.BancoDeDados import BancoDeDados

@app.route("/setinhaFimCadastro", methods=["GET"])
def setinhaFimCadastro():
    return redirect(url_for("get_cadastro"))

@app.route("/finalCadastro", methods=["GET"])
def getFinalCadastro():
    return render_template("FinalCadastro.html")

@app.route("/finalCadastro", methods=["POST"])
def validaDados():
    numero = request.form.get("numeroCartao")
    nome = request.form.get("nomeCartao")
    codSeg = request.form.get("codigoSeguranca")
    data = request.form.get("dataExpiracao")

    mes, ano = map(int, data.split('/'))
    if ano <= 49: 
        ano += 2000
    else: ano += 1900

    if not data.strip() == "" and (date.today().year > ano or (date.today().year == ano and date.today().month + 1 > mes) or mes + 1 > 12): 
        return render_template(
            "finalCadastro.html",
            error="A data de expiração do cartão é inválida.",
            data=data,
        )
    
    pessoa = session.get('pessoa')
    tipo = pessoa['tipo']
    if tipo == 'M':
        pessoa_id = BancoDeDados.CriaMusico(pessoa)
    else: pessoa_id = BancoDeDados.CriaContratante(pessoa)

    dados_cartao = {
        'id': pessoa_id,
        'num_cartao': numero,
        'nome_cartao': nome,
        'cod_seguranca': codSeg,
        'validade': data
    }

    BancoDeDados.CriaDadosBancario(dados_cartao)    

    return redirect(url_for("get_cadastro"))



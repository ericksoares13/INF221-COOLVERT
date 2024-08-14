from app import app
from flask import render_template, request, redirect, url_for, session
from validate_docbr import CPF
import re

from app.models.BancoDeDados import BancoDeDados

MUSICIAN_HTML = "musicianRegister.html"


@app.route("/cadastrarMusico", methods=["POST"])
def cadastrar_musico():
    nome = request.form.get("nome")
    nome_artistico = request.form.get("nome_artistico")
    cpf = request.form.get("cpf")
    telefone = request.form.get("telefone")
    descricao = request.form.get("descricao")

    if cpf != "" and not CPF().validate(cpf):
        return render_template(
            MUSICIAN_HTML,
            error="CPF inválido.",
            nome=nome,
            nome_artistico=nome_artistico,
            cpf=cpf,
            telefone=telefone,
            descricao=descricao,
        )

    if telefone != "" and not re.match(r"^\(\d{2}\) \d{5}-\d{4}$", telefone):
        return render_template(
            MUSICIAN_HTML,
            error="Celular inválido.",
            nome=nome,
            nome_artistico=nome_artistico,
            cpf=cpf,
            telefone=telefone,
            descricao=descricao,
        )

    if nome == "" or cpf == "" or telefone == "":
        return render_template(
            MUSICIAN_HTML,
            error="Campos obrigatórios não preenchidos.",
            nome=nome,
            nome_artistico=nome_artistico,
            cpf=cpf,
            telefone=telefone,
            descricao=descricao,
        )

    musico = session.get('pessoa', {})
    musico.update({
        'nome_pessoal': nome,
        'nome_artistico': nome_artistico,
        'documento': cpf,
        'celular': telefone,
        'descricao': descricao
    })

    session['pessoa'] = {
        'pessoa': musico,
        'tipo': 'M'
    }

    return redirect(url_for("index"))


@app.route("/cadastrarMusico", methods=["GET"])
def get_cadastrar_musico():
    return render_template(MUSICIAN_HTML)

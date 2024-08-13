from app import app
from flask import render_template, redirect, url_for


@app.route("/cadastrarMusico", methods=["POST"])
def cadastrar_musico():
    nome = request.form.get("nome")
    nome_artistico = request.form.get("nome_artistico")
    cpf = request.form.get("cpf")
    telefone = request.form.get("telefone")
    descricao = request.form.get("descricao")

    if cnpj != "" and not CPF().validate(cpf):
        return render_template(
            "hirerRegister.html",
            error="CNPJ inválido.",
            nome=nome,
            cnpj=cnpj,
            telefone=telefone,
            cep=cep,
            estado=estado,
            cidade=cidade,
            bairro=bairro,
            numero=numero,
            complemento=complemento,
        )
    return render_template("musicianRegister.html")


@app.route("/cadastrarMusico", methods=["GET"])
def get_cadastrar_musico():
    return render_template("musicianRegister.html")

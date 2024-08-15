from app import app
from flask import render_template, request, redirect, url_for, session
from validate_docbr import CNPJ
import re

HIRER_HTML = "hirerRegister.html"


@app.route("/cadastrarContratante", methods=["POST"])
def cadastrar_contratante():
    nome = request.form.get("nome")
    cnpj = request.form.get("cnpj")
    telefone = request.form.get("telefone")
    cep = request.form.get("cep")
    estado = request.form.get("estado")
    cidade = request.form.get("cidade")
    bairro = request.form.get("bairro")
    numero = request.form.get("numero")
    complemento = request.form.get("complemento")

    if cnpj != "" and not CNPJ().validate(cnpj):
        return render_template(
            HIRER_HTML,
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

    if cep != "" and (estado == "" or cidade == "" or bairro == ""):
        return render_template(
            HIRER_HTML,
            error="CEP inválido.",
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

    if telefone != "" and not re.match(r"^\(\d{2}\) \d{5}-\d{4}$", telefone):
        return render_template(
            HIRER_HTML,
            error="Celular inválido.",
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

    if nome == "" or cnpj == "" or telefone == "" or cep == "" or numero == "":
        return render_template(
            HIRER_HTML,
            error="Campos obrigatórios não preenchidos.",
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

    contratante = session.get('pessoa', {})
    contratante.update({
        'nome_estabelecimento': nome,
        'documento': cnpj,
        'celular': telefone,
        'cep': cep,
        'estado': estado,
        'cidade': cidade,
        'bairro': bairro,
        'numero': numero,
        'complemento': complemento
    })

    session['pessoa'] = contratante

    return redirect(url_for("getFinalCadastro"))


@app.route("/cadastrarContratante", methods=["GET"])
def get_cadastrar_contratante():
    return render_template(HIRER_HTML)

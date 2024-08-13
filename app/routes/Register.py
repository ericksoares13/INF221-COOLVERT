import re

from app import app
from flask import render_template, request, redirect, url_for, session

from app.models.BancoDeDados import BancoDeDados

REGISTER_HTML = "register.html"


@app.route("/cadastro", methods=["POST"])
def cadastro():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")
    user_type = request.form.get("user_type")

    if email.strip() != "" and not re.match(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email
    ):
        return render_template(
            REGISTER_HTML,
            error="Email inválido.",
            email=email,
            username=username,
            password=password,
            confirm_password=confirm_password,
            user_type=user_type,
        )

    if email.strip() != '' and not BancoDeDados.VerificaEmail(email):
        return render_template(REGISTER_HTML,
                               error='Email digitado já está em uso.',
                               email=email,
                               username=username,
                               password=password,
                               confirm_password=confirm_password,
                               user_type=user_type)

    # if username.strip() != '' and verificarSeJaExiste:
    #     return render_template(REGISTER_HTML,
    #                            error='Nome de usuário digitado já está em uso.',
    #                            email=email,
    #                            username=username,
    #                            password=password,
    #                            confirm_password=confirm_password,
    #                            user_type=user_type)

    if password.strip() != "" and not re.match(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$", password
    ):
        return render_template(
            REGISTER_HTML,
            error="Senha não atende os requisitos necessários.",
            email=email,
            username=username,
            password=password,
            confirm_password=confirm_password,
            user_type=user_type,
        )

    if (
        email.strip() == ""
        or username.strip() == ""
        or password.strip() == ""
        or confirm_password.strip() == ""
        or user_type is None
    ):
        return render_template(
            REGISTER_HTML,
            error="Campos obrigatórios não preenchidos.",
            email=email,
            username=username,
            password=password,
            confirm_password=confirm_password,
            user_type=user_type,
        )

    if password != confirm_password:
        return render_template(
            REGISTER_HTML,
            error="As senhas não coincidem.",
            email=email,
            username=username,
            password=password,
            confirm_password=confirm_password,
            user_type=user_type,
        )

    pessoa_id = BancoDeDados.CriaPessoa({
        'nome': username,
        'email': email,
        'senha': password,
        'tipo': 'M' if user_type is "musico" else 'C'
    })

    session['pessoa_id'] = pessoa_id

    if user_type == "musico":
        return redirect(url_for("get_cadastrar_musico"))
    else:
        return redirect(url_for("get_cadastrar_contratante"))


@app.route("/cadastro", methods=["GET"])
def get_cadastro():
    return render_template(REGISTER_HTML)

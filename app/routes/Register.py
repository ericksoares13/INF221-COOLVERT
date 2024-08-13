import re

from app import app
from flask import render_template, request, redirect, url_for

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
            invalid_email_error="Email inválido.",
            email=email,
            username=username,
            password=password,
            confirm_password=confirm_password,
            user_type=user_type,
        )

    # if email.strip() != '' and verificarSeJaExiste:
    #     return render_template(REGISTER_HTML,
    #                            used_email_error='Email digitado já está em uso.',
    #                            email=email,
    #                            username=username,
    #                            password=password,
    #                            confirm_password=confirm_password,
    #                            user_type=user_type)

    # if username.strip() != '' and verificarSeJaExiste:
    #     return render_template(REGISTER_HTML,
    #                            used_email_error='Nome de usuário digitado já está em uso.',
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
            invalid_password_error="Senha não atende os requisitos necessários.",
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
            required_fields_error="Campos obrigatórios não preenchidos.",
            email=email,
            username=username,
            password=password,
            confirm_password=confirm_password,
            user_type=user_type,
        )

    if password != confirm_password:
        return render_template(
            REGISTER_HTML,
            pasword_error="As senhas não coincidem.",
            email=email,
            username=username,
            password=password,
            confirm_password=confirm_password,
            user_type=user_type,
        )

    if user_type == "musico":
        return redirect(url_for("musicoRegister.html"))
    else:
        return redirect(url_for("contratanteRegister.html"))


@app.route("/cadastro", methods=["GET"])
def get_cadastro():
    return render_template(REGISTER_HTML)

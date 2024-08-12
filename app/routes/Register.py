import re

from app import app
from flask import render_template, request


@app.route("/cadastro", methods=["POST"])
def cadastro():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    if not email.strip() == "" and not re.match(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email
    ):
        return render_template(
            "register.html",
            invalid_email_error="Email inválido.",
            email=email,
            username=username,
            password=password,
            confirm_password=confirm_password,
        )

    # if not email.strip() == "" and verificarSeJaExiste:
    #     return render_template('register.html',
    #                            used_email_error="Email digitado já está em uso.",
    #                            email=email,
    #                            username=username,
    #                            password=password,
    #                            confirm_password=confirm_password)

    # if not username.strip() == "" and verificarSeJaExiste:
    #     return render_template('register.html',
    #                            used_email_error="Nome de usuário digitado já está em uso.",
    #                            email=email,
    #                            username=username,
    #                            password=password,
    #                            confirm_password=confirm_password)

    if not password.strip() == "" and not re.match(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$", password
    ):
        return render_template(
            "register.html",
            invalid_password_error="Senha não atende os requisitos necessários.",
            email=email,
            username=username,
            password=password,
            confirm_password=confirm_password,
        )

    if (
        email.strip() == ""
        or username.strip() == ""
        or password.strip() == ""
        or confirm_password.strip() == ""
    ):
        return render_template(
            "register.html",
            required_fields_error="Campos obrigatórios não preenchidos.",
            email=email,
            username=username,
            password=password,
            confirm_password=confirm_password,
        )

    if password != confirm_password:
        return render_template(
            "register.html",
            pasword_error="As senhas não coincidem.",
            email=email,
            username=username,
            password=password,
            confirm_password=confirm_password,
        )

    return render_template("userType.html")

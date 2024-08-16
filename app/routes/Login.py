from flask import render_template, request, redirect, url_for, session
from app import app
from app.models.BancoDeDados import BancoDeDados

LOGIN_HTML = "login.html"


@app.route("/setinhaLogin", methods=["GET"])
def seta_login():
    return redirect(url_for("index"))


@app.route("/vaiParaCadastro", methods=["GET"])
def vai_para_cadastro():
    return redirect(url_for("get_cadastro"))


@app.route("/entrarLogin", methods=["POST"])
def valida_login_senha():
    email = request.form.get("emailLogin")
    senha = request.form.get("senhaLogin")

    if email.strip() == "" or senha.strip() == "":
        return render_template(
            LOGIN_HTML,
            error="Campos obrigatórios não preenchidos.",
            emailLogin=email,
            senhaLogin=senha,
        )

    login = {"identificador": email, "senha": senha}

    pessoa = BancoDeDados.Login(login)
    if pessoa is not None:
        session["usuárioLogado"] = {
            "id": pessoa.id,
            "nome": pessoa.nome,
            "email": pessoa.email,
            "tipo": pessoa.tipo,
        }
        if pessoa.tipo == "C":
            return redirect(url_for("get_home_contratante"))
        else:
            return redirect(url_for("get_home_musico"))
    else:
        return render_template(
            LOGIN_HTML,
            error="Email ou senha inválidos.",
            emailLogin=email,
            senhaLogin=senha,
        )


@app.route("/entrarLogin", methods=["GET"])
def get_entrar_login():
    return render_template(LOGIN_HTML)

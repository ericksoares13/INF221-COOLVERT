from flask import render_template, request, redirect, url_for, session
from app import app
import re
from app.models.BancoDeDados import BancoDeDados

@app.route("/setinhaLogin", methods=["GET"])
def setinhaLogin():
    return redirect(url_for("index"))

@app.route("/vaiParaCadastro", methods=["GET"])
def vaiParaCadastro():
    return redirect(url_for("get_cadastro")) 

@app.route("/entrarLogin", methods=["POST"])
def validaLoginESenha():
    email = request.form.get("emailLogin")
    senha = request.form.get("senhaLogin")

    print(type(email), type(senha))

    if email.strip() == "" or senha.strip() == "":
        return render_template(
            "Login.html",
            error="Campos obrigatórios não preenchidos.",
            emailLogin=email,
            senhaLogin=senha  
        )  
    
    login = {
        'email': email,
        'senha': senha
    }

    pessoa = BancoDeDados.Login(login)
    if pessoa != None:
        session['usuárioLogado'] = pessoa
        if pessoa['tipo'] == 'C':
            return redirect(url_for("get_home_contratante"))
        # falta colocar return para homemúsico
    else:
        return render_template(
            "Login.html",
            error="Email ou senha inválidos.",
            emailLogin=email,
            senhaLogin=senha  
        )  

@app.route("/entrarLogin", methods=["GET"])
def getEntrarLogin():
    return render_template("login.html")
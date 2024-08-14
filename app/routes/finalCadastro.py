from flask import render_template, request, redirect, url_for
from app import app
import re
from datetime import date

@app.route("/setinhaFimCadastro", methods=["GET"])
def setinhaFimCadastro():
    return redirect(url_for("get_cadastro"))

@app.route("/finalCadastro", methods=["GET"])
def getFinalCadastro():
    return render_template("FinalCadastro.html")

@app.route("/finalCadastro", methods=["POST"])
def validaDados():
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
    
    return redirect(url_for("get_cadastro"))

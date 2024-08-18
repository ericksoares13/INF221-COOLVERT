from app import app
from flask import render_template, redirect, url_for


@app.route("/homeContratante", methods=["POST"])
def home_contratante():
    return render_template("hirerHome.html")


@app.route("/homeContratante", methods=["GET"])
def get_home_contratante():
    return render_template("hirerHome.html")

@app.route("/homeContratantePosDemanda", methods=["GET"])
def get_home_contratante_pos_demanda():
    return render_template("hirerHome.html", demanda='true')


@app.route("/procurarContratante", methods=["POST"])
def procurar():
    return render_template("hirerHome.html")


@app.route("/procurarContratante", methods=["GET"])
def get_procurar():
    return render_template("hirerHome.html")


@app.route("/cadastroDemanda", methods=["POST"])
def cadastro_demanda():
    return redirect(url_for("get_cadastrar_demanda"))


@app.route("/cadastroDemanda", methods=["GET"])
def get_cadastro_demanda():
    return redirect(url_for("get_cadastrar_demanda"))

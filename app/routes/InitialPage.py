from app import app
from flask import render_template, redirect, url_for


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    return redirect(url_for("get_cadastro"))


@app.route("/cadastrar", methods=["GET"])
def get_cadastrar():
    return redirect(url_for("get_cadastro"))


@app.route("/entrar", methods=["POST"])
def entrar():
    return redirect(url_for("get_entrar_login"))


@app.route("/entrar", methods=["GET"])
def get_entrar():
    return redirect(url_for("get_entrar_login"))

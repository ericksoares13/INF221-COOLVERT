from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    return render_template("register.html")


@app.route("/cadastrar", methods=["GET"])
def get_cadastrar():
    return render_template("register.html")


@app.route("/entrar", methods=["POST"])
def entrar():
    return "", 204


@app.route("/entrar", methods=["GET"])
def get_entrar():
    return "", 204

from app import app
from flask import render_template, redirect, url_for


@app.route("/cadastrarContratante", methods=["POST"])
def cadastrar_contratante():
    return render_template("hirerRegister.html")


@app.route("/cadastrarContratante", methods=["GET"])
def get_cadastrar_contratante():
    return render_template("hirerRegister.html")

from app import app
from flask import render_template, redirect, url_for


@app.route("/cadastrarMusico", methods=["POST"])
def cadastrar_musico():
    return render_template("musicianRegister.html")


@app.route("/cadastrarMusico", methods=["GET"])
def get_cadastrar_musico():
    return render_template("musicianRegister.html")

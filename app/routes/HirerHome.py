from app import app
from flask import render_template, request, redirect, url_for, session
from validate_docbr import CNPJ
import re


@app.route("/homeContratante", methods=["POST"])
def home_contratante():
    return render_template("home_contratante.html")


@app.route("/homeContratante", methods=["GET"])
def get_home_contratante():
    return render_template("home_contratante.html")


@app.route("/procurar", methods=["POST"])
def procurar():
    return render_template("home_contratante.html")


@app.route("/procurar", methods=["GET"])
def get_procurar():
    return render_template("home_contratante.html")


@app.route("/cadastrarDemanda", methods=["POST"])
def cadastrar_demanda():
    return render_template("home_contratante.html")


@app.route("/cadastrarDemanda", methods=["GET"])
def get_cadastrar_demanda():
    return render_template("home_contratante.html")

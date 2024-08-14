from flask import render_template, request, redirect, url_for
from app import app
import re
    
@app.route("/setinhaLogin", methods=["GET"])
def setinhaLogin():
    return redirect(url_for("index"))

@app.route("/vaiParaCadastro", methods=["GET"])
def vaiParaCadastro():
    return redirect(url_for("get_cadastro"))

@app.route("/entrarLogin", methods=["GET"])
def getEntrarLogin():
    return render_template("login.html")

    
    
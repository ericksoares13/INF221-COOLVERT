from app import app
from flask import render_template


@app.route("/homeMusico", methods=["POST"])
def home_musico():
    return render_template("musicianHome.html")


@app.route("/homeMusico", methods=["GET"])
def get_home_musico():
    return render_template("musicianHome.html")


@app.route("/availableDemands")
def available_demands():
    return render_template("available_demands.html")

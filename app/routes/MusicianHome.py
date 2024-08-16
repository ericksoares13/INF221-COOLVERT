from app import app
from flask import render_template, request, redirect, url_for, session
from validate_docbr import CNPJ
import re

@app.route('/musicianHome')
def musician_home():
    return render_template('home_musico.html')

@app.route('/availableDemands')
def available_demands():
    # Lógica para exibir demandas disponíveis
    return render_template('available_demands.html')

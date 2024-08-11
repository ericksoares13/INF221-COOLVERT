from app import app
from flask import Flask, render_template

@app.route('/cadastrarDemanda', methods=['POST'])
def cadastrarDemanda():
    return render_template('registerDemands.html')

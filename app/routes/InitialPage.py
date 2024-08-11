from app import app
from flask import Flask, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    return '', 204

@app.route('/entrar', methods=['POST'])
def entrar():
    return '', 204

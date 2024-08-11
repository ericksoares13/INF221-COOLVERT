from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    return render_template('register.html')

@app.route('/entrar', methods=['POST'])
def entrar():
    return '', 204

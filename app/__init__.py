from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bd = SQLAlchemy(app)

# Importar as rotas para registrar os endpoints
from app.routes import InitialPage, Register, RegistroContratante, RegistroMusico, finalCadastro, login

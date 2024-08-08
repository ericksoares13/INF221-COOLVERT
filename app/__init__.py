from flask import Flask

app = Flask(__name__)

# Importar as rotas para registrar os endpoints
from app import routes

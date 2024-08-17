from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "default_secret_key")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

bd = SQLAlchemy(app)

from app.routes import (
    ChatHirer,
    ChatMusician,
    EndRegister,
    HirerHome,
    HirerRegister,
    InitialPage,
    Login,
    MusicianHome,
    MusicianRegister,
    Register,
    RegisterDemands,
)

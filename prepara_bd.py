from app import app, bd
from app.models import *
from app.models.BancoDeDados import BancoDeDados
Usuario

if __name__ == '__main__':
    print(BancoDeDados.Login('teste@example.com', '123'))

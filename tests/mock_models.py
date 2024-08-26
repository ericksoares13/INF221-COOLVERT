from unittest.mock import MagicMock
from enum import Enum
import datetime

# Mocks das classes dependentes
class Mensagem:
    def __init__(self, match, dono, mensagem):
        self.match = match
        self.dono = dono
        self.mensagem = mensagem
        self.horario = datetime.datetime.now()

    query = MagicMock()

class TipoFotoEnum(Enum):
    PERFIL = "Perfil"
    INSTAGRAM = "Instagram"
    PORTFOLIO = "portfólio"

class Imagem:
    def __init__(self, dono, nome, tipo_foto, caminho):
        self.dono = dono
        self.nome = nome
        self.tipo_foto = tipo_foto
        self.caminho = caminho

    query = MagicMock()

class Pessoa:
    query = MagicMock()

class Contratante:
    query = MagicMock()
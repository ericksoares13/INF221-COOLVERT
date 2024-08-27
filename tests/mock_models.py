from exceptions import ValorNuloError, TipoIncorretoError
from unittest.mock import MagicMock
from enum import Enum
import datetime

# Mocks das classes dependentes
class Mensagem:
    def __init__(self, match, dono, mensagem):
        # Validações
        if not match:
            raise ValorNuloError("O campo 'match' não pode ser vazio ou nulo.")
        elif not isinstance(match, int):
            raise TipoIncorretoError("O campo 'match' deve ser um inteiro não nulo.")
        
        if not dono:
            raise ValorNuloError("O campo 'dono' não pode ser vazio ou nulo.")
        elif not isinstance(dono, int):
            raise TipoIncorretoError("O campo 'dono' deve ser um inteiro não nulo.")
        
        if not mensagem:
            raise ValorNuloError("O campo 'mensagem' não pode ser vazio ou nulo.")
        
        # Criando a instância
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
        # Validações
        if not dono:
            raise ValorNuloError("O campo 'dono' não pode ser vazio ou nulo.")
        elif not isinstance(dono, int):
            raise TipoIncorretoError("O campo 'dono' deve ser um inteiro não nulo.")
        
        if not nome:
            raise ValorNuloError("O campo 'nome' não pode ser vazio ou nulo.")
        
        if not isinstance(tipo_foto, TipoFotoEnum):
            raise TipoIncorretoError("O campo 'tipo_foto' deve ser uma instância de TipoFotoEnum.")
        
        if not caminho:
            raise ValorNuloError("O campo 'caminho' não pode ser vazio ou nulo.")
        
        # Criando a instância
        self.dono = dono
        self.nome = nome
        self.tipo_foto = tipo_foto
        self.caminho = caminho

    query = MagicMock()

class Pessoa:
    query = MagicMock()

class Contratante:
    query = MagicMock()
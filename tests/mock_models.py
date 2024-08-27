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
            raise TipoIncorretoError(
                "O campo 'tipo_foto' deve ser uma instância de TipoFotoEnum."
            )

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


class Match:
    id = None
    id_musico = None
    id_demanda = None

    def __init__(self, id_musico, id_demanda):
        if id_musico is None:
            raise ValorNuloError("O campo 'id_musico' não pode ser vazio ou nulo.")
        elif not isinstance(id_musico, int):
            raise TipoIncorretoError("O campo 'id_musico' deve ser um inteiro não nulo.")

        if id_demanda is None:
            raise ValorNuloError("O campo 'id_demanda' não pode ser vazio ou nulo.")
        elif not isinstance(id_demanda, int):
            raise TipoIncorretoError("O campo 'id_demanda' deve ser um inteiro não nulo.")

        self.set_id_musico = id_musico
        self.set_id_demanda = id_demanda

    query = MagicMock()


class EstiloMusical:
    id = None
    nome = None
    def __init__(self, nome):
        # Validações
        if nome is None:
            raise ValorNuloError("O campo 'nome' não pode ser vazio ou nulo.")
        elif not isinstance(nome, str):
            raise TipoIncorretoError("O campo 'nome' deve ser uma string não nula.")

        # Criando a instância
        self.nome = nome
        
    query = MagicMock()


class DemandaEstilos:
    query = MagicMock()


class TipoPagamentoEnum(Enum):
    FIXO = "Fixo"
    COUVERT = "Couvert"


class MomentoPagamentoEnum(Enum):
    APOS_EVENTO = "Após o evento"
    ANTECIPADO = "Antecipado"


class Demanda:
    id = None
    data_show = None
    raio_procurado = None
    fornece_equipamento = None
    publico_esperado = None
    duracao_show = None
    visivel = None
    tipo_pagamento = None
    momento_pagamento = None
    estilos = None
    dono = None

    def __init__(
        self,
        id,
        data_show,
        raio_procurado,
        fornece_equipamento,
        publico_esperado,
        duracao_show,
        visivel,
        tipo_pagamento,
        momento_pagamento,
        estilos,
        dono,
    ):
        if id is None:
            raise ValorNuloError("O campo 'id' não pode ser vazio ou nulo.")
        elif not isinstance(id, int):
            raise TipoIncorretoError("O campo 'id' deve ser um inteiro não nulo.")

        if data_show is None:
            raise ValorNuloError("O campo 'data_show' não pode ser vazio ou nulo.")
        try:
            if isinstance(data_show, str):
                data_show = datetime.datetime.strptime(
                    data_show, "%Y-%m-%d"
                ).date()  # Ajuste o formato se necessário
            elif not isinstance(data_show, datetime.date):
                raise TipoIncorretoError("O campo 'data_show' deve ser do tipo date.")
        except ValueError:
            raise TipoIncorretoError("O campo 'data_show' deve ser uma data válida.")
        if data_show < datetime.date.today():
            raise TipoIncorretoError(
                "O campo 'data_show' não pode ser uma data no passado."
            )

        if raio_procurado is None:
            raise ValorNuloError("O campo 'raio_procurado' não pode ser vazio ou nulo.")
        elif not isinstance(raio_procurado, (int, float)):
            raise TipoIncorretoError(
                "O campo 'raio_procurado' deve ser um número não nulo."
            )

        if fornece_equipamento is None:
            raise ValorNuloError(
                "O campo 'fornece_equipamento' não pode ser vazio ou nulo."
            )
        elif not isinstance(fornece_equipamento, bool):
            raise TipoIncorretoError(
                "O campo 'fornece_equipamento' deve ser um booleano não nulo."
            )

        if publico_esperado is None:
            raise ValorNuloError(
                "O campo 'publico_esperado' não pode ser vazio ou nulo."
            )
        elif not isinstance(publico_esperado, int):
            raise TipoIncorretoError(
                "O campo 'publico_esperado' deve ser um inteiro não nulo."
            )

        if duracao_show is None:
            raise ValorNuloError("O campo 'duracao_show' não pode ser vazio ou nulo.")
        elif not isinstance(duracao_show, str):
            raise TipoIncorretoError(
                "O campo 'duracao_show' deve ser uma string não nula."
            )

        if visivel is None:
            raise ValorNuloError("O campo 'visivel' não pode ser vazio ou nulo.")
        elif not isinstance(visivel, bool):
            raise TipoIncorretoError("O campo 'visivel' deve ser um booleano não nulo.")

        if tipo_pagamento is None:
            raise ValorNuloError("O campo 'tipo_pagamento' não pode ser vazio ou nulo.")
        elif tipo_pagamento not in (TipoPagamentoEnum.FIXO, TipoPagamentoEnum.COUVERT):
            raise TipoIncorretoError(
                "O campo 'tipo_pagamento' deve ser 'Fixo' ou 'Couvert'."
            )

        if momento_pagamento is None:
            raise ValorNuloError(
                "O campo 'momento_pagamento' não pode ser vazio ou nulo."
            )
        elif momento_pagamento not in (
            MomentoPagamentoEnum.ANTECIPADO,
            MomentoPagamentoEnum.APOS_EVENTO,
        ):
            raise TipoIncorretoError(
                "O campo 'momento_pagamento' deve ser 'Antecipado' ou 'Após o evento'."
            )

        if estilos is None:
            raise ValorNuloError("O campo 'estilos' não pode ser vazio ou nulo.")
        elif not isinstance(estilos, list):
            raise TipoIncorretoError("O campo 'estilos' deve ser uma lista não nula.")

        if dono is None:
            raise ValorNuloError("O campo 'dono' não pode ser vazio ou nulo.")
        elif not isinstance(dono, int):
            raise TipoIncorretoError("O campo 'dono' deve ser um inteiro não nulo.")

        self.id = id
        self.data_show = data_show
        self.raio_procurado = raio_procurado
        self.fornece_equipamento = fornece_equipamento
        self.publico_esperado = publico_esperado
        self.duracao_show = duracao_show
        self.visivel = visivel
        self.tipo_pagamento = tipo_pagamento
        self.momento_pagamento = momento_pagamento
        self.estilos = estilos
        self.dono = dono

    query = MagicMock()

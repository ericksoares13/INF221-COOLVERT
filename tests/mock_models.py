from enum import Enum
from exceptions import TipoIncorretoError, ValorNuloError
from unittest.mock import MagicMock
import datetime


class Contratante:
    def __init__(self, id, nome_estabelecimento, cep, estado, cidade, bairro, numero, complemento):
        if not isinstance(id, int):
            raise TipoIncorretoError("O campo 'id' deve ser um inteiro não nulo.")

        if not nome_estabelecimento:
            raise ValorNuloError("O campo 'nome_estabelecimento' não pode ser vazio ou nulo.")
        if not isinstance(nome_estabelecimento, str):
            raise TipoIncorretoError("O campo 'nome_estabelecimento' deve ser uma string não nula.")

        if not cep:
            raise ValorNuloError("O campo 'cep' não pode ser vazio ou nulo.")
        if not isinstance(cep, str):
            raise TipoIncorretoError("O campo 'cep' deve ser uma string não nula.")

        if not estado:
            raise ValorNuloError("O campo 'estado' não pode ser vazio ou nulo.")
        if not isinstance(estado, str):
            raise TipoIncorretoError("O campo 'estado' deve ser uma string não nula.")

        if not cidade:
            raise ValorNuloError("O campo 'cidade' não pode ser vazio ou nulo.")
        if not isinstance(cidade, str):
            raise TipoIncorretoError("O campo 'cidade' deve ser uma string não nula.")

        if not bairro:
            raise ValorNuloError("O campo 'bairro' não pode ser vazio ou nulo.")
        if not isinstance(bairro, str):
            raise TipoIncorretoError("O campo 'bairro' deve ser uma string não nula.")

        if not numero:
            raise ValorNuloError("O campo 'numero' não pode ser vazio ou nulo.")
        if not isinstance(numero, str):
            raise TipoIncorretoError("O campo 'numero' deve ser uma string não nula.")

        if not complemento:
            raise ValorNuloError("O campo 'complemento' não pode ser vazio ou nulo.")
        if not isinstance(complemento, str):
            raise TipoIncorretoError("O campo 'complemento' deve ser uma string não nula.")

        self.id = id
        self.nome_estabelecimento = nome_estabelecimento
        self.cep = cep
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.numero = numero
        self.complemento = complemento

    query = MagicMock()


class DadosBancario:
    def __init__(self, id, num_cartao, nome_cartao, cod_seguranca, validade):
        # Validações
        if not isinstance(id, int):
            raise TipoIncorretoError("O campo 'id' deve ser um inteiro não nulo.")

        if not num_cartao:
            raise ValorNuloError("O campo 'num_cartao' não pode ser vazio ou nulo.")
        if not isinstance(num_cartao, str):
            raise TipoIncorretoError("O campo 'num_cartao' deve ser uma string não nula.")

        if not nome_cartao:
            raise ValorNuloError("O campo 'nome_cartao' não pode ser vazio ou nulo.")
        if not isinstance(nome_cartao, str):
            raise TipoIncorretoError("O campo 'nome_cartao' deve ser uma string não nula.")

        if not cod_seguranca:
            raise ValorNuloError("O campo 'cod_seguranca' não pode ser vazio ou nulo.")
        if not isinstance(cod_seguranca, str):
            raise TipoIncorretoError("O campo 'cod_seguranca' deve ser uma string não nula.")

        if not validade:
            raise ValorNuloError("O campo 'validade' não pode ser vazio ou nulo.")
        if not isinstance(validade, str):
            raise TipoIncorretoError("O campo 'validade' deve ser uma string não nula.")

        self.id = id
        self.num_cartao = num_cartao
        self.nome_cartao = nome_cartao
        self.cod_seguranca = cod_seguranca
        self.validade = validade

    query = MagicMock()


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
                ).date()
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


class DemandaEstilos:
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

        self.dono = dono
        self.nome = nome
        self.tipo_foto = tipo_foto
        self.caminho = caminho

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

        self.match = match
        self.dono = dono
        self.mensagem = mensagem
        self.horario = datetime.datetime.now()

    query = MagicMock()


class MomentoPagamentoEnum(Enum):
    APOS_EVENTO = "Após o evento"
    ANTECIPADO = "Antecipado"


class Musico:
    def __init__(self, id, nome_pessoal, nome_artistico, descricao):
        # Validações
        if not isinstance(id, int):
            raise TipoIncorretoError("O campo 'id' deve ser um inteiro não nulo.")

        if not nome_pessoal:
            raise ValorNuloError("O campo 'nome_pessoal' não pode ser vazio ou nulo.")
        if not isinstance(nome_pessoal, str):
            raise TipoIncorretoError("O campo 'nome_pessoal' deve ser uma string não nula.")

        if not nome_artistico:
            raise ValorNuloError("O campo 'nome_artistico' não pode ser vazio ou nulo.")
        if not isinstance(nome_artistico, str):
            raise TipoIncorretoError("O campo 'nome_artistico' deve ser uma string não nula.")

        if not descricao:
            raise ValorNuloError("O campo 'descricao' não pode ser vazio ou nulo.")
        if not isinstance(descricao, str):
            raise TipoIncorretoError("O campo 'descricao' deve ser uma string não nula.")

        self.id = id
        self.nome_pessoal = nome_pessoal
        self.nome_artistico = nome_artistico
        self.descricao = descricao

    query = MagicMock()


class Pessoa:
    def __init__(self, nome, email, senha, tipo):
        # Validações
        if not nome:
            raise ValorNuloError("O campo 'nome' não pode ser vazio ou nulo.")
        if not isinstance(nome, str):
            raise TipoIncorretoError("O campo 'nome' deve ser uma string não nula.")

        if not email:
            raise ValorNuloError("O campo 'email' não pode ser vazio ou nulo.")
        if not isinstance(email, str):
            raise TipoIncorretoError("O campo 'email' deve ser uma string não nula.")

        if not senha:
            raise ValorNuloError("O campo 'senha' não pode ser vazio ou nulo.")
        if not isinstance(senha, bytes):
            raise TipoIncorretoError("O campo 'senha' deve ser um byte array não nulo.")

        if not tipo:
            raise ValorNuloError("O campo 'tipo' não pode ser vazio ou nulo.")
        if not isinstance(tipo, str):
            raise TipoIncorretoError("O campo 'tipo' deve ser uma string não nula.")

        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo
        self.id = 1

    query = MagicMock()


class TipoFotoEnum(Enum):
    PERFIL = "Perfil"
    INSTAGRAM = "Instagram"
    PORTFOLIO = "portfólio"


class TipoPagamentoEnum(Enum):
    FIXO = "Fixo"
    COUVERT = "Couvert"


class Usuario:
    def __init__(self, id, celular, documento):
        # Validações
        if not isinstance(id, int):
            raise TipoIncorretoError("O campo 'id' deve ser um inteiro não nulo.")
        
        if not celular:
            raise ValorNuloError("O campo 'celular' não pode ser vazio ou nulo.")
        if not isinstance(celular, str):
            raise TipoIncorretoError("O campo 'celular' deve ser uma string não nula.")

        if not documento:
            raise ValorNuloError("O campo 'documento' não pode ser vazio ou nulo.")
        if not isinstance(documento, str):
            raise TipoIncorretoError("O campo 'documento' deve ser uma string não nula.")
        
        self.id = id
        self.celular = celular
        self.documento = documento

    query = MagicMock()

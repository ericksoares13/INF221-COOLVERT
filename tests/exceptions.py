class ValorNuloError(Exception):
    """Exceção lançada quando um atributo é nulo ou vazio."""

    def __init__(self, mensagem="O valor do atributo não pode ser nulo ou vazio."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)


class TipoIncorretoError(Exception):
    """Exceção lançada quando o tipo de um atributo é incorreto."""

    def __init__(self, mensagem="O tipo do atributo é incorreto."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

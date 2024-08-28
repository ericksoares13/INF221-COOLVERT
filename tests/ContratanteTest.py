from BancoDeDados import BancoDeDados
from mock_models import Contratante, TipoIncorretoError, ValorNuloError
from unittest.mock import patch
import unittest

class ContratanteTest(unittest.TestCase):
    @patch("BancoDeDados.BancoDeDados.CriaPessoa", return_value=1)
    @patch("BancoDeDados.BancoDeDados.CriaUsuario")
    @patch("BancoDeDados.Contratante")
    @patch("BancoDeDados.bd.session.commit")
    @patch("BancoDeDados.bd.session.add")
    def test_cria_contratante(
        self,
        mock_add,
        mock_commit,
        mock_contratante,
        mock_cria_usuario,
        mock_cria_pessoa,
    ):
        obj = {
            "nome": "Test User",
            "email": "test@example.com",
            "senha": "123456",
            "tipo": "C",
            "nome_estabelecimento": "Estabelecimento",
            "cep": "12345-678",
            "estado": "SP",
            "cidade": "Cidade",
            "bairro": "Bairro",
            "numero": "123",
            "complemento": "Apto 1",
        }
        mock_contratante_instance = mock_contratante.return_value

        result_id = BancoDeDados.CriaContratante(obj)

        mock_cria_pessoa.assert_called_once_with(obj)
        mock_cria_usuario.assert_called_once_with(obj)
        mock_contratante.assert_called_once_with(
            id=1,
            nome_estabelecimento=obj["nome_estabelecimento"],
            cep=obj["cep"],
            estado=obj["estado"],
            cidade=obj["cidade"],
            bairro=obj["bairro"],
            numero=obj["numero"],
            complemento=obj["complemento"],
        )
        mock_add.assert_called_once_with(mock_contratante_instance)
        mock_commit.assert_called_once()

        self.assertEqual(result_id, 1)

    def test_validacoes_contratante(self):
        
        #Testes de ValorNuloError
        with self.assertRaises(ValorNuloError):
            Contratante(
                id=None,
                nome_estabelecimento="nome_estabelecimento",
                cep="12345-678",
                estado="SP",
                cidade="Cidade",
                bairro="Bairro",
                numero="123",
                complemento="Apto 1",
            )
        with self.assertRaises(ValorNuloError):    
            Contratante(
                id=1,
                nome_estabelecimento=None,
                cep="12345-678",
                estado="SP",
                cidade="Cidade",
                bairro="Bairro",
                numero="123",
                complemento="Apto 1",
            )
        with self.assertRaises(ValorNuloError):
            Contratante(
                id=1,
                nome_estabelecimento="nome_estabelecimento",
                cep=None,
                estado="SP",
                cidade="Cidade",
                bairro="Bairro",
                numero="123",
                complemento="Apto 1",
            )
        with self.assertRaises(ValorNuloError):    
            Contratante(
                id=1,
                nome_estabelecimento="nome_estabelecimento",
                cep="12345-678",
                estado=None,
                cidade="Cidade",
                bairro="Bairro",
                numero="123",
                complemento="Apto 1",
            )
        with self.assertRaises(ValorNuloError):
            Contratante(
                id=1,
                nome_estabelecimento="nome_estabelecimento",
                cep="12345-678",
                estado="SP",
                cidade=None,
                bairro="Bairro",
                numero="123",
                complemento="Apto 1",
            )
        with self.assertRaises(ValorNuloError):
            Contratante(
                id=1,
                nome_estabelecimento="nome_estabelecimento",
                cep="12345-678",
                estado="SP",
                cidade="Cidade",
                bairro=None,
                numero="123",
                complemento="Apto 1",
            )
        with self.assertRaises(ValorNuloError):
            Contratante(
                id=1,
                nome_estabelecimento="nome_estabelecimento",
                cep="12345-678",
                estado="SP",
                cidade="Cidade",
                bairro="Bairro",
                numero=None,
                complemento="Apto 1",
            )
        with self.assertRaises(ValorNuloError):
            Contratante(
                id=1,
                nome_estabelecimento="nome_estabelecimento",
                cep="12345-678",
                estado="SP",
                cidade="Cidade",
                bairro="Bairro",
                numero="123",
                complemento=None,
            )
        #Testes de TipoIncorretoError  
        
        with self.assertRaises(TipoIncorretoError):
            Contratante(
                id="abc",
                nome_estabelecimento="Estabelecimento",
                cep="12345-678",
                estado="SP",
                cidade="Cidade",
                bairro="Bairro",
                numero="123",
                complemento="Apto 1",
            )
        with self.assertRaises(TipoIncorretoError):
            Contratante(
                id=1,
                nome_estabelecimento=123,
                cep="12345-678",
                estado="SP",
                cidade="Cidade",
                bairro="Bairro",
                numero="123",
                complemento="Apto 1",
            )
        with self.assertRaises(TipoIncorretoError):
            Contratante(
                id=1,
                nome_estabelecimento="Estabelecimento",
                cep=123,
                estado="SP",
                cidade="Cidade",
                bairro="Bairro",
                numero="123",
                complemento="Apto 1",
            )
        with self.assertRaises(TipoIncorretoError):
            Contratante(
                id=1,
                nome_estabelecimento="Estabelecimento",
                cep="12345-678",
                estado=123,
                cidade="Cidade",
                bairro="Bairro",
                numero="123",
                complemento="Apto 1",
            )
        with self.assertRaises(TipoIncorretoError):
            Contratante(
                id=1,
                nome_estabelecimento="Estabelecimento",
                cep="12345-678",
                estado="SP",
                cidade=123,
                bairro="Bairro",
                numero="123",
                complemento="Apto 1",
            )
        with self.assertRaises(TipoIncorretoError):
            Contratante(
                id=1,
                nome_estabelecimento="Estabelecimento",
                cep="12345-678",
                estado="SP",
                cidade="Cidade",
                bairro=123,
                numero="123",
                complemento="Apto 1",
            )
        with self.assertRaises(TipoIncorretoError):
            Contratante(
                id=1,
                nome_estabelecimento="Estabelecimento",
                cep="12345-678",
                estado="SP",
                cidade="Cidade",
                bairro="Bairro",
                numero=123,
                complemento="Apto 1",
            )
        with self.assertRaises(TipoIncorretoError):
            Contratante(
                id=1,
                nome_estabelecimento="Estabelecimento",
                cep="12345-678",
                estado="SP",
                cidade="Cidade",
                bairro="Bairro",
                numero="123",
                complemento=123,
            )

       

    @patch("BancoDeDados.Contratante.query")
    def test_GetContratante(self, mock_query):
        self.contratante_obj = Contratante(
            id=1,
            nome_estabelecimento="Estabelecimento",
            cep="12345-678",
            estado="SP",
            cidade="Cidade",
            bairro="Bairro",
            numero="123",
            complemento="Apto 1",
        )

        def get_side_effect(id_contratante):
            return self.contratante_obj if id_contratante == 1 else None

        mock_query.get.side_effect = get_side_effect

        result = BancoDeDados.GetContratante(1)
        self.assertIs(
            result, self.contratante_obj, "Não foi retornado o objeto correto."
        )

        mock_query.get.assert_called_once_with(1)

    @patch("BancoDeDados.Contratante.query")
    def test_GetContratanteNone(self, mock_query):
        self.contratante_obj = Contratante(
            id=1,
            nome_estabelecimento="Estabelecimento",
            cep="12345-678",
            estado="SP",
            cidade="Cidade",
            bairro="Bairro",
            numero="123",
            complemento="Apto 1",
        )

        def get_side_effect(id_contratante):
            return self.contratante_obj if id_contratante == 1 else None

        mock_query.get.side_effect = get_side_effect

        result = BancoDeDados.GetContratante(2)
        self.assertIsNone(result, "Foi encontrado um objeto inesperado.")

        mock_query.get.assert_called_once_with(2)

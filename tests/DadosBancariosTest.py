from BancoDeDados import BancoDeDados
from mock_models import DadosBancario, TipoIncorretoError, ValorNuloError
from unittest.mock import patch
import unittest


class DadosBancariosTest(unittest.TestCase):
    @patch("BancoDeDados.DadosBancario")
    @patch("BancoDeDados.bd.session.commit")
    @patch("BancoDeDados.bd.session.add")
    def test_cria_dados_bancario(self, mock_add, mock_commit, mock_dados_bancario):
        obj = {
            "id": 1,
            "num_cartao": "1234-5678-9012-3456",
            "nome_cartao": "Test User",
            "cod_seguranca": "123",
            "validade": "12/25",
        }
        mock_dados_bancario_instance = mock_dados_bancario.return_value

        BancoDeDados.CriaDadosBancario(obj)

        mock_dados_bancario.assert_called_once_with(
            id=obj["id"],
            num_cartao=obj["num_cartao"],
            nome_cartao=obj["nome_cartao"],
            cod_seguranca=obj["cod_seguranca"],
            validade=obj["validade"],
        )
        mock_add.assert_called_once_with(mock_dados_bancario_instance)
        mock_commit.assert_called_once()

    def test_validacoes_dados_bancarios(self):
        # Testes de ValorNuloError
        with self.assertRaises(ValorNuloError):
            DadosBancario(
                id=None,
                num_cartao="1234-5678-9012-3456",
                nome_cartao="Test User",
                cod_seguranca="123",
                validade="12/25",
            )
        
        with self.assertRaises(ValorNuloError):
            DadosBancario(
                id=1,
                num_cartao=None,
                nome_cartao="Test User",
                cod_seguranca="123",
                validade="12/25",
            )
        with self.assertRaises(ValorNuloError):
            DadosBancario(
                id=1,
                num_cartao="1234-5678-9012-3456",
                nome_cartao=None,
                cod_seguranca="123",
                validade="12/25",
            )
        with self.assertRaises(ValorNuloError):
            DadosBancario(
                id=1,
                num_cartao="1234-5678-9012-3456",
                nome_cartao="Test User",
                cod_seguranca=None,
                validade="12/25",
            )
        with self.assertRaises(ValorNuloError):
            DadosBancario(
                id=1,
                num_cartao="1234-5678-9012-3456",
                nome_cartao="Test User",
                cod_seguranca="123",
                validade=None,
            )
        # Testes de TipoIncorretoError
        
        with self.assertRaises(TipoIncorretoError):
            DadosBancario(
                id="abc",
                num_cartao="1234-5678-9012-3456",
                nome_cartao="Test User",
                cod_seguranca="123",
                validade="12/25",
            )
        with self.assertRaises(TipoIncorretoError):
            DadosBancario(
                id=1,
                num_cartao=1234567890123456,
                nome_cartao="Test User",
                cod_seguranca="123",
                validade="12/25",
            )
        with self.assertRaises(TipoIncorretoError):
            DadosBancario(
                id=1,
                num_cartao="1234-5678-9012-3456",
                nome_cartao=123,
                cod_seguranca="123",
                validade="12/25",
            )
        with self.assertRaises(TipoIncorretoError):
            DadosBancario(
                id=1,
                num_cartao="1234-5678-9012-3456",
                nome_cartao="Test User",
                cod_seguranca=123,
                validade="12/25",
            )
        with self.assertRaises(TipoIncorretoError):
            DadosBancario(
                id=1,
                num_cartao="1234-5678-9012-3456",
                nome_cartao="Test User",
                cod_seguranca="123",
                validade=1225,
            )


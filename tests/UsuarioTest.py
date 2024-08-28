from BancoDeDados import BancoDeDados
from mock_models import TipoIncorretoError, Usuario, ValorNuloError
from unittest.mock import MagicMock, patch
import unittest


class UsuarioTest(unittest.TestCase):

    @patch('BancoDeDados.Usuario')
    @patch('BancoDeDados.bd.session.commit')
    @patch('BancoDeDados.bd.session.add')
    def test_cria_usuario(self, mock_add, mock_commit, mock_usuario):
        obj = {'id': 1, 'celular': '123456789', 'documento': '11122233344'}
        mock_usuario_instance = mock_usuario.return_value

        BancoDeDados.CriaUsuario(obj)

        mock_usuario.assert_called_once_with(id=obj['id'], celular=obj['celular'], documento=obj['documento'])
        mock_add.assert_called_once_with(mock_usuario_instance)
        mock_commit.assert_called_once()

    def test_validacoes_usuario(self):
        with self.assertRaises(TipoIncorretoError):
            Usuario(id="abc", celular="123456789", documento="11122233344")

        with self.assertRaises(ValorNuloError):
            Usuario(id=1, celular="", documento="11122233344")

    @patch('BancoDeDados.Pessoa.query.get')
    def test_GetNomeUsuario_valido(self, mock_get):
        mock_pessoa = MagicMock()
        mock_pessoa.nome = "João"
        mock_get.return_value = mock_pessoa

        result = BancoDeDados.GetNomeUsuario(1)

        mock_get.assert_called_once_with(1)
        self.assertEqual(result, "João")

    @patch('BancoDeDados.Pessoa.query.get')
    def test_GetNomeUsuario_invalido(self, mock_get):
        mock_get.return_value = None

        result = BancoDeDados.GetNomeUsuario(999)

        mock_get.assert_called_once_with(999)
        self.assertIsNone(result)

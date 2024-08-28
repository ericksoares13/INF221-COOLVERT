from BancoDeDados import BancoDeDados
from mock_models import Musico, TipoIncorretoError, ValorNuloError
from unittest.mock import patch
import unittest


class MusicoTest(unittest.TestCase):
    @patch("BancoDeDados.BancoDeDados.CriaPessoa", return_value=1)
    @patch("BancoDeDados.BancoDeDados.CriaUsuario")
    @patch("BancoDeDados.Musico")
    @patch("BancoDeDados.bd.session.commit")
    @patch("BancoDeDados.bd.session.add")
    def test_cria_musico(
        self, mock_add, mock_commit, mock_musico, mock_cria_usuario, mock_cria_pessoa
    ):
        obj = {
            "nome": "Test User",
            "email": "test@example.com",
            "senha": "123456",
            "tipo": "M",
            "nome_pessoal": "Pessoal",
            "nome_artistico": "Artistico",
            "descricao": "Descricao",
        }
        mock_musico_instance = mock_musico.return_value

        result_id = BancoDeDados.CriaMusico(obj)

        mock_cria_pessoa.assert_called_once_with(obj)
        mock_cria_usuario.assert_called_once_with(obj)
        mock_musico.assert_called_once_with(
            id=1,
            nome_pessoal=obj["nome_pessoal"],
            nome_artistico=obj["nome_artistico"],
            descricao=obj["descricao"],
        )
        mock_add.assert_called_once_with(mock_musico_instance)
        mock_commit.assert_called_once()

        self.assertEqual(result_id, 1)

    def test_validacoes_musico(self):
        
        #Testes de ValorNuloError
        with self.assertRaises(ValorNuloError):
            Musico(
                id=None, nome_pessoal="Pessoal", nome_artistico="Artistico", descricao="Descricao"
            )
        with self.assertRaises(ValorNuloError):
            Musico(
                id=1, nome_pessoal=None, nome_artistico="Artistico", descricao="Descricao"
            )
        with self.assertRaises(ValorNuloError):
            Musico(
                id=1, nome_pessoal="Pessoal", nome_artistico=None, descricao="Descricao"
            )
        with self.assertRaises(ValorNuloError):
            Musico(
                id=1, nome_pessoal="Pessoal", nome_artistico="Artistico", descricao = None
            )
        #Testes de TipoIncorretoError     
            
            
        with self.assertRaises(TipoIncorretoError):
            Musico(
                id="abc",
                nome_pessoal="Pessoal",
                nome_artistico="Artistico",
                descricao="Descricao",
            )
        with self.assertRaises(TipoIncorretoError):
            Musico(
                id=1,
                nome_pessoal=123,
                nome_artistico="Artistico",
                descricao="Descricao",
            )
            
        with self.assertRaises(TipoIncorretoError):
            Musico(
                id=1,
                nome_pessoal="Pessoal",
                nome_artistico=123,
                descricao="Descricao",
            )
        with self.assertRaises(TipoIncorretoError):
            Musico(
                id=1,
                nome_pessoal="Pessoal",
                nome_artistico="Artistico",
                descricao=123,
            )


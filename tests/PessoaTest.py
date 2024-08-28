from BancoDeDados import BancoDeDados
from mock_models import Pessoa, TipoIncorretoError, ValorNuloError
from unittest.mock import MagicMock, patch
import unittest
import bcrypt

class PessoaTest(unittest.TestCase):
    @patch("BancoDeDados.Pessoa")
    @patch("BancoDeDados.bd.session.commit")
    @patch("BancoDeDados.bd.session.add")
    def test_CriaPessoa(self, mock_add, mock_commit, mock_pessoa):
        mock_pessoa_instance = MagicMock()
        mock_pessoa.return_value = mock_pessoa_instance
        mock_pessoa_instance.id = 1

        obj = {
            "nome": "Test User",
            "email": "test@example.com",
            "senha": "123456",
            "tipo": "C",
        }
        pessoa_id = BancoDeDados.CriaPessoa(obj)

        mock_add.assert_called_once_with(mock_pessoa_instance)
        mock_commit.assert_called_once()

        self.assertIsInstance(pessoa_id, int)
        self.assertEqual(pessoa_id, 1)

    def test_validacoes_pessoa(self):
        # Teste para ValorNuloError
        with self.assertRaises(ValorNuloError):
            Pessoa(nome=None, email="test@example.com", senha=b"123456", tipo="C")

        with self.assertRaises(ValorNuloError):
            Pessoa(nome="Test User", email=None, senha=b"123456", tipo="C")

        with self.assertRaises(ValorNuloError):
            Pessoa(nome="Test User", email="test@example.com", senha=None, tipo="C")
            
        with self.assertRaises(ValorNuloError):
            Pessoa(nome="Test User", email="test@example.com", senha=b"123456", tipo= None)

        # Teste para TipoIncorretoError
        with self.assertRaises(TipoIncorretoError):
            Pessoa(
                nome=1, email="test@example.com", senha=b"123456", tipo="C"
            )

        with self.assertRaises(TipoIncorretoError):
            Pessoa(
                nome="Test User", email=1, senha=b"123456", tipo="C"
            )
        with self.assertRaises(TipoIncorretoError):
            Pessoa(
                nome="Test User", email= "test@example.com", senha="123456", tipo="C"
            )
        with self.assertRaises(TipoIncorretoError):
            Pessoa(
                nome="Test User", email= "test@example.com", senha=b"123456", tipo=1
            )
            

    @patch("BancoDeDados.Pessoa.query.filter_by")
    def test_Login(self, mock_filter_by):
        mock_pessoa = MagicMock()
        mock_pessoa.verifica_senha.return_value = True
        mock_filter_by.return_value.first.return_value = mock_pessoa

        obj = {"identificador": "test@example.com", "senha": "password"}
        result = BancoDeDados.Login(obj)
        self.assertEqual(result, mock_pessoa)

    @patch("BancoDeDados.Pessoa.query.filter_by")
    def test_Login_Invalid(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = None

        obj = {"identificador": "test@example.com", "senha": "password"}
        result = BancoDeDados.Login(obj)
        self.assertIsNone(result)

    @patch("BancoDeDados.Pessoa.query.filter_by")
    def test_VerificaEmail(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = None

        email = "test@example.com"
        result = BancoDeDados.VerificaEmail(email)
        self.assertTrue(result)

    @patch("BancoDeDados.Pessoa.query.filter_by")
    def test_VerificaEmail_Exists(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = MagicMock()

        email = "test@example.com"
        result = BancoDeDados.VerificaEmail(email)
        self.assertFalse(result)

    @patch("BancoDeDados.Pessoa.query.filter_by")
    def test_VerificaNomeUsuario(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = None

        nome = "Test User"
        result = BancoDeDados.VerificaNomeUsuario(nome)
        self.assertTrue(result)

    @patch("BancoDeDados.Pessoa.query.filter_by")
    def test_VerificaNomeUsuario_Exists(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = MagicMock()

        nome = "Test User"
        result = BancoDeDados.VerificaNomeUsuario(nome)
        self.assertFalse(result)

    @patch("BancoDeDados.Pessoa.query")
    def test_GetUser(self, mock_query):
        self.user_obj = Pessoa(
            nome="Test User", 
            email="test@example.com", 
            senha=bcrypt.hashpw("ABcd123!".encode("utf-8"), bcrypt.gensalt()),
            tipo='M'
        )

        def get_side_effect(id_user):
            return self.user_obj if id_user == 1 else None

        mock_query.get.side_effect = get_side_effect

        result = BancoDeDados.GetUser(1)
        self.assertIs(result, self.user_obj, "Não foi retornado o objeto correto.")

        mock_query.get.assert_called_once_with(1)

    @patch("BancoDeDados.Pessoa.query")
    def test_GetUserNone(self, mock_query):
        self.user_obj = Pessoa(
            nome="Test User", 
            email="test@example.com", 
            senha=bcrypt.hashpw("ABcd123!".encode("utf-8"), bcrypt.gensalt()),
            tipo='M'
        )

        def get_side_effect(id_user):
            return self.user_obj if id_user == 1 else None

        mock_query.get.side_effect = get_side_effect

        result = BancoDeDados.GetUser(2)
        self.assertIsNone(result, "Foi encontrado um objeto inesperado.")

        mock_query.get.assert_called_once_with(2)

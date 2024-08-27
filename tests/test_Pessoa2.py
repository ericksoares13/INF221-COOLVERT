import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from BancoDeDados_Pessoa2 import BancoDeDados
from mock_models import *

app = Flask(__name__)
app.secret_key = "default_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
bd = SQLAlchemy(app)


class TestBancoDeDados(unittest.TestCase):
    @patch("BancoDeDados_Pessoa2.Pessoa.query.filter_by")
    def test_Login(self, mock_filter_by):
        mock_pessoa = MagicMock()
        mock_pessoa.verifica_senha.return_value = True
        mock_filter_by.return_value.first.return_value = mock_pessoa

        obj = {'identificador': 'test@example.com', 'senha': 'password'}
        result = BancoDeDados.Login(obj)
        self.assertEqual(result, mock_pessoa)

    @patch("BancoDeDados_Pessoa2.Pessoa.query.filter_by")
    def test_Login_Invalid(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = None

        obj = {'identificador': 'test@example.com', 'senha': 'password'}
        result = BancoDeDados.Login(obj)
        self.assertIsNone(result)

    @patch("BancoDeDados_Pessoa2.Pessoa.query.filter_by")
    def test_VerificaEmail(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = None

        email = 'test@example.com'
        result = BancoDeDados.VerificaEmail(email)
        self.assertTrue(result)

    @patch("BancoDeDados_Pessoa2.Pessoa.query.filter_by")
    def test_VerificaEmail_Exists(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = MagicMock()

        email = 'test@example.com'
        result = BancoDeDados.VerificaEmail(email)
        self.assertFalse(result)

    @patch("BancoDeDados_Pessoa2.Pessoa.query.filter_by")
    def test_VerificaNomeUsuario(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = None

        nome = 'Test User'
        result = BancoDeDados.VerificaNomeUsuario(nome)
        self.assertTrue(result)

    @patch("BancoDeDados_Pessoa2.Pessoa.query.filter_by")
    def test_VerificaNomeUsuario_Exists(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = MagicMock()

        nome = 'Test User'
        result = BancoDeDados.VerificaNomeUsuario(nome)
        self.assertFalse(result)

    @patch("BancoDeDados_Pessoa2.EstiloMusical.query.filter_by")
    def test_VerificaEstiloMusical(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = None

        nome = 'Rock'
        result = BancoDeDados.VerificaEstiloMusical(nome)
        self.assertTrue(result)

    @patch("BancoDeDados_Pessoa2.EstiloMusical.query.filter_by")
    def test_VerificaEstiloMusical_Exists(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = MagicMock()

        nome = 'Rock'
        result = BancoDeDados.VerificaEstiloMusical(nome)
        self.assertFalse(result)

    @patch("BancoDeDados_Pessoa2.EstiloMusical")
    @patch("BancoDeDados_Pessoa2.bd.session.add")
    @patch("BancoDeDados_Pessoa2.bd.session.commit")
    def test_CriaEstiloMusical(self, mock_commit, mock_add, mock_estilo):
        nome = 'Rock'
        BancoDeDados.CriaEstiloMusical(nome)

        mock_estilo.assert_called_once_with(nome=nome)
        mock_add.assert_called_once()
        mock_commit.assert_called_once()

    @patch("BancoDeDados_Pessoa2.DemandaEstilos.query.filter_by")
    @patch("BancoDeDados_Pessoa2.EstiloMusical.query.with_entities")
    def test_GetEstilosMusicais(self, mock_with_entities, mock_filter_by):
        mock_estilo = MagicMock()
        mock_with_entities.return_value.filter_by.return_value.first.return_value = ['Rock']
        mock_filter_by.return_value.all.return_value = [mock_estilo]

        id_demanda = 1
        result = BancoDeDados.GetEstilosMusicais(id_demanda)

        mock_filter_by.assert_called_once_with(demanda=id_demanda)
        mock_with_entities.assert_called_once()
        self.assertEqual(result, ['Rock'])

if __name__ == "__main__":
    unittest.main()

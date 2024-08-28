from BancoDeDados import BancoDeDados
from mock_models import Mensagem, TipoIncorretoError, ValorNuloError
from unittest.mock import patch
import datetime
import unittest


class MensagemTest(unittest.TestCase):
    @patch("BancoDeDados.bd.session")
    @patch("BancoDeDados.Mensagem")
    def test_EnviaMensagem(self, mock_mensagem, mock_session):
        self.obj_mensagem = {"match": 1, "dono": 1, "mensagem": "Oi!"}

        mock_instance = mock_mensagem.return_value

        BancoDeDados.EnviaMensagem(self.obj_mensagem)

        mock_mensagem.assert_called_once_with(match=1, dono=1, mensagem="Oi!")
        mock_session.add.assert_called_once_with(mock_instance)
        mock_session.commit.assert_called_once()

    @patch("BancoDeDados.Mensagem.query")
    def test_GetChat(self, mock_query):
        self.msg1 = Mensagem(1, 1, "Oi! Tudo bem?")
        self.msg2 = Mensagem(1, 2, "Tudo bem! E vc?")

        self.msg1.horario = datetime.datetime(2024, 8, 25, 10, 0, 0)
        self.msg2.horario = datetime.datetime(2024, 8, 25, 11, 0, 0)

        self.obj_chat = [self.msg2, self.msg1]

        mock_query.filter_by.return_value.all.return_value = self.obj_chat

        result = BancoDeDados.GetChat(1)

        self.assertEqual(len(result), 2, "As mensagens do chat não foram encontradas.")

        self.assertIs(
            result[0], self.msg1, "As mensagens do chat chegaram na ordem errada."
        )
        self.assertIs(
            result[1], self.msg2, "As mensagens do chat chegaram na ordem errada."
        )

    def test_ValidacoesMensagem(self):
        with self.assertRaises(ValorNuloError):
            Mensagem(match="", dono=1, mensagem="Oi!")

        with self.assertRaises(ValorNuloError):
            Mensagem(match=1, dono=None, mensagem="Oi!")

        with self.assertRaises(ValorNuloError):
            Mensagem(match=1, dono=1, mensagem="")

        with self.assertRaises(TipoIncorretoError):
            Mensagem(match="abc", dono=1, mensagem="Oi!")

        with self.assertRaises(TipoIncorretoError):
            Mensagem(match=1, dono="abc", mensagem="Oi!")

    @patch("BancoDeDados.Mensagem.query")
    def test_GetChatVazio(self, mock_query):
        self.obj_chat = [Mensagem(1, 1, "Oi! Tudo bem?")]

        mock_query.filter_by.return_value.all.return_value = []

        result = BancoDeDados.GetChat(1)

        self.assertEqual(len(result), 0, "Esse chat deveria estar vazio.")

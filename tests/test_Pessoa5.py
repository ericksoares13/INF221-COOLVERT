import datetime
import unittest
from unittest.mock import patch, MagicMock
from BancoDeDados_Pessoa5 import BancoDeDados
from mock_models import *

class TestBancoDeDados(unittest.TestCase):
    
    @patch('BancoDeDados_Pessoa5.bd.session')
    @patch('BancoDeDados_Pessoa5.Mensagem')
    def test_EnviaMensagem(self, mock_Mensagem, mock_session):
        # ----- SetUp -----
        self.obj_mensagem = {
            'match': 1,
            'dono': 1,
            'mensagem': 'Oi!'
        }
        
        # ----- Teste -----
        mock_instance = mock_Mensagem.return_value

        BancoDeDados.EnviaMensagem(self.obj_mensagem)

        mock_Mensagem.assert_called_once_with(match=1, dono=1, mensagem='Oi!')
        mock_session.add.assert_called_once_with(mock_instance)
        mock_session.commit.assert_called_once()

    @patch('BancoDeDados_Pessoa5.bd.session')
    @patch('BancoDeDados_Pessoa5.Imagem')
    def test_CriaImagem(self, mock_Imagem, mock_session):
        # ----- SetUp -----
        self.obj_imagem = {
            'dono': 1,
            'nome': 'foto.jpg',
            'tipo_foto': 'Perfil',
            'caminho': '/app/static/images/foto.jpg'
        }
        
        # ----- Teste -----
        mock_instance = mock_Imagem.return_value

        BancoDeDados.CriaImagem(self.obj_imagem)

        mock_Imagem.assert_called_once_with(dono=1, nome='foto.jpg', tipo_foto=TipoFotoEnum.PERFIL, caminho='/app/static/images/foto.jpg')
        mock_session.add.assert_called_once_with(mock_instance)
        mock_session.commit.assert_called_once()

    @patch('BancoDeDados_Pessoa5.Mensagem.query')
    def test_GetChat(self, mock_query):
        # ----- SetUp -----
        # Definindo horários diferentes para simular a ordenação
        self.msg1 = Mensagem(1, 1, 'Oi! Tudo bem?')
        self.msg2 = Mensagem(1, 2, 'Tudo bem! E vc?')

        # Ajuste nos horários para garantir a ordenação correta
        self.msg1.horario = datetime.datetime(2024, 8, 25, 10, 0, 0)
        self.msg2.horario = datetime.datetime(2024, 8, 25, 11, 0, 0)

        self.obj_chat = [
            self.msg2,  # msg2 com horário posterior deve vir depois
            self.msg1   # msg1 com horário anterior deve vir antes
        ]
        
        # ----- Teste -----
        mock_query.filter_by.return_value.all.return_value = self.obj_chat

        result = BancoDeDados.GetChat(1)

        self.assertEqual(len(result), 2, 'As mensagens do chat não foram encontradas.')

        self.assertIs(result[0], self.msg1, 'As mensagens do chat chegaram na ordem errada.')
        self.assertIs(result[1], self.msg2, 'As mensagens do chat chegaram na ordem errada.')
        
    @patch('BancoDeDados_Pessoa5.Imagem.query')
    def test_GetImagemPerfil(self, mock_query):
        # ----- SetUp -----
        self.imagem_obj = Imagem(dono=1, nome='foto.jpg', tipo_foto=TipoFotoEnum.PERFIL, caminho='/app/static/images/foto.jpg')
        
        # ----- Teste -----
        def filter_by_side_effect(**kwargs):
            if kwargs == {"dono": 1, "tipo_foto": TipoFotoEnum.PERFIL}:
                mock_result = MagicMock()
                mock_result.first.return_value = self.imagem_obj
                return mock_result
            else:
                return MagicMock(first=MagicMock(return_value=None))

        mock_query.filter_by.side_effect = filter_by_side_effect

        result = BancoDeDados.GetImagemPerfil(1)
        self.assertIs(result, self.imagem_obj, 'Não foi retornado o objeto correto.')

        mock_query.filter_by.assert_called_once_with(dono=1, tipo_foto=TipoFotoEnum.PERFIL)

    @patch('BancoDeDados_Pessoa5.Pessoa.query')
    def test_GetUser(self, mock_query):
        # ----- SetUp -----
        self.user_obj = Pessoa()
        
        # ----- Teste -----
        def get_side_effect(id_user):
            return self.user_obj if id_user == 1 else None

        mock_query.get.side_effect = get_side_effect

        result = BancoDeDados.GetUser(1)
        self.assertIs(result, self.user_obj, 'Não foi retornado o objeto correto.')

        mock_query.get.assert_called_once_with(1)

    @patch('BancoDeDados_Pessoa5.Contratante.query')
    def test_GetContratante(self, mock_query):
        # ----- SetUp -----
        self.contratante_obj = Contratante()
        
        # ----- Teste -----
        def get_side_effect(id_contratante):
            return self.contratante_obj if id_contratante == 1 else None

        mock_query.get.side_effect = get_side_effect

        result = BancoDeDados.GetContratante(1)
        self.assertIs(result, self.contratante_obj, 'Não foi retornado o objeto correto.')

        mock_query.get.assert_called_once_with(1)

if __name__ == '__main__':
    unittest.main()
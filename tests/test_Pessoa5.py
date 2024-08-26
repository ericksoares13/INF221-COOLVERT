import unittest
from unittest.mock import patch, MagicMock
from BancoDeDados_Pessoa5 import BancoDeDados
from mock_models import TipoFotoEnum

class TestBancoDeDados(unittest.TestCase):

    def setUp(self):
        self.obj_mensagem = {
            'match': 1,
            'dono': 1,
            'mensagem': 'Oi!'
        }

        self.obj_imagem = {
            'dono': 1,
            'nome': 'foto.jpg',
            'tipo_foto': 'Perfil',
            'caminho': '/app/static/images/foto.jpg'
        }

    @patch('BancoDeDados_Pessoa5.bd.session')
    @patch('BancoDeDados_Pessoa5.Mensagem')
    def test_EnviaMensagem(self, mock_Mensagem, mock_session):
        mock_instance = mock_Mensagem.return_value

        BancoDeDados.EnviaMensagem(self.obj_mensagem)

        mock_Mensagem.assert_called_once_with(match=1, dono=1, mensagem='Oi!')
        mock_session.add.assert_called_once_with(mock_instance)
        mock_session.commit.assert_called_once()

    @patch('BancoDeDados_Pessoa5.Mensagem.query')
    def test_GetChat(self, mock_query):
        mock_query.filter_by.return_value.all.return_value = [
            MagicMock(horario=2), MagicMock(horario=1)
        ]

        result = BancoDeDados.GetChat(1)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].horario, 1)
        self.assertEqual(result[1].horario, 2)

    @patch('BancoDeDados_Pessoa5.bd.session')
    @patch('BancoDeDados_Pessoa5.Imagem')
    def test_CriaImagem(self, mock_Imagem, mock_session):
        mock_instance = mock_Imagem.return_value

        BancoDeDados.CriaImagem(self.obj_imagem)

        mock_Imagem.assert_called_once_with(dono=1, nome='foto.jpg', tipo_foto=TipoFotoEnum.PERFIL, caminho='/app/static/images/foto.jpg')
        mock_session.add.assert_called_once_with(mock_instance)
        mock_session.commit.assert_called_once()

    @patch('BancoDeDados_Pessoa5.Imagem.query')
    def test_GetImagemPerfil(self, mock_query):
        mock_query.filter_by.return_value.first.return_value = 'imagem_obj'

        result = BancoDeDados.GetImagemPerfil(1)

        mock_query.filter_by.assert_called_once_with(dono=1, tipo_foto=TipoFotoEnum.PERFIL)
        self.assertEqual(result, 'imagem_obj')

    @patch('BancoDeDados_Pessoa5.Pessoa.query')
    def test_GetUser(self, mock_query):
        mock_query.get.return_value = 'user_obj'

        result = BancoDeDados.GetUser(1)

        mock_query.get.assert_called_once_with(1)
        self.assertEqual(result, 'user_obj')

    @patch('BancoDeDados_Pessoa5.Contratante.query')
    def test_GetContratante(self, mock_query):
        mock_query.get.return_value = 'contratante_obj'

        result = BancoDeDados.GetContratante(1)

        mock_query.get.assert_called_once_with(1)
        self.assertEqual(result, 'contratante_obj')

if __name__ == '__main__':
    unittest.main()

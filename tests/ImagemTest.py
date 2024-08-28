from BancoDeDados import BancoDeDados
from mock_models import Imagem, TipoFotoEnum, TipoIncorretoError, ValorNuloError
from unittest.mock import MagicMock, patch
import unittest


class ImagemTest(unittest.TestCase):
    @patch("BancoDeDados.bd.session")
    @patch("BancoDeDados.Imagem")
    def test_CriaImagem(self, mock_imagem, mock_session):
        self.obj_imagem = {
            "dono": 1,
            "nome": "foto.jpg",
            "tipo_foto": "Perfil",
            "caminho": "/app/static/images/foto.jpg",
        }

        mock_instance = mock_imagem.return_value

        BancoDeDados.CriaImagem(self.obj_imagem)

        mock_imagem.assert_called_once_with(
            dono=1,
            nome="foto.jpg",
            tipo_foto=TipoFotoEnum.PERFIL,
            caminho="/app/static/images/foto.jpg",
        )
        mock_session.add.assert_called_once_with(mock_instance)
        mock_session.commit.assert_called_once()

    @patch("BancoDeDados.Imagem.query")
    def test_GetImagemPerfil(self, mock_query):
        self.imagem_obj = Imagem(
            dono=1,
            nome="foto.jpg",
            tipo_foto=TipoFotoEnum.PERFIL,
            caminho="/app/static/images/foto.jpg",
        )

        def filter_by_side_effect(**kwargs):
            if kwargs == {"dono": 1, "tipo_foto": TipoFotoEnum.PERFIL}:
                mock_result = MagicMock()
                mock_result.first.return_value = self.imagem_obj
                return mock_result
            else:
                return MagicMock(first=MagicMock(return_value=None))

        mock_query.filter_by.side_effect = filter_by_side_effect

        result = BancoDeDados.GetImagemPerfil(1)
        self.assertIs(result, self.imagem_obj, "Não foi retornado o objeto correto.")

        mock_query.filter_by.assert_called_once_with(
            dono=1, tipo_foto=TipoFotoEnum.PERFIL
        )

    def test_ValidacoesImagem(self):
        with self.assertRaises(ValorNuloError):
            Imagem(
                dono=1,
                nome="",
                tipo_foto=TipoFotoEnum.PERFIL,
                caminho="/caminho/foto.jpg",
            )

        with self.assertRaises(ValorNuloError):
            Imagem(
                dono=None,
                nome="foto.jpg",
                tipo_foto=TipoFotoEnum.PERFIL,
                caminho="/caminho/foto.jpg",
            )

        with self.assertRaises(TipoIncorretoError):
            Imagem(
                dono="abc",
                nome="foto.jpg",
                tipo_foto=TipoFotoEnum.PERFIL,
                caminho="/caminho/foto.jpg",
            )

        with self.assertRaises(TipoIncorretoError):
            Imagem(
                dono=1,
                nome="foto.jpg",
                tipo_foto="INVALIDO",
                caminho="/caminho/foto.jpg",
            )

        with self.assertRaises(ValorNuloError):
            Imagem(dono=1, nome="foto.jpg", tipo_foto=TipoFotoEnum.PERFIL, caminho="")

    @patch("BancoDeDados.Imagem.query")
    def test_GetImagemPerfilNone(self, mock_query):
        self.imagem_obj = Imagem(
            dono=1,
            nome="foto.jpg",
            tipo_foto=TipoFotoEnum.PERFIL,
            caminho="/app/static/images/foto.jpg",
        )

        def filter_by_side_effect(**kwargs):
            if kwargs == {"dono": 1, "tipo_foto": TipoFotoEnum.PERFIL}:
                mock_result = MagicMock()
                mock_result.first.return_value = self.imagem_obj
                return mock_result
            else:
                return MagicMock(first=MagicMock(return_value=None))

        mock_query.filter_by.side_effect = filter_by_side_effect

        result = BancoDeDados.GetImagemPerfil(2)
        self.assertIsNone(result, "Foi encontrado um objeto inesperado.")

        mock_query.filter_by.assert_called_once_with(
            dono=2, tipo_foto=TipoFotoEnum.PERFIL
        )

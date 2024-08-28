from BancoDeDados import BancoDeDados
from mock_models import Match, TipoIncorretoError, ValorNuloError
from unittest.mock import MagicMock, patch
import unittest


class MatchTest(unittest.TestCase):
    @patch("BancoDeDados.Match")
    @patch("BancoDeDados.bd.session.commit")
    @patch("BancoDeDados.bd.session.add")
    def test_CriaMatch(self, mock_add, mock_commit, mock_match):
        mock_match.return_value.id = 1

        obj = {"id_musico": 1, "id_demanda": 2}
        match_id = BancoDeDados.CriaMatch(obj)

        mock_add.assert_called_once()
        mock_commit.assert_called_once()

        self.assertIsInstance(match_id, int)
        self.assertEqual(match_id, 1)

    def test_validar_id_musico_nulo(self):
        with self.assertRaises(ValorNuloError):
            Match(None, 1)

    def test_validar_id_musico_tipo_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Match("string", 1)

    def test_validar_id_demanda_nulo(self):
        with self.assertRaises(ValorNuloError):
            Match(1, None)

    def test_validar_id_demanda_tipo_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Match(1, "string")

    @patch("BancoDeDados.Match.query.get")
    def test_GetMatch_valido(self, mock_get):
        mock_match = MagicMock()
        mock_get.return_value = mock_match

        result = BancoDeDados.GetMatch(1)

        mock_get.assert_called_once_with(1)
        self.assertEqual(result, mock_match)

    @patch("BancoDeDados.Match.query.get")
    def test_GetMatch_invalido(self, mock_get):
        mock_get.return_value = None

        result = BancoDeDados.GetMatch(999)

        mock_get.assert_called_once_with(999)
        self.assertIsNone(result)

    @patch("BancoDeDados.Match.query.filter_by")
    def test_GetMatches(self, mock_filter_by):
        mock_filter_by.return_value.all.return_value = [MagicMock(), MagicMock()]

        result = BancoDeDados.GetMatches(1)

        mock_filter_by.assert_called_once_with(id_demanda=1)
        self.assertEqual(len(result), 2)

    @patch("BancoDeDados.Match.query.filter_by")
    def test_GetMatches_id_inexistente(self, mock_filter_by):
        mock_filter_by.return_value.all.return_value = []

        result = BancoDeDados.GetMatches(999)

        mock_filter_by.assert_called_once_with(id_demanda=999)
        self.assertEqual(len(result), 0)

    @patch("BancoDeDados.Match.query.filter_by")
    def test_GetMatches_erro_consulta(self, mock_filter_by):
        mock_filter_by.side_effect = Exception("Erro na consulta")

        with self.assertRaises(Exception) as context:
            BancoDeDados.GetMatches(1)

        self.assertEqual(str(context.exception), "Erro na consulta")

    @patch("BancoDeDados.Match.query.filter_by")
    def test_GetMatchesMusico(self, mock_filter_by):
        mock_filter_by.return_value.all.return_value = [MagicMock(), MagicMock()]

        result = BancoDeDados.GetMatchesMusico(1)

        mock_filter_by.assert_called_once_with(id_musico=1)
        self.assertEqual(len(result), 2)

    @patch("BancoDeDados.Match.query.filter_by")
    def test_GetMatchesMusico_id_inexistente(self, mock_filter_by):
        mock_filter_by.return_value.all.return_value = []

        result = BancoDeDados.GetMatchesMusico(999)

        mock_filter_by.assert_called_once_with(id_musico=999)
        self.assertEqual(len(result), 0)

    @patch("BancoDeDados.Match.query.with_entities")
    def test_GetMusicos(self, mock_with_entities):
        mock_with_entities.return_value.filter_by.return_value.all.return_value = [
            (1,),
            (2,),
        ]

        result = BancoDeDados.GetMusicos(1)

        mock_with_entities.assert_called_once()
        self.assertEqual(result, [1, 2])

    @patch("BancoDeDados.Match.query.with_entities")
    def test_GetMusicos_erro_consulta(self, mock_with_entities):
        mock_with_entities.side_effect = Exception("Erro na consulta")

        with self.assertRaises(Exception) as context:
            BancoDeDados.GetMusicos(1)

        self.assertEqual(str(context.exception), "Erro na consulta")

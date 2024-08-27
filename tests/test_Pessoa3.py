import unittest
from datetime import date, timedelta
from unittest.mock import patch
from BancoDeDados_Pessoa3 import BancoDeDados
from mock_models import *


class TestBancoDeDadosDemandas(unittest.TestCase):
    @patch("BancoDeDados_Pessoa3.Demanda")
    @patch("BancoDeDados_Pessoa3.bd.session.add")
    @patch("BancoDeDados_Pessoa3.bd.session.commit")
    @patch("BancoDeDados_Pessoa3.Contratante.query.get")
    @patch("BancoDeDados_Pessoa3.EstiloMusical.query.filter_by")
    def test_CriaDemanda(
        self, mock_filter_by, mock_contratante_get, mock_commit, mock_add, mock_demanda
    ):
        mock_estilo = MagicMock()
        mock_filter_by.return_value.first.return_value = mock_estilo
        mock_contratante = MagicMock()
        mock_contratante_get.return_value = mock_contratante

        obj = {
            "data_show": "2023-12-31",
            "raio_procurado": 10,
            "fornece_equipamento": True,
            "publico_esperado": 100,
            "duracao_show": 120,
            "dono": 1,
            "tipo_pagamento": "Fixo",
            "momento_pagamento": "Antecipado",
            "estilos": ["Rock", "Pop"],
        }

        BancoDeDados.CriaDemanda(obj)

        mock_demanda.assert_called_once_with(
            data_show="2023-12-31",
            raio_procurado=10,
            fornece_equipamento=True,
            publico_esperado=100,
            duracao_show=120,
            dono=1,
            tipo_pagamento=TipoPagamentoEnum(obj["tipo_pagamento"]),
            momento_pagamento=MomentoPagamentoEnum(obj["momento_pagamento"]),
        )
        mock_add.assert_called_once()
        mock_commit.assert_called_once()

    def test_validar_id_nulo(self):
        with self.assertRaises(ValorNuloError):
            Demanda(
                None,
                date.today(),
                5,
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_id_tipo_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Demanda(
                "string",
                date.today(),
                5,
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_data_show_nula(self):
        with self.assertRaises(ValorNuloError):
            Demanda(
                1,
                None,
                5,
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_data_show_tipo_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Demanda(
                1,
                12345,
                5,
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_data_show_data_passada(self):
        with self.assertRaises(TipoIncorretoError):
            Demanda(
                1,
                date.today() - timedelta(days=1),
                5,
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_raio_procurado_nulo(self):
        with self.assertRaises(ValorNuloError):
            Demanda(
                1,
                date.today(),
                None,
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_raio_procurado_tipo_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Demanda(
                1,
                date.today(),
                "string",
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_fornece_equipamento_nulo(self):
        with self.assertRaises(ValorNuloError):
            Demanda(
                1,
                date.today(),
                5,
                None,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_fornece_equipamento_tipo_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Demanda(
                1,
                date.today(),
                5,
                "string",
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_publico_esperado_nulo(self):
        with self.assertRaises(ValorNuloError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                None,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_publico_esperado_tipo_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                "string",
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_duracao_show_nula(self):
        with self.assertRaises(ValorNuloError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                100,
                None,
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_duracao_show_tipo_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                100,
                12345,
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_visivel_nulo(self):
        with self.assertRaises(ValorNuloError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                100,
                "1h",
                None,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_visivel_tipo_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                100,
                "1h",
                "string",
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_tipo_pagamento_nulo(self):
        with self.assertRaises(ValorNuloError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                100,
                "1h",
                True,
                None,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_tipo_pagamento_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                100,
                "1h",
                True,
                "invalid",
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                1,
            )

    def test_validar_momento_pagamento_nulo(self):
        with self.assertRaises(ValorNuloError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                None,
                [],
                1,
            )

    def test_validar_momento_pagamento_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                "invalid",
                [],
                1,
            )

    def test_validar_estilos_nulo(self):
        with self.assertRaises(ValorNuloError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                None,
                1,
            )

    def test_validar_estilos_tipo_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                "string",
                1,
            )

    def test_validar_dono_nulo(self):
        with self.assertRaises(ValorNuloError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                None,
            )

    def test_validar_dono_tipo_incorreto(self):
        with self.assertRaises(TipoIncorretoError):
            Demanda(
                1,
                date.today(),
                5,
                True,
                100,
                "1h",
                True,
                TipoPagamentoEnum.FIXO,
                MomentoPagamentoEnum.ANTECIPADO,
                [],
                "string",
            )

    @patch("BancoDeDados_Pessoa3.Demanda.query.filter_by")
    def test_GetDemandas(self, mock_filter_by):
        mock_filter_by.return_value.all.return_value = ["demanda1", "demanda2"]

        result = BancoDeDados.GetDemandas()

        mock_filter_by.assert_called_once_with(visivel=True)
        self.assertEqual(result, ["demanda1", "demanda2"])

    @patch("BancoDeDados_Pessoa3.Demanda.query.filter_by")
    def test_GetDemandas_invalido(self, mock_filter_by):
        mock_filter_by.return_value.all.return_value = []

        result = BancoDeDados.GetDemandas()

        mock_filter_by.assert_called_once_with(visivel=True)
        self.assertEqual(result, [])

    @patch("BancoDeDados_Pessoa3.Demanda.query.filter_by")
    def test_GetDemandas_ComIdDono(self, mock_filter_by):
        mock_filter_by.return_value.all.return_value = ["demanda1", "demanda2"]

        id_dono = 1
        result = BancoDeDados.GetDemandas(id_dono)

        mock_filter_by.assert_called_once_with(dono=id_dono)
        self.assertEqual(result, ["demanda1", "demanda2"])

    @patch("BancoDeDados_Pessoa3.Demanda.query.filter_by")
    def test_GetDemandas_ComIdDono_invalido(self, mock_filter_by):
        mock_filter_by.return_value.all.return_value = []

        id_dono = 2
        result = BancoDeDados.GetDemandas(id_dono)

        mock_filter_by.assert_called_once_with(dono=id_dono)
        self.assertEqual(result, [])

    @patch("BancoDeDados_Pessoa3.Demanda.query.get")
    def test_GetDemanda(self, mock_get):
        mock_demanda = MagicMock()
        mock_get.return_value = mock_demanda

        id_demanda = 1
        result = BancoDeDados.GetDemanda(id_demanda)

        mock_get.assert_called_once_with(id_demanda)
        self.assertEqual(result, mock_demanda)

    @patch("BancoDeDados_Pessoa3.Demanda.query.get")
    def test_GetDemanda_invalido(self, mock_get):
        mock_get.return_value = None

        id_demanda = 999
        result = BancoDeDados.GetDemanda(id_demanda)

        mock_get.assert_called_once_with(id_demanda)
        self.assertIsNone(result)

    @patch("BancoDeDados_Pessoa3.Demanda.query.get")
    @patch("BancoDeDados_Pessoa3.Match.query.get")
    @patch("BancoDeDados_Pessoa3.bd.session.commit")
    def test_FechaDemanda(self, mock_commit, mock_match_get, mock_demanda_get):
        mock_demanda = MagicMock()
        mock_demanda_get.return_value = mock_demanda
        mock_match = MagicMock()
        mock_match_get.return_value = mock_match
        mock_match.id_demanda = 1

        BancoDeDados.FechaDemanda(1)

        mock_match_get.assert_called_once_with(1)
        mock_demanda_get.assert_called_once_with(mock_match.id_demanda)
        self.assertFalse(mock_demanda.visivel)
        mock_commit.assert_called_once()

    @patch("BancoDeDados_Pessoa3.Demanda.query.get")
    @patch("BancoDeDados_Pessoa3.Match.query.get")
    @patch("BancoDeDados_Pessoa3.bd.session.commit")
    def test_FechaDemanda_demanda_invalida(
        self, mock_commit, mock_match_get, mock_demanda_get
    ):
        mock_match = MagicMock()
        mock_match_get.return_value = mock_match
        mock_demanda_get.return_value = None

        result = BancoDeDados.FechaDemanda(1)

        mock_match_get.assert_called_once_with(1)
        mock_demanda_get.assert_called_once_with(mock_match.id_demanda)
        mock_commit.assert_not_called()
        self.assertIsNone(result)

    @patch("BancoDeDados_Pessoa3.Demanda.query.get")
    @patch("BancoDeDados_Pessoa3.Match.query.get")
    @patch("BancoDeDados_Pessoa3.bd.session.commit")
    def test_LiberaDemanda(self, mock_commit, mock_match_get, mock_demanda_get):
        mock_demanda = MagicMock()
        mock_demanda_get.return_value = mock_demanda
        mock_match = MagicMock()
        mock_match_get.return_value = mock_match
        mock_match.id_demanda = 1

        BancoDeDados.LiberaDemanda(1)

        mock_match_get.assert_called_once_with(1)
        mock_demanda_get.assert_called_once_with(mock_match.id_demanda)
        self.assertTrue(mock_demanda.visivel)
        mock_commit.assert_called_once()

    @patch("BancoDeDados_Pessoa3.Match.query.get")
    @patch("BancoDeDados_Pessoa3.Demanda.query.get")
    @patch("BancoDeDados_Pessoa3.bd.session.commit")
    def test_LiberaDemanda_demanda_invalida(
        self, mock_commit, mock_demanda_get, mock_match_get
    ):
        mock_match = MagicMock()
        mock_match_get.return_value = mock_match
        mock_demanda_get.return_value = None

        result = BancoDeDados.LiberaDemanda(1)

        mock_match_get.assert_called_once_with(1)
        mock_demanda_get.assert_called_once_with(mock_match.id_demanda)
        mock_commit.assert_not_called()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()

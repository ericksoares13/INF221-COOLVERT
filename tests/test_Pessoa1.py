import unittest
from unittest.mock import patch
from BancoDeDados_Pessoa1 import BancoDeDados
from mock_models import *


class TestBancoDeDados(unittest.TestCase):

    @patch('BancoDeDados_Pessoa1.Pessoa')
    @patch('BancoDeDados_Pessoa1.bd.session.commit')
    @patch('BancoDeDados_Pessoa1.bd.session.add')
    def test_CriaPessoa(self, mock_add, mock_commit, mock_pessoa):
        mock_pessoa_instance = MagicMock()
        mock_pessoa.return_value = mock_pessoa_instance
        mock_pessoa_instance.id = 1

        obj = {'nome': 'Test User', 'email': 'test@example.com', 'senha': '123456', 'tipo': 'user'}
        pessoa_id = BancoDeDados.CriaPessoa(obj)

        mock_add.assert_called_once_with(mock_pessoa_instance)
        mock_commit.assert_called_once()

        self.assertIsInstance(pessoa_id, int)
        self.assertEqual(pessoa_id, 1)

    @patch('BancoDeDados_Pessoa1.Usuario')
    @patch('BancoDeDados_Pessoa1.bd.session.commit')
    @patch('BancoDeDados_Pessoa1.bd.session.add')
    def test_cria_usuario(self, mock_add, mock_commit, mock_usuario):
        obj = {'id': 1, 'celular': '123456789', 'documento': '11122233344'}
        mock_usuario_instance = mock_usuario.return_value

        BancoDeDados.CriaUsuario(obj)

        mock_usuario.assert_called_once_with(id=obj['id'], celular=obj['celular'], documento=obj['documento'])
        mock_add.assert_called_once_with(mock_usuario_instance)
        mock_commit.assert_called_once()

    @patch('BancoDeDados_Pessoa1.DadosBancario')
    @patch('BancoDeDados_Pessoa1.bd.session.commit')
    @patch('BancoDeDados_Pessoa1.bd.session.add')
    def test_cria_dados_bancario(self, mock_add, mock_commit, mock_dados_bancario):
        obj = {
            'id': 1,
            'num_cartao': '1234-5678-9012-3456',
            'nome_cartao': 'Test User',
            'cod_seguranca': '123',
            'validade': '12/25'
        }
        mock_dados_bancario_instance = mock_dados_bancario.return_value

        BancoDeDados.CriaDadosBancario(obj)

        mock_dados_bancario.assert_called_once_with(
            id=obj['id'],
            num_cartao=obj['num_cartao'],
            nome_cartao=obj['nome_cartao'],
            cod_seguranca=obj['cod_seguranca'],
            validade=obj['validade']
        )
        mock_add.assert_called_once_with(mock_dados_bancario_instance)
        mock_commit.assert_called_once()

    @patch('BancoDeDados_Pessoa1.BancoDeDados.CriaPessoa', return_value=1)
    @patch('BancoDeDados_Pessoa1.BancoDeDados.CriaUsuario')
    @patch('BancoDeDados_Pessoa1.Musico')
    @patch('BancoDeDados_Pessoa1.bd.session.commit')
    @patch('BancoDeDados_Pessoa1.bd.session.add')
    def test_cria_musico(self, mock_add, mock_commit, mock_musico, mock_cria_usuario, mock_cria_pessoa):
        obj = {
            'nome': 'Test User',
            'email': 'test@example.com',
            'senha': '123456',
            'tipo': 'musico',
            'nome_pessoal': 'Pessoal',
            'nome_artistico': 'Artistico',
            'descricao': 'Descricao'
        }
        mock_musico_instance = mock_musico.return_value

        result_id = BancoDeDados.CriaMusico(obj)

        mock_cria_pessoa.assert_called_once_with(obj)
        mock_cria_usuario.assert_called_once_with(obj)
        mock_musico.assert_called_once_with(
            id=1,
            nome_pessoal=obj['nome_pessoal'],
            nome_artistico=obj['nome_artistico'],
            descricao=obj['descricao']
        )
        mock_add.assert_called_once_with(mock_musico_instance)
        mock_commit.assert_called_once()

        self.assertEqual(result_id, 1)

    @patch('BancoDeDados_Pessoa1.BancoDeDados.CriaPessoa', return_value=1)
    @patch('BancoDeDados_Pessoa1.BancoDeDados.CriaUsuario')
    @patch('BancoDeDados_Pessoa1.Contratante')
    @patch('BancoDeDados_Pessoa1.bd.session.commit')
    @patch('BancoDeDados_Pessoa1.bd.session.add')
    def test_cria_contratante(self, mock_add, mock_commit, mock_contratante, mock_cria_usuario, mock_cria_pessoa):
        obj = {
            'nome': 'Test User',
            'email': 'test@example.com',
            'senha': '123456',
            'tipo': 'contratante',
            'nome_estabelecimento': 'Estabelecimento',
            'cep': '12345-678',
            'estado': 'SP',
            'cidade': 'Cidade',
            'bairro': 'Bairro',
            'numero': '123',
            'complemento': 'Apto 1'
        }
        mock_contratante_instance = mock_contratante.return_value

        result_id = BancoDeDados.CriaContratante(obj)

        mock_cria_pessoa.assert_called_once_with(obj)
        mock_cria_usuario.assert_called_once_with(obj)
        mock_contratante.assert_called_once_with(
            id=1,
            nome_estabelecimento=obj['nome_estabelecimento'],
            cep=obj['cep'],
            estado=obj['estado'],
            cidade=obj['cidade'],
            bairro=obj['bairro'],
            numero=obj['numero'],
            complemento=obj['complemento']
        )
        mock_add.assert_called_once_with(mock_contratante_instance)
        mock_commit.assert_called_once()

        self.assertEqual(result_id, 1)

    # --- TESTES DE VALIDAÇÕES PARA EXCEÇÕES ---
    def test_validacoes_pessoa(self):
        with self.assertRaises(ValorNuloError):
            Pessoa(nome="", email="test@example.com", senha=b"123456", tipo="user")

        with self.assertRaises(ValorNuloError):
            Pessoa(nome="Test User", email=None, senha=b"123456", tipo="user")

        with self.assertRaises(TipoIncorretoError):
            Pessoa(nome="Test User", email="test@example.com", senha="123456", tipo="user")  # senha deve ser bytes

        with self.assertRaises(TipoIncorretoError):
            Pessoa(nome="Test User", email="test@example.com", senha=b"123456", tipo=123)  # tipo deve ser string

    def test_validacoes_usuario(self):
        with self.assertRaises(TipoIncorretoError):
            Usuario(id="abc", celular="123456789", documento="11122233344")  # id deve ser inteiro

        with self.assertRaises(ValorNuloError):
            Usuario(id=1, celular="", documento="11122233344")

    def test_validacoes_dados_bancarios(self):
        with self.assertRaises(TipoIncorretoError):
            DadosBancario(id="abc", num_cartao="1234-5678-9012-3456", nome_cartao="Test User", cod_seguranca="123", validade="12/25")  # id deve ser inteiro

        with self.assertRaises(ValorNuloError):
            DadosBancario(id=1, num_cartao="", nome_cartao="Test User", cod_seguranca="123", validade="12/25")

    def test_validacoes_musico(self):
        with self.assertRaises(TipoIncorretoError):
            Musico(id="abc", nome_pessoal="Pessoal", nome_artistico="Artistico", descricao="Descricao")  # id deve ser inteiro

        with self.assertRaises(ValorNuloError):
            Musico(id=1, nome_pessoal="", nome_artistico="Artistico", descricao="Descricao")

    def test_validacoes_contratante(self):
        with self.assertRaises(TipoIncorretoError):
            Contratante(id="abc", nome_estabelecimento="Estabelecimento", cep="12345-678", estado="SP", cidade="Cidade", bairro="Bairro", numero="123", complemento="Apto 1")  # id deve ser inteiro

        with self.assertRaises(ValorNuloError):
            Contratante(id=1, nome_estabelecimento="", cep="12345-678", estado="SP", cidade="Cidade", bairro="Bairro", numero="123", complemento="Apto 1")


if __name__ == '__main__':
    unittest.main()

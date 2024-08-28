import unittest
from unittest.mock import patch, MagicMock, ANY
import bcrypt
from BancoDeDados_Pessoa1 import BancoDeDados
from mock_models import *

class TestBancoDeDados(unittest.TestCase):

    @patch('BancoDeDados_Pessoa1.BancoDeDados.session')
    @patch('BancoDeDados_Pessoa1.Pessoa')
    def test_cria_pessoa(self, MockPessoa, mock_session):
        obj = {'nome': 'Test User', 'email': 'test@example.com', 'senha': '123456', 'tipo': 'user'}
        mock_pessoa_instance = MockPessoa.return_value
        mock_pessoa_instance.id = 1

        result_id = BancoDeDados.CriaPessoa(obj)

        MockPessoa.assert_called_once_with(nome=obj['nome'], email=obj['email'], senha=ANY, tipo=obj['tipo'])
        mock_session.add.assert_called_once_with(mock_pessoa_instance)
        mock_session.commit.assert_called_once()

        self.assertEqual(result_id, mock_pessoa_instance.id)
        hash_senha = MockPessoa.call_args[1]['senha']
        self.assertTrue(bcrypt.checkpw(obj['senha'].encode('utf-8'), hash_senha))

    @patch('BancoDeDados_Pessoa1.BancoDeDados.session')
    @patch('BancoDeDados_Pessoa1.Usuario')
    def test_cria_usuario(self, MockUsuario, mock_session):
        obj = {'id': 1, 'celular': '123456789', 'documento': '11122233344'}
        mock_usuario_instance = MockUsuario.return_value

        BancoDeDados.CriaUsuario(obj)

        MockUsuario.assert_called_once_with(id=obj['id'], celular=obj['celular'], documento=obj['documento'])
        mock_session.add.assert_called_once_with(mock_usuario_instance)
        mock_session.commit.assert_called_once()

    @patch('BancoDeDados_Pessoa1.BancoDeDados.session')
    @patch('BancoDeDados_Pessoa1.DadosBancario')
    def test_cria_dados_bancario(self, MockDadosBancario, mock_session):
        obj = {'id': 1, 'num_cartao': '1234-5678-9012-3456', 'nome_cartao': 'Test User', 'cod_seguranca': '123', 'validade': '12/25'}
        mock_dados_bancario_instance = MockDadosBancario.return_value

        BancoDeDados.CriaDadosBancario(obj)

        MockDadosBancario.assert_called_once_with(id=obj['id'], num_cartao=obj['num_cartao'], nome_cartao=obj['nome_cartao'], cod_seguranca=obj['cod_seguranca'], validade=obj['validade'])
        mock_session.add.assert_called_once_with(mock_dados_bancario_instance)
        mock_session.commit.assert_called_once()

    @patch('BancoDeDados_Pessoa1.BancoDeDados.session')
    @patch('BancoDeDados_Pessoa1.BancoDeDados.CriaPessoa', return_value=1)
    @patch('BancoDeDados_Pessoa1.BancoDeDados.CriaUsuario')
    @patch('BancoDeDados_Pessoa1.Musico')
    def test_cria_musico(self, MockMusico, mock_cria_usuario, mock_cria_pessoa, mock_session):
        obj = {'nome': 'Test User', 'email': 'test@example.com', 'senha': '123456', 'tipo': 'musico', 'nome_pessoal': 'Pessoal', 'nome_artistico': 'Artistico', 'descricao': 'Descricao'}
        mock_musico_instance = MockMusico.return_value

        result_id = BancoDeDados.CriaMusico(obj)

        mock_cria_pessoa.assert_called_once_with(obj)
        mock_cria_usuario.assert_called_once_with(obj)
        MockMusico.assert_called_once_with(id=1, nome_pessoal=obj['nome_pessoal'], nome_artistico=obj['nome_artistico'], descricao=obj['descricao'])
        mock_session.add.assert_called_once_with(mock_musico_instance)
        mock_session.commit.assert_called_once()

        self.assertEqual(result_id, 1)

    @patch('BancoDeDados_Pessoa1.BancoDeDados.session')
    @patch('BancoDeDados_Pessoa1.BancoDeDados.CriaPessoa', return_value=1)
    @patch('BancoDeDados_Pessoa1.BancoDeDados.CriaUsuario')
    @patch('BancoDeDados_Pessoa1.Contratante')
    def test_cria_contratante(self, MockContratante, mock_cria_pessoa, mock_cria_usuario, mock_session):
        obj = {'nome': 'Test User', 'email': 'test@example.com', 'senha': '123456', 'tipo': 'contratante', 
               'nome_estabelecimento': 'Estabelecimento', 'cep': '12345-678', 'estado': 'SP', 
               'cidade': 'Cidade', 'bairro': 'Bairro', 'numero': '123', 'complemento': 'Apto 1'}
        mock_contratante_instance = MockContratante.return_value

        result_id = BancoDeDados.CriaContratante(obj)

        mock_cria_pessoa.assert_called_once_with(obj)
        mock_cria_usuario.assert_called_once_with(obj)
        MockContratante.assert_called_once_with(id=1, nome_estabelecimento=obj['nome_estabelecimento'], cep=obj['cep'], estado=obj['estado'], cidade=obj['cidade'], bairro=obj['bairro'], numero=obj['numero'], complemento=obj['complemento'])
        mock_session.add.assert_called_once_with(mock_contratante_instance)
        mock_session.commit.assert_called_once()

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

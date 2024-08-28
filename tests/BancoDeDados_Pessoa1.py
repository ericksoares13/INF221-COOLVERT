from mock_models import *

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Código copiado de app.__init__.py para remover as dependenias
app = Flask(__name__)
app.secret_key = "default_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
bd = SQLAlchemy(app)


class BancoDeDados: 
    # Pessoa 1
    session = bd.session
    @staticmethod
    def CriaPessoa(obj):
        with app.app_context():
            hash_senha =  bcrypt.hashpw(obj['senha'].encode('utf-8'), bcrypt.gensalt())
            nova_pessoa = Pessoa(nome=obj['nome'], email=obj['email'], senha=hash_senha, tipo=obj['tipo'])
            bd.session.add(nova_pessoa)
            bd.session.commit()
            return nova_pessoa.id
    
    @staticmethod
    def CriaUsuario(obj):
        with app.app_context():
            novo_usuario = Usuario(id=obj['id'], celular=obj['celular'], documento=obj['documento'])
            bd.session.add(novo_usuario)
            bd.session.commit()
            
    @staticmethod
    def CriaDadosBancario(obj):
        with app.app_context():
            novo_cartao = DadosBancario(id=obj['id'], num_cartao=obj['num_cartao'], nome_cartao=obj['nome_cartao'], cod_seguranca=obj['cod_seguranca'], validade=obj['validade'])
            bd.session.add(novo_cartao)
            bd.session.commit()
    
    @staticmethod
    def CriaMusico(obj):
        with app.app_context():
            obj['id'] = BancoDeDados.CriaPessoa(obj)
            BancoDeDados.CriaUsuario(obj)
            novo_musico = Musico(id=obj['id'], nome_pessoal=obj['nome_pessoal'], nome_artistico=obj['nome_artistico'], descricao=obj['descricao'])
            bd.session.add(novo_musico)
            bd.session.commit()
            return obj['id']
            
    @staticmethod
    def CriaContratante(obj):
        with app.app_context():
            obj['id'] = BancoDeDados.CriaPessoa(obj)
            BancoDeDados.CriaUsuario(obj)
            novo_contratante = Contratante(id=obj['id'], nome_estabelecimento=obj['nome_estabelecimento'], cep=obj['cep'], estado=obj['estado'], 
                                           cidade=obj['cidade'], bairro=obj['bairro'], numero=obj['numero'], complemento=obj['complemento'])
            bd.session.add(novo_contratante)
            bd.session.commit()
            return obj['id']
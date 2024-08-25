import bcrypt
from sqlalchemy.orm import joinedload

from app import app, bd
from app.models import *
from sqlalchemy import func

class BancoDeDados: 
    # Pessoa 1
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
    
    # Pessoa 2
    @staticmethod
    def Login(obj):
        with app.app_context():
            pessoa = None
            pessoa = Pessoa.query.filter_by(email=obj['identificador']).first()
            if pessoa is None:
                pessoa = Pessoa.query.filter_by(nome=obj['identificador']).first()
            if pessoa and pessoa.verifica_senha(obj['senha']):
                return pessoa
            else: 
                return None
    
    @staticmethod
    def VerificaEmail(email):
        with app.app_context():
            return False if Pessoa.query.filter_by(email=email).first() else True
    
    @staticmethod
    def VerificaNomeUsuario(nome):
        with app.app_context():
            return False if Pessoa.query.filter_by(nome=nome).first() else True
        
    @staticmethod
    def VerificaEstiloMusical(nome):
        with app.app_context():
            return False if EstiloMusical.query.filter_by(nome=nome).first() else True
        
    @staticmethod
    def CriaEstiloMusical(nome):
        with app.app_context():
            estiloMusical = EstiloMusical(nome=nome)
            bd.session.add(estiloMusical)
            bd.session.commit()
    
    @staticmethod
    def GetEstilosMusicais(id_demanda):
        with app.app_context():
            estilos = DemandaEstilos.query.filter_by(demanda=id_demanda).all()
            estilos_musicais = []
            for estilo in estilos:
                estilos_musicais.append(EstiloMusical.query.with_entities(EstiloMusical.nome).filter_by(id=estilo.estilo_musical).first()[0])
            return estilos_musicais
        
    # Pessoa 3        
    @staticmethod
    def CriaDemanda(obj):
        with app.app_context():
            nova_demanda = Demanda(data_show=obj['data_show'], raio_procurado=obj['raio_procurado'], fornece_equipamento=obj['fornece_equipamento'], 
            publico_esperado=obj['publico_esperado'], duracao_show=obj['duracao_show'], dono=obj['dono'],
            tipo_pagamento=TipoPagamentoEnum(obj['tipo_pagamento']), momento_pagamento=MomentoPagamentoEnum(obj['momento_pagamento']))
            for nome_estilo in obj['estilos']:
                estilo_musical = EstiloMusical.query.filter_by(nome=nome_estilo).first()
                nova_demanda.estilos.append(estilo_musical)
            contratante = Contratante.query.get(obj['dono'])
            bd.session.add(nova_demanda)
            bd.session.commit()
    
    @staticmethod
    def GetDemandas(id_dono=None):
        with app.app_context():
            if id_dono is None:
                return list(Demanda.query.filter_by(visivel=True).all())
            else:
                return list(Demanda.query.filter_by(dono=id_dono).all())

    @staticmethod
    def GetDemanda(id_demanda):
        with app.app_context():
            return Demanda.query.get(id_demanda)
        
    @staticmethod
    def FechaDemanda(id_match):
        with app.app_context():
            match = Match.query.get(id_match)
            demanda = Demanda.query.get(match.id_demanda)
            demanda.visivel = False
            bd.session.commit()
            
    @staticmethod
    def LiberaDemanda(id_match):
        with app.app_context():
            match = Match.query.get(id_match)
            demanda = Demanda.query.get(match.id_demanda)
            demanda.visivel = True
            bd.session.commit()
            
    # Pessoa 4
    @staticmethod
    def GetNomeUsuario(user_id):
        with app.app_context():
            return Pessoa.query.get(user_id).nome
            
    @staticmethod
    def CriaMatch(obj):
        with app.app_context():
            match = Match(id_musico=obj['id_musico'], id_demanda=obj['id_demanda'])
            bd.session.add(match)
            bd.session.commit()
            return match.id
    
    @staticmethod
    def GetMatch(id_match):
        with app.app_context():
            return Match.query.get(id_match)

    @staticmethod
    def GetMatches(id_demanda):
        with app.app_context():
            return list(Match.query.filter_by(id_demanda=id_demanda).all())

    @staticmethod
    def GetMatchesMusico(id_musico):
        with app.app_context():
            return list(Match.query.filter_by(id_musico=id_musico).all())
        
    @staticmethod
    def GetMusicos(id_demanda):
        with app.app_context():
            return [ id[0] for id in Match.query.with_entities(Match.id_musico).filter_by(id_demanda=id_demanda).all() ]
        
    # Pessoa 5
    @staticmethod
    def EnviaMensagem(obj):
        with app.app_context():
            mensagem = Mensagem(match=obj['match'], dono=obj['dono'], mensagem=obj['mensagem'])
            bd.session.add(mensagem)
            bd.session.commit()
    
    @staticmethod
    def GetChat(id_match):
        with app.app_context():
            return sorted(list(Mensagem.query.filter_by(match=id_match).all()), key=lambda x: x.horario)
    
    @staticmethod
    def CriaImagem(obj):
        with app.app_context():
            imagem = Imagem(dono=obj['dono'], nome=obj['nome'], tipo_foto=TipoFotoEnum(obj['tipo_foto']), caminho=obj['caminho'])
            bd.session.add(imagem)
            bd.session.commit()
            
    @staticmethod
    def GetImagemPerfil(dono):
        with app.app_context():
            return Imagem.query.filter_by(dono=dono, tipo_foto=TipoFotoEnum.PERFIL).first()
        
    @staticmethod
    def GetUser(id_user):
        with app.app_context():
            return Pessoa.query.get(id_user)
        
    @staticmethod
    def GetContratante(id_contratante):
        with app.app_context():
            return Contratante.query.get(id_contratante)
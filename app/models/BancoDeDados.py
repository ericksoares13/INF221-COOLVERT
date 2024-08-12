from app import app, bd
from flask import Flask, g
from app.models import *
import bcrypt

class BancoDeDados: 
    @staticmethod
    def Login(obj):
        with app.app_context():
            pessoa = Pessoa.query.filter_by(email=obj['email']).first()
            if pessoa and pessoa.verifica_senha(obj['senha']):
                return pessoa
            else: 
                return None
    
    @staticmethod
    def VerificaEmail(email):
        with app.app_context():
            return False if Pessoa.query.filter_by(email=email).first() else True
        
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
    def CriaMusico(obj):
        with app.app_context():
            obj['id'] = BancoDeDados.CriaPessoa(obj)
            BancoDeDados.CriaUsuario(obj)
            novo_musico = Musico(id=obj['id'], nome_pessoal=obj['nome_pessoal'], nome_artistico=obj['nome_artistico'])
            bd.session.add(novo_musico)
            bd.session.commit()
            
    @staticmethod
    def CriaContratante(obj):
        with app.app_context():
            obj['id'] = BancoDeDados.CriaPessoa(obj)
            BancoDeDados.CriaUsuario(obj)
            novo_contratante = Contratante(id=obj['id'], nome_estabelecimento=obj['nome_estabelecimento'], cidade=obj['cidade'])
            bd.session.add(novo_contratante)
            bd.session.commit()
        
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
    def CriaDemanda(obj):
        with app.app_context():
            nova_demanda = Demanda(data_show=obj['data_show'], raio_procurado=obj['raio_procurado'], fornece_equipamento=obj['fornece_equipamento'], 
                                   publico_esperado=obj['publico_esperado'], duracao_show=obj['duracao_show'], dono=obj['dono'],
                                   tipo_pagamento=TipoPagamentoEnum.FIXO if obj['pagamento_fixo'] else TipoPagamentoEnum.COUVERT, 
                                   momento_pagamento=MomentoPagamentoEnum.ANTECIPADO if obj['antecipado'] else MomentoPagamentoEnum.APOS_EVENTO)
            for nome_estilo in obj['estilos']:
                estilo_musical = EstiloMusical.query.filter_by(nome=nome_estilo).first()
                nova_demanda.estilos.append(estilo_musical)
            contratante = Contratante.query.get(obj['dono'])
            contratante.demandas.append(nova_demanda)
            bd.session.add(nova_demanda)
            bd.session.commit()
    
    @staticmethod
    def GetDemandas(id_dono=None):
        with app.app_context():
            if id_dono is None:
                return list(Demanda.query.all())
            else:
                return list(Demanda.query.filter_by(dono=id_dono).all())
            
    @staticmethod
    def CriaMatch(obj):
        with app.app_context():
            match = Match(id_musico=obj['id_musico'], id_demanda=obj['id_demanda'])
            bd.session.add(match)
            bd.session.commit()
            return match.id
        
    @staticmethod
    def GetMusicos(id_demanda):
        with app.app_context():
            return [ id[0] for id in Match.query.with_entities(Match.id_musico).filter_by(id_demanda=id_demanda).all() ]
        
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
    
        
    
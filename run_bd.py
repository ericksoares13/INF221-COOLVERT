from app import app, bd
from app.models.BancoDeDados import BancoDeDados
from app.models.Demanda import EstiloMusical
from datetime import date

if __name__ == '__main__':
    with app.app_context():
        bd.create_all() # Usado quando vai criar novas tabelas
        
        #Musico
        musico_obj = {
            'email': 'katyperry@diva.com',
            'senha': '123slay',
            'nome': 'katyPerryDiva',
            'tipo': 'M',
            'celular': '(31)987654321',
            'documento': '111.222.333-44',
            'nome_pessoal': 'Katherine Hudson',
            'nome_artistico': 'Katy Perry',
            'descricao': "Não precisa, I'm the queen."
        }
        
        #Contratante
        contratante_obj = {
            'email': 'rockin@rio.com',
            'senha': '654321',
            'nome': 'rockInRio',
            'tipo': 'C',
            'celular': '31123456789',
            'documento': '111.222.333-44',
            'nome_estabelecimento': 'Rock In Rio',
            'cep': '05407-002',
            'estado': 'RJ',
            'cidade': 'Rio de Janeiro',
            'bairro': 'Tijuca',
            'numero': 123,
            'complemento': 'Maior palco da cidade.',
        }
        
        #Dados Bancários 
        dadosBancarios_obj = {
            'num_cartao': '1111 2222 3333 4444',
            'nome_cartao': 'Rock In Rio',
            'cod_seguranca': 123,
            'validade': '01/30'
        }
        
        #Login errado - Katy Perry
        login_obj1 = {
            'identificador': 'katyperry@diva.com',
            'senha': '654321'
        }
        
        #Login certo - Rock In Rio
        login_obj2 = {
            'identificador': 'rockin@rio.com',
            'senha': '654321'
        } 
        
        if BancoDeDados.VerificaEmail(musico_obj['email']):
            musico_id = BancoDeDados.CriaMusico(musico_obj)

        if BancoDeDados.VerificaEmail(contratante_obj['email']):
            contratante_id = BancoDeDados.CriaContratante(contratante_obj)
            dadosBancarios_obj['id'] = contratante_id
          
        if BancoDeDados.Login(login_obj1):
            print("Login realizado com sucesso!")
        else: 
            print("Email ou senha incorretos.")
            
        contratante = BancoDeDados.Login(login_obj2)
        if contratante is not None:
            print("Login realizado com sucesso!")
        else: 
            print("Email ou senha incorretos.")
        login_obj2['identificador'] = 'rockInRio'
        contratante = BancoDeDados.Login(login_obj2)
        if contratante is not None:
            print("Login realizado com sucesso!")
        else: 
            print("Email ou senha incorretos.")
        print()
            
        #Estilos Musicais
        if BancoDeDados.VerificaEstiloMusical('Rock'):
            BancoDeDados.CriaEstiloMusical('Rock')
            
        if BancoDeDados.VerificaEstiloMusical('Pop'):
            BancoDeDados.CriaEstiloMusical('Pop')
            
        if BancoDeDados.VerificaEstiloMusical('MPB'):
            BancoDeDados.CriaEstiloMusical('MPB')
            
        if BancoDeDados.VerificaEstiloMusical('Sertanejo'):
            BancoDeDados.CriaEstiloMusical('Sertanejo')
            
        if BancoDeDados.VerificaEstiloMusical('Forró'):
            BancoDeDados.CriaEstiloMusical('Forró')
            
        if BancoDeDados.VerificaEstiloMusical('Funk'):
            BancoDeDados.CriaEstiloMusical('Funk')
            
        if BancoDeDados.VerificaEstiloMusical('Eletrônico'):
            BancoDeDados.CriaEstiloMusical('Eletrônico')
            
        if BancoDeDados.VerificaEstiloMusical('Axé'):
            BancoDeDados.CriaEstiloMusical('Axé')
                
        if BancoDeDados.VerificaEstiloMusical('Bossa Nova'):
            BancoDeDados.CriaEstiloMusical('Bossa Nova')
            
        #Demanda
        demanda_obj = {
            'data_show': date(2024, 9, 1),
            'raio_procurado': 2000,
            'fornece_equipamento': True,
            'publico_esperado': 100000,
            'duracao_show': '4h',
            'tipo_pagamento': 'Fixo', # ou 'Couvert'
            'momento_pagamento': 'Antecipado', # ou 'Após o evento'
            'estilos': ['Rock', 'Pop'],
            'dono': contratante.id
        }
        
        BancoDeDados.CriaDemanda(demanda_obj) # execute apenas pra não ficar repetindo
        print('Demandas:')
        demandas = BancoDeDados.GetDemandas(contratante.id)
        for demanda in demandas:
            print(demanda)
            estilos_demanda = BancoDeDados.GetEstilosMusicais(demanda.id)
            print(f'Estilos musicais: {estilos_demanda}')
        print()
            
        #Match
        musico = BancoDeDados.Login({'identificador': 'katyperry@diva.com', 'senha': '123slay'})
        
        match_obj = {
            'id_musico': musico.id,
            'id_demanda': demandas[0].id
        }
        match_id = BancoDeDados.CriaMatch(match_obj)
        
        #Candidatos a demanda 
        candidatos = BancoDeDados.GetMusicos(demandas[0].id)
        print('Candidatos:')
        for candidato in candidatos:
            print(candidato)
        print()
        
        #Mensagem
        mensagem_obj1 = {
            'match': match_id,
            'dono': musico.id,
            'mensagem': 'Sou foda, o resto é moda.'
        }
        
        mensagem_obj2 = {
            'match': match_id,
            'dono': contratante.id,
            'mensagem': 'QUEEN!!!'
        }
        
        BancoDeDados.EnviaMensagem(mensagem_obj1)
        BancoDeDados.EnviaMensagem(mensagem_obj2)
        
        #Chat 
        chat = BancoDeDados.GetChat(match_id)
        print('Mensagens:')
        for mensagem in chat: 
            print(mensagem)
        print()
            
        #Perfil
        perfil_obj = {
            'id': musico.id,
            'nome_instagram': 'katyperry',
            'link_instagram': 'https://www.instagram.com/KatyPerry',
            'link_spotify': 'https://open.spotify.com/intl-pt/artist/6jJ0s89eD6GaHleKKya26X?si=iHGz_WvQQi-4q0KoAGoaqw',
            'link_youtube': 'www.youtube.com/@KatyPerry',
            'descricao': "Não precisa, I'm the queen."
        }
        
        BancoDeDados.CriaPerfil(perfil_obj)
        perfil = BancoDeDados.GetPerfil(musico.id)
        print(f'Perfil Katy Perry:')
        print(perfil)
        print()
        
        
        #Imagens
        imagem_obj1 = {
            'dono': musico.id,
            'nome': 'imagem1',
            'tipo_foto': 'Perfil',
            'caminho': '../static/images/katy.png'
        }
        
        imagem_obj2 = {
            'dono': musico.id,
            'nome': 'imagem2',
            'tipo_foto': 'Instagram',
            'caminho': '../static/images/katy.png'
        }
        
        imagem_obj3 = {
            'dono': musico.id,
            'nome': 'imagem3',
            'tipo_foto': 'portfólio',
            'caminho': '../static/images/katy.png'
        }
        
        imagem_obj4 = {
            'dono': musico.id,
            'nome': 'imagem4',
            'tipo_foto': 'portfólio',
            'caminho': '../static/images/katy.png'
        }
        
        BancoDeDados.CriaImagem(imagem_obj1)
        BancoDeDados.CriaImagem(imagem_obj2)
        BancoDeDados.CriaImagem(imagem_obj3)
        BancoDeDados.CriaImagem(imagem_obj4)
        
        get_imagens_obj1 = {
            'dono': musico.id,
            'tipo_foto': None
        }
        
        get_imagens_obj2 = {
            'dono': musico.id,
            'tipo_foto': 'portfólio'
        }
        
        print(f'Todas as imagens de Katy Perry:')
        imagens = BancoDeDados.GetImagens(get_imagens_obj1)
        for imagem in imagens:
            print(imagens)
        print()
        
        print(f'Apenas as imagens de portfólio da Katy Perry:')
        imagens = BancoDeDados.GetImagens(get_imagens_obj2)
        for imagem in imagens:
            print(imagens)
        print()
            
        imagem = BancoDeDados.GetImagemPerfil(musico.id)
        print(f'Foto de perfil da Katy Perry:')
        print(imagem)
        print()
        
        #Avaliação
        #* Estou exemplificando de Contratante pra músico mas pode ser o contrário
        avaliacao_obj1 = { 
            'dono': contratante.id,
            'perfil': perfil.id,
            'parte_avaliacao': 'Pagamento',
            'estrelas': 5, 
            'comentario': 'Pagou certinho'
        }
        
        avaliacao_obj2 = { 
            'dono': contratante.id,
            'perfil': perfil.id,
            'parte_avaliacao': 'Pontualidade',
            'estrelas': 4, 
            'comentario': 'Chegou na hora'
        }
        # Outras 'parte_avaliacao': {"Qualidade equipamento de som", "Veracidade das informações", "Divulgação do show"}
        
        BancoDeDados.CriaAvaliacao(avaliacao_obj1)
        BancoDeDados.CriaAvaliacao(avaliacao_obj2)
        
        procura_avaliacao_obj1 = {
            'dono': contratante.id,
            'perfil': perfil.id,
            'parte_avaliacao': 'Qualidade equipamento de som',
        }
        
        procura_avaliacao_obj2 = {
            'dono': contratante.id,
            'perfil': perfil.id,
            'parte_avaliacao': 'Pontualidade',
        }
        
        avaliacao = BancoDeDados.GetAvaliacao(procura_avaliacao_obj1)
        if avaliacao is None: 
            print('Não encontrou avaliação!')
        avaliacao = BancoDeDados.GetAvaliacao(procura_avaliacao_obj2)
        if avaliacao is not None: 
            print(f'Encontrou avaliação: {avaliacao}')
        print()
        
        print(f'Número de avaliações do perfil {perfil.id}: {BancoDeDados.GetNumAvaliacoes(perfil.id)}')
        print(f'Média de estrelas das avaliações do perfil {perfil.id}: {BancoDeDados.GetMediaEstrelas(perfil.id)}')
        print()
        
        avaliacoes_obj1 = {
            'perfil': perfil.id,
            'parte_avaliacao': None # Retorna todas as avaliações daquele perfil
        }
        
        avaliacoes_obj2 = {
            'perfil': perfil.id,
            'parte_avaliacao': 'Pontualidade' # Retorna apenas de um tipo específico
        }
        
        avaliacoes = BancoDeDados.GetAvaliacoes(avaliacoes_obj1)
        print(f'Todas as avaliações do perfil {perfil.id}:')
        for avaliacao in avaliacoes:
            print(avaliacao)
        print()
        
        avaliacoes = BancoDeDados.GetAvaliacoes(avaliacoes_obj2)
        print(f'Avaliações sobre "Pontualidade" do perfil {perfil.id}:')
        for avaliacao in avaliacoes:
            print(avaliacao)
        print()
        
        BancoDeDados.ExcluiAvaliacao(avaliacoes[0])
        if BancoDeDados.GetAvaliacao(procura_avaliacao_obj2) is None:
            print('Avaliação deletada com sucesso!')
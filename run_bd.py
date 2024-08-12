from app import app, bd
from app.models.BancoDeDados import BancoDeDados
from app.models.Demanda import EstiloMusical
from datetime import date

if __name__ == '__main__':
    with app.app_context():
        #bd.create_all() # Usado quando vai criar novas tabelas
        
        #Musico
        musico_obj = {
            'email': 'katyperry@diva.com',
            'senha': '123slay',
            'nome': 'katyPerryDiva',
            'tipo': 'M',
            'celular': '(31)987654321',
            'documento': '111.222.333-44',
            'nome_pessoal': 'Katherine Hudson',
            'nome_artistico': 'Katy Perry'
        }
        
        #Contratante
        contratante_obj = {
            'email': 'rockin@rio.com',
            'senha': '654321',
            'nome': 'rockInRio',
            'tipo': 'C',
            'celular': '31123456789',
            'documento': '12.345.678/0001-00',
            'nome_estabelecimento': 'Rock In Rio',
            'cidade': 'Rio de Janeiro, RJ'
        }
        
        #Login errado - Katy Perry
        login_obj1 = {
            'email': 'katyperry@diva.com',
            'senha': '654321'
        }
        
        #Login certo - Rock In Rio
        login_obj2 = {
            'email': 'rockin@rio.com',
            'senha': '654321'
        }
        
        if BancoDeDados.VerificaEmail(musico_obj['email']):
            musico = BancoDeDados.CriaMusico(musico_obj)

        if BancoDeDados.VerificaEmail(contratante_obj['email']):
            contratante = BancoDeDados.CriaContratante(contratante_obj)
          
        if BancoDeDados.Login(login_obj1):
            print("Login realizado com sucesso!")
        else: 
            print("Email ou senha incorretos.")
            
        contratante = BancoDeDados.Login(login_obj2)
        if contratante is not None:
            print("Login realizado com sucesso!")
        else: 
            print("Email ou senha incorretos.")
            
        #Demanda
        demanda_obj = {
            'data_show': date(2024, 9, 1),
            'raio_procurado': 2000,
            'fornece_equipamento': True,
            'publico_esperado': 100000,
            'duracao_show': '4h',
            'pagamento_fixo': True,
            'antecipado': True, 
            'estilos': ['Rock', 'Pop'],
            'dono': contratante.id
        }
        
        BancoDeDados.CriaDemanda(demanda_obj)
        
        '''
        estilosMusicais = [ 
            EstiloMusical(nome='Rock'), 
            EstiloMusical(nome='Pop'), 
            EstiloMusical(nome='MPB'), 
            EstiloMusical(nome='Sertanejo'),
            EstiloMusical(nome='Forró'),
            EstiloMusical(nome='Funk'),
            EstiloMusical(nome='Eletrônico'),
            EstiloMusical(nome='Axé'),
            EstiloMusical(nome='Bossa Nova'),
        ]
        
        for estilo in estilosMusicais:
            bd.session.add(estilo)
        '''
        
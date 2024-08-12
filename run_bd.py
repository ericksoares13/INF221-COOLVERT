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
            'pagamento_fixo': True,
            'antecipado': True, 
            'estilos': ['Rock', 'Pop'],
            'dono': contratante.id
        }
        
        BancoDeDados.CriaDemanda(demanda_obj) # execute apenas pra não ficar repetindo
        print('Demandas:')
        demandas = BancoDeDados.GetDemandas(contratante.id)
        for demanda in demandas:
            print(demanda)
            
        #Match
        musico = BancoDeDados.Login({'email': 'katyperry@diva.com', 'senha': '123slay'})
        
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
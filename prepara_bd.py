from app import app, bd
from app.models.Pessoa import Pessoa

if __name__ == '__main__':
    with app.app_context():
        bd.create_all()
    
        #nova_pessoa = Pessoa(nome="João", email="joao@example.com", senha="1234", tipo="M")
        #bd.session.add(nova_pessoa)
        #bd.session.commit()

from app import app, bd
from app.models.Pessoa import Pessoa
from app.models.Usuario import Usuario
from app.models.DadosBancario import DadosBancario

if __name__ == '__main__':
    with app.app_context():
        bd.create_all()
    
        nova_pessoa = Pessoa(nome="teste", email="teste@example.com", senha="11111", tipo="M")
        bd.session.add(nova_pessoa)
        bd.session.commit()
        
        nova_conta_bancaria = DadosBancario(id=nova_pessoa.id, agencia="0000-0", conta="00000000-0", numCartao= "1234567891234567", codSeguranca=123, validade="01/30")
        novo_usuario = Usuario(id=nova_pessoa.id, celular="(00)123456789", documento="1111222233334444")
        bd.session.add(nova_conta_bancaria)
        bd.session.add(novo_usuario)
        bd.session.commit()

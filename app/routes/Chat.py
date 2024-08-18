from app import app
from flask import render_template, session

from app.models.BancoDeDados import BancoDeDados

CHAT_HTML = "chat.html"


@app.route("/chat", methods=["GET", "POST"])
def chat():
    user_id = session.get("usuárioLogado")["id"]
    minha_imagem = BancoDeDados.GetImagemPerfil(2)
    outra_imagem = BancoDeDados.GetImagemPerfil(1)
    
    # Obtenha os dados do usuário logado e do outro usuário
    usuario_logado = BancoDeDados.GetUser(2)
    outro_usuario = BancoDeDados.GetUser(1)
    print(outro_usuario, outro_usuario.nome)
    
    # Obtenha as mensagens do chat
    chat = BancoDeDados.GetChat(1)
    mensagens = []
    for mensagem in chat:
        print(mensagem.dono, user_id)
        mensagens.append({
            'conteudo': mensagem.mensagem,
            'is_mine': (mensagem.dono == user_id),
            'imagem_perfil': minha_imagem.caminho if (mensagem.dono == user_id) else outra_imagem.caminho,
        })

    return render_template(CHAT_HTML, mensagens=mensagens, user=usuario_logado, other_user=outro_usuario)

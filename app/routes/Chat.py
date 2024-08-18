from app import app
from flask import render_template, session, request, jsonify, redirect, url_for

from app.models.BancoDeDados import BancoDeDados

CHAT_HTML = "chat.html"


@app.route("/chat", methods=["GET", "POST"])
def chat():
    id_user = session.get("usuárioLogado")["id"]
    id_outro = session.get('id_outro')["id"]
    match_id = session.get('match_id')["id"]

    minha_imagem = BancoDeDados.GetImagemPerfil(id_user)
    outra_imagem = BancoDeDados.GetImagemPerfil(id_outro)
    
    user_obj = BancoDeDados.GetUser(id_user)
    outro_obj = BancoDeDados.GetUser(id_outro)
    
    chat = BancoDeDados.GetChat(match_id)
    mensagens = []
    for mensagem in chat:
        mensagens.append({
            'conteudo': mensagem.mensagem,
            'is_mine': (mensagem.dono == id_user),
            'imagem_perfil': minha_imagem.caminho if (mensagem.dono == id_user) else outra_imagem.caminho,
        })

    return render_template(CHAT_HTML, mensagens=mensagens, user=user_obj, other_user=outro_obj)


@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    user_id = session.get("usuárioLogado")["id"]
    match_id = session.get('match_id')["id"]
    
    BancoDeDados.EnviaMensagem({
        'match': match_id,
        'dono': user_id,
        'mensagem': data['message']
    })
    
    return jsonify({"status": "success"})


@app.route("/chatDetails", methods=["GET", "POST"])
def chat_details():
    session["id_outro"] = {"id": request.form.get('chat_id_outro')}
    session["match_id"] = {"id": request.form.get('chat_id_match')}
    return redirect(url_for("chat"))

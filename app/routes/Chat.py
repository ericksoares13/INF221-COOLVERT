from app import app
from flask import render_template, session, request, jsonify, redirect, url_for

from app.models.BancoDeDados import BancoDeDados

CHAT_HTML = "chat.html"

@app.route("/chatDetails", methods=["GET", "POST"])
def chat_details():
    session["chat"] = {
        "id_outro": request.form.get('chat_id_outro'),
        "id_match": request.form.get('chat_id_match'),
        "origin_screen": request.form.get('origin_screen')
    }
    return redirect(url_for("chat"))

@app.route("/chat", methods=["GET", "POST"])
def chat():
    id_user = session.get("usuárioLogado")["id"]
    id_outro = session.get('chat')["id_outro"]
    id_match = session.get('chat')["id_match"]
    origin_screen = session.get('chat')["origin_screen"]
    
    minha_imagem = BancoDeDados.GetImagemPerfil(id_user)
    outra_imagem = BancoDeDados.GetImagemPerfil(id_outro)
    
    user_obj = BancoDeDados.GetUser(id_user)
    outro_obj = BancoDeDados.GetUser(id_outro)
    
    match = BancoDeDados.GetMatch(id_match)
    demanda = BancoDeDados.GetDemanda(match.id_demanda)
    
    chat = BancoDeDados.GetChat(id_match)
    mensagens = []
    for mensagem in chat:
        mensagens.append({
            'conteudo': mensagem.mensagem,
            'is_mine': (mensagem.dono == id_user),
            'imagem_perfil': (minha_imagem.caminho if minha_imagem else None) if (mensagem.dono == id_user) else (outra_imagem.caminho if outra_imagem else None),
        })

    return render_template(CHAT_HTML, mensagens=mensagens, user=user_obj, other_user=outro_obj, origin_screen=origin_screen, demanda=demanda)

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    user_id = session.get("usuárioLogado")["id"]
    match_id = session.get('chat')["id_match"]
    
    BancoDeDados.EnviaMensagem({
        'match': match_id,
        'dono': user_id,
        'mensagem': data['message']
    })
    
    return jsonify({"status": "success"})

@app.route("/close_demand", methods=["POST"])
def close_demand():
    BancoDeDados.FechaDemanda(session.get('chat')["id_match"])
    return jsonify({"status": "success"})
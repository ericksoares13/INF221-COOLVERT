from app import app
from flask import render_template, session

from app.models.BancoDeDados import BancoDeDados

CHAT_HTML = "chat.html"


@app.route("/chat", methods=["POST"])
def chat():
    return render_template(CHAT_HTML, chats=get_chat())


@app.route("/chat", methods=["GET"])
def get_chat():
    return render_template(CHAT_HTML, chats=get_chat())


def get_chat():
    contratante_id = session.get("usuárioLogado")["id"]
    demandas = BancoDeDados().GetDemandas(contratante_id)

    matches = []
    for demanda in demandas:
        matches.extend(BancoDeDados.GetMatches(demanda.id))

    chats = []
    for match in matches:
        imagem = BancoDeDados.GetImagemPerfil(match.id_musico)
        nome = BancoDeDados.GetNomeUsuario(match.id_musico)
        mensagens = BancoDeDados.GetChat(match.id)
        chat = {
            "image": imagem.caminho if imagem is not None else "",
            "name": nome,
            "last_message": mensagens[-1].mensagem if len(mensagens) > 0 else "",
        }
        chats.append(chat)

    return chats

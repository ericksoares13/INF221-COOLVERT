import re

from app import app
from flask import render_template, session

from app.models.BancoDeDados import BancoDeDados

CHAT_HIRER_HTML = "chatMusician.html"


@app.route("/chatMusico", methods=["POST"])
def chat_musico():
    return render_template(CHAT_HIRER_HTML, chats=get_chats())


@app.route("/chatMusico", methods=["GET"])
def get_chat_musico():
    return render_template(CHAT_HIRER_HTML, chats=get_chats())


def get_chats():
    musico_id = session.get("usuárioLogado")["id"]
    matches = BancoDeDados().GetMatchesMusico(musico_id)

    chats = []
    for match in matches:
        dono_demanda = BancoDeDados.GetDonoDaDemanda(match.id_demanda).dono
        imagem = BancoDeDados.GetImagemPerfil(dono_demanda)
        nome = BancoDeDados.GetNomeUsuario(dono_demanda)
        mensagens = BancoDeDados.GetChat(match.id)
        chat = {
            "musician_image": imagem.caminho if imagem is not None else "",
            "musician_name": nome,
            "last_message": mensagens[-1].mensagem if len(mensagens) > 0 else "",
        }
        chats.append(chat)

    return chats

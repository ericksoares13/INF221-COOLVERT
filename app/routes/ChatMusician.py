from app import app
from flask import render_template, session

from app.models.BancoDeDados import BancoDeDados

CHAT_MUSICIAN_HTML = "chatMusician.html"


@app.route("/chatMusico", methods=["POST"])
def chat_musico():
    return render_template(CHAT_MUSICIAN_HTML, chats=get_chats())


@app.route("/chatMusico", methods=["GET"])
def get_chat_musico():
    return render_template(CHAT_MUSICIAN_HTML, chats=get_chats())


def get_chats():
    musico_id = session.get("usuárioLogado")["id"]
    matches = BancoDeDados().GetMatchesMusico(musico_id)

    chats = []
    for match in matches:
        dono_demanda = BancoDeDados.GetDemanda(match.id_demanda).dono
        imagem = BancoDeDados.GetImagemPerfil(dono_demanda)
        nome = BancoDeDados.GetNomeUsuario(dono_demanda)
        mensagens = BancoDeDados.GetChat(match.id)
        chat = {
            "image": imagem.caminho if imagem is not None else "",
            "name": nome,
            "id_match": match.id,
            "id_outro": dono_demanda,
            "last_message": mensagens[-1].mensagem if len(mensagens) > 0 else "",
        }
        chats.append(chat)

    return chats

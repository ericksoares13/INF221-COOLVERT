from app import app
from flask import render_template, session

from app.models.BancoDeDados import BancoDeDados

CHAT_HIRER_HTML = "chatHirer.html"


@app.route("/chatContratante", methods=["POST"])
def chat_contratante():
    return render_template(CHAT_HIRER_HTML, chats=get_chats())


@app.route("/chatContratante", methods=["GET"])
def get_chat_contratante():
    return render_template(CHAT_HIRER_HTML, chats=get_chats())


def get_chats():
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

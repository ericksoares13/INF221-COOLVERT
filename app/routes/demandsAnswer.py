from flask import render_template, request, redirect, url_for, session
from app import app
from app.models.BancoDeDados import BancoDeDados

DEMAND_ANSWER = "demandsAnswer.html"

@app.route("/setinhaCandidatos", methods=["GET"])
def seta_demandsAnswer():
    return redirect(url_for("home_contratante"))

@app.route("/verMusicos", methods=["GET"])
def get_candidatos_demanda():
    candidatos = session.get("candidatos", {})
    return render_template(DEMAND_ANSWER, candidatos=candidatos)

@app.route("/verMusicos", methods=["POST"])
def ver_musicos():
    demanda_id = request.form.get("demanda_id")
    demanda = BancoDeDados.GetDemanda(demanda_id)
    
    dia, mes, ano = demanda.data_show.day, demanda.data_show.month, demanda.data_show.year
    matches = []
    for match in BancoDeDados().GetMatches(demanda_id):
        imagem = BancoDeDados.GetImagemPerfil(match.id_musico)
        matches.append({
            "id_musico": match.id_musico,
            "id_match": match.id,
            "nome": BancoDeDados.GetNomeUsuario(match.id_musico),
            "img": imagem.caminho if imagem is not None else ""
        })
    musicos = {
        "data_demanda": f"{dia:02d}/{mes:02d}/{ano:04d}",
        "musicos": matches
    }

    session["candidatos"] = musicos
    return render_template("demandsAnswer.html", candidatos=musicos)
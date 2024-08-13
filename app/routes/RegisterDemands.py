from app import app
from flask import render_template, request
from datetime import datetime
import re

@app.route('/cadastrarDemanda', methods=['POST'])
def cadastrar_demanda():
    data_show = request.form.get("data_show")
    raio_procurado = request.form.get("raio_procurado")
    estilos_marcados = request.form.getlist('estilo')
    equipamento_som = request.form.get('equipamento_som')
    publico_esperado = request.form.get('publico_esperado')
    duracao_show = request.form.get('duracao_show')
    pagamento = request.form.get('pagamento')
    modo_pagamento = request.form.get('modo_pagamento')

    print(modo_pagamento)

    if (data_show == ""):
        return render_template('registerDemands.html',
                               data_show=data_show,
                               raio_procurado=raio_procurado,
                               estilo=estilos_marcados,
                               equipamento_som=equipamento_som,
                               publico_esperado=publico_esperado,
                               duracao_show=duracao_show,
                               pagamento=pagamento,
                               modo_pagamento=modo_pagamento,
                               error="Campos obrigatórios não preenchidos.")


    try:
        data_py = datetime.strptime(data_show, "%d/%m/%Y")

        if data_py.date() < datetime.now().date():
            return render_template('registerDemands.html',
                                   data_show=data_show,
                                   raio_procurado=raio_procurado,
                                   estilo=estilos_marcados,
                                   equipamento_som=equipamento_som,
                                   publico_esperado=publico_esperado,
                                   duracao_show=duracao_show,
                                   pagamento=pagamento,
                                   modo_pagamento=modo_pagamento,
                                   error="A data informada é anterior ao dia atual.")
    except ValueError:
        return render_template('registerDemands.html',
                                    data_show=data_show,
                                    raio_procurado=raio_procurado,
                                    estilo=estilos_marcados,
                                    equipamento_som=equipamento_som,
                                    publico_esperado=publico_esperado,
                                    duracao_show=duracao_show,
                                    pagamento=pagamento,
                                    modo_pagamento=modo_pagamento,
                                    error="A data informada é inválida.")

    if (len(estilos_marcados) == 0) or (publico_esperado == "") or (duracao_show == "") or pagamento is None or modo_pagamento is None:
        return render_template('registerDemands.html',
                                   data_show=data_show,
                                   raio_procurado=raio_procurado,
                                   estilo=estilos_marcados,
                                   equipamento_som=equipamento_som,
                                   publico_esperado=publico_esperado,
                                   duracao_show=duracao_show,
                                   pagamento=pagamento,
                                   modo_pagamento=modo_pagamento,
                                   error="Campos obrigatórios não preenchidos.")

    return render_template('registerDemands.html',
                           data_show=data_show,
                           raio_procurado=raio_procurado,
                           estilo=estilos_marcados,
                           equipamento_som=equipamento_som,
                           publico_esperado=publico_esperado,
                           duracao_show=duracao_show,
                           pagamento=pagamento,
                           modo_pagamento=modo_pagamento)

@app.route('/cadastrarDemanda', methods=['GET'])
def get_cadastrar_demanda():
    return render_template("registerDemands.html")

from app import app
from flask import render_template, request
from datetime import datetime

@app.route('/cadastrarDemanda', methods=['POST'])
def cadastrarDemanda():
    data = request.form.get("data_show")

    if data == "":
        return render_template('registerDemands.html',
                               data_show=data, invalid_date="Campos obrigatórios não preenchidos.")

    try:
        dataPy = datetime.strptime(data, "%d/%m/%Y")

        if dataPy.date() < datetime.now().date():
            return render_template('registerDemands.html',
                           data_show=data, invalid_date="A data informada é anterior ao dia atual.")
        else:
            return render_template('registerDemands.html',
                                   data_show=data)
    except ValueError:
        return render_template('registerDemands.html',
                                   data_show=data, invalid_date="A data informada é inválida.")



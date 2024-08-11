from app import app
from flask import render_template, request


@app.route('/cadastro', methods=['POST'])
def cadastro():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if email.strip() == "" or username.strip() == "" or password.strip() == "" or confirm_password.strip() == "":
        print(render_template('register.html',
                               required_fields_error="Campos obrigatórios não preenchidos.",
                               email=email,
                               username=username,
                               password=password,
                               confirm_password=confirm_password))
        return render_template('register.html',
                               required_fields_error="Campos obrigatórios não preenchidos.",
                               email=email,
                               username=username,
                               password=password,
                               confirm_password=confirm_password)

    if password != confirm_password:
        return render_template('register.html',
                               pasword_error="As senhas não coincidem.",
                               email=email,
                               username=username,
                               password=password,
                               confirm_password=confirm_password)

    return render_template('index.html')
    return '', 204

from turtle import title
from flask import render_template,session,request,redirect,url_for,flash

from loja import app, db
from .forms import RegistrationForm

@app.route('/')
def home():
    return "Teste"

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
                    #form.password.data)
        #db_session.add(user)
        flash('Obrigado por se Registrar')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Pagina de Registro")
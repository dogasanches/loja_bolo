#from crypt import methods
from turtle import title
from flask import render_template,session,request,redirect,url_for,flash

from loja import app, db, bcrypt
from .forms import RegistrationForm,LoginFomulario
from .models import User
import os

@app.route('/')
def home():
    return render_template ('admin/index.html',title='Pagina Administrativa')

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,username=form.username.data, email=form.email.data,
        password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Obrigado {form.name.data} por se Registrar','error')
        return redirect(url_for('home'))
    return render_template('admin/registrar.html', form=form, title="Pagina de Registro")

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginFomulario(request.form)
    return render_template ('admin/login.html',form=form,title='Pagina Login')

    
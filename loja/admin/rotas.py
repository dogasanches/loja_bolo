from turtle import title
from flask import render_template,session,request,redirect,url_for

from loja import app, db

@app.route('/')
def home():
    return "Teste"

@app.route('/registrar')
def registrar():
    return render_template('admin/registrar.html', title="Registrar usuarios")
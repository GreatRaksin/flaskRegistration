from flask import render_template, redirect
from forms import *
from app import app, db


@app.route('/')
def index_page():
    return render_template('index.html', title='Главная страница')


@app.route('/register/', methods=['GET', 'POST'])
def register_page():
    return render_template('register.html', title='Регистрация')


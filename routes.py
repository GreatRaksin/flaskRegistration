from flask import render_template, redirect, request, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegisterForm
from app import app, db
from models import User


@app.route('/')
def index_page():
    return render_template('index.html', title='Главная страница')


@app.route('/register/', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if request.method == 'POST' and form.validate:
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(
            usename=form.username.data,
            password=form.password.data,
            phone=form.phone.data
        )
        db.session.add(new_user)
        db.session.commit()
        flash('You have successfully registered!', 'success')
        return redirect(url_for('login'))
    else:
        return render_template('register.html', title='Регистрация', form=form)


@app.route('/login/', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if request.method == 'POST' and form.validate:
        user = User.query.filter_by(email=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                flash('You have successfully signed in', 'success')
                return redirect(url_for('index_page'))
            else:
                flash('Username or Password incorrect', 'danger')
                return redirect(url_for('login_page'))
    return render_template('login.html', form=form)



from app import app, db
from flask import render_template, redirect, url_for, flash, request
from app.forms import LoginForm, RegistrationForm, RegistrationForm2
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login2():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():

        user = User.query.filter_by(username=register_form.username.data).first()
        if user is None or not user.check_password(register_form.password.data):
            flash('Invalid login credentials')
            return redirect(url_for('login'))
        login_user(user, remember=register_form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        flash('Thanks for logging in {}!'.format(current_user.username))
        return redirect(next_page)
    return render_template('login2.html', form=register_form)

# this was my original login page2 (the pw one)
@app.route('/login2', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login2.html', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register2():
    # register_form = RegistrationForm2()
    # if register_form.validate_on_submit():
    #     return redirect(url_for('login'))
    # return render_template('register.html', form=register_form)
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))
    register_form = RegistrationForm2()
    if register_form.validate_on_submit():
        user = User(username=register_form.username.data, email=register_form.email.data)
        user.set_password(register_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered!')
        return redirect(url_for('login'))
    return render_template('register.html', form=register_form)

@app.route('/index')
def index():
    return render_template('index.html', title='Home Page')

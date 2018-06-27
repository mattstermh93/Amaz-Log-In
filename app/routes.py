from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm, RegistrationForm, RegistrationForm2

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login2():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        return redirect(url_for('login2'))
    return render_template('login.html', form=register_form)


@app.route('/login2', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login2.html', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register2():
    register_form = RegistrationForm2()
    if register_form.validate_on_submit():
        return redirect(url_for('register'))
    return render_template('register.html', form=register_form)

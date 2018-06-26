from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm, RegistrationForm

@app.route('/login', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('login2.html', form=register_form)

@app.route('/')
@app.route('/login2', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for('login2'))
    return render_template('login2.html', form=login_form)

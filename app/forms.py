from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    email = StringField('Email (phone for mobile accounts)', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

class RegistrationForm2(FlaskForm):
    username = StringField('Your name', validators=[Length(min=8, max=24), DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-enter password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

    submit = SubmitField('Create your Amazon account')

# class RegistrationForm2(FlaskForm):
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Submit')

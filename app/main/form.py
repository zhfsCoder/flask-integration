from flask_wtf.file import FileField
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField, validators
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    username = StringField('username', [validators.Length(min=4, max=25)])
    emain    = StringField('Email Address', [validators.Length(min=6, max=35)])
    submit = SubmitField('Subit')

class PhotoForm(Form):
    photo = FileField('Your Photo')
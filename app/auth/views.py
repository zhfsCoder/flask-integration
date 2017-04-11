from flask import render_template
from . import auth
from .forms import LoginForm
from flask_login import login_user

@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)
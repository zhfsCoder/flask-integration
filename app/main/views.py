from flask import render_template, url_for
from . import main
from .form import NameForm

@main.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
from flask import render_template, url_for, session, redirect
from . import main
from .form import NameForm, PhotoForm

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'))

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filenam)
    else:
        filename = None
    return render_template('upload.html', form=form, filename=filename)

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
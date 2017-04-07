from flask import render_template, url_for, session, redirect
from . import main
from .form import NameForm, PhotoForm
from ..models import User, Role
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'),
                          known = session.get('known', False))

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
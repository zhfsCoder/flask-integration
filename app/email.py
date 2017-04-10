from flask_mail import Message
from . import mail
from flask import current_app, render_template

def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message('Flasky' + subject, 
                 sender=app.config['MAIL_USERNAME'], recipients=[to])
    msg.body = render_template(template + '.txt' , **kwargs)
    msg.html = render_template(template + '.html' , **kwargs)
    mail.send(msg)
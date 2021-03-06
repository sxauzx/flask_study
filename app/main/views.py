from flask import render_template, session, url_for, current_app, redirect
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from ..email import send_mail

@main.route('/', methods=['GET', 'POST'])
def index():
     form = NameForm()
     if form.validate_on_submit():
         user = User.query.filter_by(username=form.name.data).first()
         if user is None:
             user = User(username=form.name.data)
             db.session.add(user)
             session['known'] = False
             if current_app.config['FLASK_ADMIN']:
                 send_mail(current_app.config['FLASK_ADMIN'], 'New User', 'mail/new_user', user=user)
         else:
             session['known'] = True
         session['name'] = form.name.data
         return redirect(url_for('.index'))
     return render_template('index.html', name=session.get('name'),known=session.get('known',False),form=form)

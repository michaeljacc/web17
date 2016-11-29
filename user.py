from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import abort
from flask import session

from models import User


main = Blueprint('user', __name__)


def current_user():
    uid = session.get("user_id")
    if uid is not None:
        u = User.query.get(uid)
        return u


@main.route('/')
def login_view():
    u = current_user()
    if u is not None:
        return redirect('/blogs')
    return render_template('login.html')


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    avatar = u.av()
    u.avatar = avatar
    if u.valid():
        u.save()
    else:
        abort(410)
    return redirect(url_for('.login_view'))


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u = User(form)
    user = User.query.filter_by(username=u.username).first()
    if user is not None and user.validate_login(u):
        print("success")
        session['user_id'] = user.id
    else:
        print('FAILD')
    return redirect(url_for('.login_view'))



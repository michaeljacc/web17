from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import Blueprint

from models import Message

Model = Message

main = Blueprint('msg', __name__)


@main.route('/')
def index():
    # 查找所有的 msg 并返回
    msgs = Model.query.all()
    # print('msg index', msgs, len(msgs))
    return render_template('message.html', msgs=msgs)


@main.route('/msg/add', methods=['POST'])
def add():
    form = request.form
    Message.new(form)
    return redirect(url_for('.index'))

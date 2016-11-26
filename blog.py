from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import Blueprint

from models import Blog
from models import Comment

Model = Blog

main = Blueprint('blog', __name__)


@main.route('/blogs')
def index():
    ms = Model.query.all()
    return render_template('blog_list.html', blog_list=ms)


@main.route('/blog/new')
def new():
    return render_template('blog_new.html')


@main.route('/blog/add', methods=['POST'])
def add():
    form = request.form
    Blog.new(form)
    return redirect(url_for('.index'))


@main.route('/blog/<int:blog_id>')
def detail(blog_id):
    b = Blog.query.get(blog_id)
    cs = Comment.query.filter_by(blog_id=b.id).all()
    return render_template('blog_detail.html', blog=b, comments=cs)


@main.route('/blogs/blogs')
def blog():
    ms = Model.query.all()
    return render_template('blog_all.html', blog_list=ms)


@main.route('/comment/add', methods=['POST'])
def add_comment():
    form = request.form
    print('add comment', form)
    c = Comment.new(form)
    # url_for 的第二个参数可以匹配到动态路由
    # /blog/<c.blog_id>
    # 如果没有动态路由，参数就变成 query 的形式
    # /blog/new?blog_id=1
    return redirect(url_for('.detail', blog_id=c.blog_id))
    # return redirect('/blog/{}'.format(c.blog_id))

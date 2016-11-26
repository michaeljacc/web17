from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import time


# 以下都是套路
app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 指定数据库的路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web17.db'

db = SQLAlchemy(app)


# 定义一个 Model，继承自 db.Model
class Message(db.Model):
    __tablename__ = 'msgs'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    username = db.Column(db.Text)
    created_time = db.Column(db.Integer, default=0)

    @classmethod
    def new(cls, form):
        m = cls(form)
        m.save()
        return m

    def __init__(self, form):
        self.content = form.get('content', '')
        self.username = form.get('username', '')
        self.created_time = int(time.time())

    def __repr__(self):
        return u'<Msg {} {} from {}>'.format(self.id, self.content, self.username)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Blog(db.Model):
    __tablename__ = 'blogs'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    author = db.Column(db.Text)
    created_time = db.Column(db.Integer, default=0)

    @classmethod
    def new(cls, form):
        m = cls(form)
        m.save()
        return m

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.author = form.get('author', '')
        self.created_time = int(time.time())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Comment(db.Model):
    __tablename__ = 'comments'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    author = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    #
    blog_id = db.Column(db.Integer)

    @classmethod
    def new(cls, form):
        m = cls(form)
        m.save()
        return m

    def __init__(self, form):
        self.content = form.get('content', '')
        self.author = form.get('author', '')
        self.blog_id = int(form.get('blog_id'))
        self.created_time = int(time.time())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


if __name__ == '__main__':
    # 先 drop_all 删除所有数据库中的表
    # 再 create_all 创建所有的表
    db.drop_all()
    db.create_all()
    print('rebuild database')
    d = dict(
        title='新鲜的博客',
        content='第一篇文章',
        author='gua',
    )
    m = Blog.new(d)
    # # print('创建了msg', m)
    # # for i in range(3):
    # #     name = 'gua{}'.format(i)
    # #     md = dict(
    # #         content='hello',
    # #         username=name,
    # #     )
    # #     m = Message.new(md)
    # print('all', Message.query.all())

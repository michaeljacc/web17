from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import Blueprint

from message import main as routes_msg
from blog import main as routes_blog


app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便你设置什么内容都可以
app.secret_key = 'random string'
# 这一行是套路
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


"""
在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
蓝图可以拥有自己的静态资源路径、模板路径（现在还没涉及）
用法如下
"""
# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
app.register_blueprint(routes_msg)
app.register_blueprint(routes_blog)

# 运行代码
# 默认端口是 5000
if __name__ == '__main__':
    app.run(debug=True)

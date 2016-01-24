#coding=utf-8
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/hello/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/browser')
def print_browser():
    print request.headers
    user_agent=request.headers.get('User-Agent')
    return u'<h1>你的浏览器是：%s</h1>'%user_agent

@app.route('/ww')
def print_404():
    return u'<h1>不存在这个人哦</h1>',400

@app.route('/web/<host>')
def red(host):
    web_host='http://'+host+".com"
    print web_host
    return redirect(web_host)

@app.route('/welcome/<name>')
def welcome(name):
    return render_template("welcome.html",usr_name=name)

@app.route('/user1/<name>')
def test_user(name):
    return render_template("user1.html",usr_name=name)

@app.errorhandler(404)
def print_404(e):
    return render_template("404.html"),404

if __name__ == '__main__':
    bootstrap=Bootstrap(app)
    app.run(debug=True)

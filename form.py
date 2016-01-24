#-*- encoding:UTF-8 -*-
__author__ = 'kejun'
# create Datetime: 16-1-24 下午8:29
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config["SECRET_KEY"]="QiuGenDAFEIBAO"

@app.errorhandler(404)
def print_404(e):
    return render_template("404.html"),404

if __name__=="__main__":
    bootstrap=Bootstrap(app)
    app.run(debug=True)
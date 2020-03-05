from app import app
from flask import render_template, url_for


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('base.html')

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


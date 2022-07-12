from flask import Flask
from flask import render_template, redirect, url_for
from flask import session
from os import urandom, environ

app = Flask(__name__)
if environ.get('FLASK_ENV') == 'development':
    app.secret_key = b'Hakuna Matata \n\n\t'
else:
    app.secret_key = urandom(64)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    page = render_template('test.html', environ=environ.get('FLASK_ENV'))
    return page

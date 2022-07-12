from flask import Flask
from flask import render_template, redirect, url_for, request
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
    links = {'login_url': url_for('login'), 'registration_url': url_for('register')}
    page = render_template('login.html', **links)
    return page


@app.post('/register')
def register():
    request.form.get('email', None)
    return "<h1>not implemented yet</h1>"

from os import urandom, environ
from flask import Flask, g, render_template, redirect, url_for, request, abort  # , session
import sqlite3
from argon2 import PasswordHasher

ph = PasswordHasher()


app = Flask(__name__)
if environ.get('FLASK_ENV') == 'development':
    app.secret_key = b'Hakuna Matata \n\n\t'
else:
    app.secret_key = urandom(64).hex()
DATABASE = 'db.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(_):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def get_user(email):
    sql = '''
        SELECT * FROM users WHERE email = ?
    '''
    db = get_db()
    cur = db.execute(sql, (email,))
    return cur.fetchone()


def create_user(user_data):
    if get_user(user_data['email']):
        return False
    sql = '''
        INSERT INTO users
        (first_name, last_name, pass, email, phone, "role")
        VALUES(:first_name, :last_name, :hashed_pass, :email, :phone, 'student');
        '''
    user_data['hashed_pass'] = ph.hash(user_data['pass'])
    perform_dml(sql, user_data)
    user = get_user(user_data['email'])
    return user


def remove_user(who):
    sql = '''
        DELETE FROM {table} WHERE user_id = ?
        '''
    tables = ('user_class', 'user_group', 'allowed_user_group', 'users')
    deletes = {k: 0 for k in tables}
    for table in tables:
        affected_rows = perform_dml(sql.format(table=table), [who])
        deletes[table] = affected_rows
    return deletes


def perform_dml(dml_statement, params=None):
    db = get_db()
    cur = db.cursor()
    if not params:
        cur.execute(dml_statement)
    elif isinstance(params, list):
        if all(isinstance(param, (list, tuple)) and len(param) == 2 for param in params):
            cur.executemany(dml_statement, params)
        elif all(isinstance(param, (str, int, float))for param in params):
            cur.execute(dml_statement, params)
        else:
            raise ValueError('One of parameters for the query is invalid.')
    else:
        raise ValueError('Invalid type supplied for query as parameter list')
    db.commit()
    return cur.rowcount


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
    # in field_mapping keys are for pyton code, values are form field names.
    field_mapping = {
        'email': 'login',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'phone': 'phone',
        'pass': 'password'
    }
    # TODO: validate activation code
    if request.form.get('password', None) != request.form.get('repeat-password', ...):
        abort(405, 'passwords must match!')
    user_data = {k: request.form.get(v, None) for k, v in field_mapping.items()}
    user_record = create_user(user_data)
    print(*user_record, sep='\n')
    return repr(user_record)


"""
from os import urandom
from string import ascii_lowercase, digits
alphas = digits+ascii_lowercase
''.join(alphas[byte % len(alphas)] for byte in urandom(5))
"""

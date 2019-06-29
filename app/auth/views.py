from flask import render_template
from . import auth
from flask_login import LoginManager


@auth.route('/login')
def login():
    return render_template('auth/login.html')

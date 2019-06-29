from flask import render_template
from . import auth
from flask_login import LoginManager



def create_app(config_name):
    #....
    #Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    


@auth.route('/login')
def login():
    return render_template('auth/login.html')

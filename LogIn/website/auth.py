from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)    ##sets up a blueprint for the application

@auth.route('/Sign-Up')
def sign_up():
    return render_template("sign_up.html")

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"



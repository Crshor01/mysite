from flask import Blueprint, render_template

views = Blueprint('views', __name__)    ##sets up a blueprint for the application

@views.route('/')                        
def home():                             ##function runs whenever you go to the site
    return render_template("home.html")
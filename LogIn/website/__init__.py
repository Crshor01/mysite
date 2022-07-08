from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Flask and Python are fun!'      #cookies and info are kept safe

    from .views import views                                    #imports the views blueprint
    from .auth import auth                                      #imports the auth blueprint

    app.register_blueprint(views, url_prefix="/")               #registers the views blueprint
    app.register_blueprint(auth, url_prefix="/")                #registers the auth blueprint

    return app
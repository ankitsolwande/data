from flask import Flask
from config import app_config
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    from mypro.details.views import mod as users_module
    app.register_blueprint(users_module)
    return app

    
    

    

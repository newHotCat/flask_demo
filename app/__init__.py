from flask import Flask
from app.model.book import db

def createApp():
    "创建app"
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app

def register_blueprint(app):
    """
    注册蓝图
    """
    from app.web import web
    app.register_blueprint(web)
# -*- coding=utf-8 -*-
from flask import Flask, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_pagedown import PageDown
from config import config
from flask_uploads import UploadSet, configure_uploads, IMAGES,\
 patch_request_class

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
pagedown = PageDown()
login_manager.session_protection = 'strong'
login_manager.login_view = 'admin.login'
login_manager.login_message = u'请登入账号再进行下一步操作！'
photos = UploadSet('photos', IMAGES)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.config['SECRET_KEY'] = 'a random string'
    basepath = os.path.dirname(__file__)
    app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basepath, 'static/uploads')
    configure_uploads(app, photos)
    patch_request_class(app)  # 文件大小限制，默认为16MB

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)


    pagedown.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app

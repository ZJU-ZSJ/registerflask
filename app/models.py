# -*- coding=utf-8 -*-

from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash  # 引入密码加密 验证方法
from flask_login import UserMixin  # 引入flask-login用户模型继承类方法
from sqlalchemy.sql import func



class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sex = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    major = db.Column(db.Text)
    phone = db.Column(db.String(64))
    studentid = db.Column(db.String(64))
    email = db.Column(db.Text)
    question3 = db.Column(db.Integer) # 第一志愿
    question4 = db.Column(db.Integer)
    question5 = db.Column(db.Boolean, default=False)
    photo = db.Column(db.Text) #照片url

class User(UserMixin, db.Model):
    # 在使用Flask-Login作为登入功能�?在user模型要继承UserMimix�?
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    # real_name = db.Column(db.String(64), unique=True)
    # record = db.relationship('Record', backref='user')

    @property
    def password(self):
        raise AttributeError(u'不是可获取信息')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        # 增加password会通过generate_password_hash方法来加密储�?

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
        # 在登入时,我们需要验证明文密码是否和加密密码所吻合

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# -*- coding=utf-8 -*-
from . import admin
from flask import render_template, flash, redirect, url_for, request, jsonify, send_from_directory, abort
from flask_login import login_required, current_user, login_user, logout_user
from forms import LoginForm, RegistrationForm, EditRecordForm, ModifyForm, EditErecordForm
from ..models import User,Students
from .. import db
from xlwt import *
import os


@admin.route('/')
@login_required
def index():
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('admin.record'))
        flash(u'用户密码不正确')
    return render_template('admin/login.html', form=form)

@admin.route('/record', methods=['GET', 'POST'])
@login_required
def record():
    alist = Students.query.all()
    return render_template('admin/check.html', list=alist)

@admin.route('/modify/<int:id>', methods=['GET', 'POST'])
@login_required
def look(id):
    re = db.session.query(Students).filter(Students.id == id).one()
    return render_template("admin/look.html", re = re)



@admin.route('/register', methods=['GET', 'POST'])
def register():
    register_key = 'zhucema'
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.registerkey.data != register_key:
            flash(u'注册码不符，请返回重试')
            return redirect(url_for('admin.register'))
        else:
            if form.password.data != form.password2.data:
                flash(u'两次输入密码不一')
                return redirect(url_for('admin.register'))
            else:
                try:
                    user = User(username=form.username.data, password=form.password.data)
                    db.session.add(user)
                    db.session.commit()
                    flash(u'您已经成功注册')
                    return redirect(url_for('admin.login'))
                except:
                    db.session.rollback()
                    flash(u'用户名已存在')
    return render_template('admin/register.html', form=form)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'您已经登出了系统')
    return redirect(url_for('admin.index'))



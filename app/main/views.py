#-*- coding=utf-8 -*-
from flask import render_template, flash, redirect, url_for, request
from . import main
from .forms import Addstudentsform,UploadForm
from .. import db
from datetime import datetime
import datetime
import random
import string
import os
from werkzeug.utils import secure_filename
from .. import photos
from .. models import Students


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/first.html')


@main.route('/baoming', methods=['GET', 'POST'])
def baoming():
    form = Addstudentsform()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data,name=str(datetime.datetime.now())+form.studentid.data+'.')
        file_url = photos.url(filename)
        students = Students(studentid = form.studentid.data,name = form.name.data,sex = form.sex.data,grade = form.grade.data,major = form.major.data,phone = form.phone.data,email = form.email.data,question3 = form.wants1.data,question4 = form.wants2.data,question5 = form.follow.data,photo = file_url)
        i = 1
        while (i):
            try:
                db.session.add(students)
                db.session.commit()
                flash(u'报名表提交成功')
                print '1'
                i = 0
                return redirect(url_for('main.index'))
            except:
                db.session.rollback()
    else:
        file_url = None
    return render_template('main/index.html',form = form,file_url=file_url)


@main.route('/upload', methods=['POST', 'GET'])
def upload():
     if request.method == 'POST':
         f = request.files['file']
         basepath = os.path.dirname(__file__)  # 当前文件所在路径
         upload_path = os.path.join(basepath, '../static/upload',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
         f.save(upload_path)
         return redirect(url_for('main.upload'))
     return render_template('main/uploads.html')


html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>图片上传</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=photo>
         <input type=submit value=上传>
    </form>
    '''

@main.route('/up', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        file_url = photos.url(filename)
        return html + '<br><img src=' + file_url + '>'
    return html


#-*- coding=utf-8 -*-
from flask import render_template, flash, redirect, url_for, request,session,jsonify
from . import main
from .forms import Addstudentsform,UploadForm
from .. import db
from datetime import datetime
import datetime
import time
import random
import string
import os
from .. import photos,document
from .. models import Students
import pdfkit
import shutil
from docx.shared import Inches
from PIL import Image, ImageDraw, ImageFont, ImageFilter


@main.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('main.baoming'))



@main.route('/yanzheng')
def yanzheng():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=str)
    if a==session['code']:
        return jsonify(result='验证成功')
    else:
        return jsonify(result='失败')

@main.route('/changeimg')
def changeimg():
    code_url = codeimg()
    return jsonify(code_url = code_url)


@main.route('/add')
def inx():
    code_url= codeimg()
    return render_template('main/inx.html',code = code_url)


@main.route('/joinus', methods=['GET', 'POST'])
def baoming():
    form = Addstudentsform()
    if form.validate_on_submit():
        print form.ver.data
        if (form.wants1.data == form.wants2.data=='1') or (form.wants1.data == form.wants2.data=='2') or (int(form.wants1.data)+int(form.wants2.data) == 3):
            flash(u'技术部只能选择一个')
        elif (form.ver.data.upper()!=session['code']):
            flash(u'验证码错误')
        else:
            pname = str(time.time())+form.studentid.data
            filename = photos.save(form.photo.data,name=pname+'.')
            file_url = url_for('static', filename=('uploads/' + str(filename)))
            students = Students(studentid = form.studentid.data,name = form.name.data,sex = form.sex.data,grade = form.grade.data,major = form.major.data,phone = form.phone.data,email = form.email.data,question3 = form.wants1.data,
                                question4 = form.wants2.data,question5 = form.follow.data,photo = file_url,
                                intro = form.intro.data,why = form.why.data,what = form.what.data,day25 = form.day25.data,
                                day26 = form.day26.data,day27 = form.day27.data,day28 = form.day28.data,day291 = form.day291.data,
                                day29 =form.day29.data,day30 = form.day30.data,remarks = form.remarks.data,filename = filename,whywants1 = form.whywants1.data,whywants2 = form.whywants2.data )
            i = 1
            while (i):
                try:
                    db.session.add(students)
                    db.session.commit()
                    print '1'
                    i = 0
                    return render_template('main/ok.html')
                except:
                    db.session.rollback()
                    flash(u'提交失败')
    else:
        file_url = None
    code_url = codeimg()
    return render_template('main/index.html',form = form, code = code_url)

def codeimg():
    def rndChar():
        return chr(random.choice([random.randint(65, 90),random.randint(48,57)]))

    # 随机颜色1:
    def rndColor():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    # 随机颜色2:
    def rndColor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('arial.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    num = ''
    for t in range(4):
        ele = rndChar()
        num = str(num)+str(ele)
        draw.text((60 * t + 10, 10), ele, font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)

    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强（阈值更大）
    imgname = str(time.time())+'.jpg'
    image.save(imgname, 'jpeg');
    os.system("mv " + imgname + "  app/static/code/")
    code_url = url_for('static', filename=('code/' + str(imgname)))
    session['code'] = num
    return code_url


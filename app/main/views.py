#-*- coding=utf-8 -*-
from flask import render_template, flash, redirect, url_for, request,session,jsonify
from . import main
from .forms import Addstudentsform
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




@main.route('/end', methods=['GET', 'POST'])
def end():
    return render_template('main/end.html')





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


@main.route('/', methods=['GET', 'POST'])
def baoming():
    return redirect(url_for('main.end'))
    form = Addstudentsform()
    if form.validate_on_submit():
        if (form.ver.data.upper()!=session['code']):
            flash(u'提交失败：验证码错误')
        else:
            students = Students(studentid = form.studentid.data,name = form.name.data,sex = form.sex.data,grade = form.grade.data,major = form.major.data,phone = form.phone.data,email = form.email.data,question1 = form.question1.data,question2 = form.question2.data,question3 = form.question3.data,question4 = form.question4.data,
                                question5=form.question5.data,question6=form.question6.data,day242 = form.day242.data,day243 = form.day243.data,day244 = form.day244.data,day251 = form.day251.data,day252 = form.day252.data,day253 = form.day253.data,day254 = form.day254.data,day261 = form.day261.data,day262 = form.day262.data,day263 = form.day263.data)
            i = 1
            while (i):
                try:
                    db.session.add(students)
                    db.session.commit()
                    print '1'
                    i = 0
                    return render_template('main/finish.html')
                except:
                    db.session.rollback()
                    flash(u'提交失败，请仔细检查是否填写正确')
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


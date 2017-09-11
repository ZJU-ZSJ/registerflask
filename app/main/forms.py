#-*- coding=utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField,BooleanField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import Required, length, Regexp
from .. import photos




class Addstudentsform(FlaskForm):
    """
    用户提交维修记录的表单
    """
    name = StringField(u'* 姓名:', validators=[Required(), length(2, 5, message=u'姓名只允许2-5个字符！')])
    sex =  SelectField(u'* 性别:', choices=[('1',u'男'),('2',u'女')])
    studentid = StringField(u'* 学号:', validators=[Required(), length(10, 10, message=u'请正确填写学号')])
    phone = StringField(u'* 手机号:', validators=[Required(), length(11, 11, message=u'请正确填写手机号'), Regexp('[0-9]')])
    grade = SelectField(u'* 年级:', validators=[Required()],choices=[('1',u'大一'),('2',u'大二'),('3',u'大三'),('4',u'大四')])
    major =  StringField(u'* 专业:', validators=[Required()])
    email = StringField(u'邮箱:')
    wants1 = SelectField(u'* 第一志愿:', validators=[Required()],choices=[('1',u'电脑部'),('2',u'电器部'),('3',u'财外部'),('4',u'人资部'),('5',u'文宣部')])
    wants2 = SelectField(u'* 第二志愿:', validators=[Required()],choices=[('1',u'电脑部'),('2',u'电器部'),('3',u'财外部'),('4',u'人资部'),('5',u'文宣部')])
    follow = BooleanField(u'* 服从志愿请打勾')
    photo = FileField(u'照片上传', validators=[
        FileAllowed(photos, u'只能上传图片！'),
        FileRequired(u'文件未选择！')
    ])
    submit = SubmitField(u'提交')


class UploadForm(FlaskForm):
    photo = FileField(validators=[
        FileAllowed(photos, u'只能上传图片！'),
        FileRequired(u'文件未选择！')])
    submit = SubmitField(u'上传')
#-*- coding=utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField,BooleanField,SelectMultipleField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import Required, length, Regexp,Email
from .. import photos




class Addstudentsform(FlaskForm):
    """
    用户提交维修记录的表单
    """
    name = StringField(u'* 姓名:', validators=[Required(), length(2, 5, message=u'姓名只允许2-5个字符！')],render_kw={"placeholder": "Your name","style": "background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAWCAYAAAArdgcFAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA+5pVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ1dWlkOjY1RTYzOTA2ODZDRjExREJBNkUyRDg4N0NFQUNCNDA3IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkIzOUVGMUYxMDY3MTExRTI5OUZEQTZGODg4RDc1ODdCIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkIzOUVGMUYwMDY3MTExRTI5OUZEQTZGODg4RDc1ODdCIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDUzYgKE1hY2ludG9zaCkiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDowMTgwMTE3NDA3MjA2ODExODA4M0ZFMkJBM0M1RUU2NSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDowNjgwMTE3NDA3MjA2ODExODA4M0U3NkRBMDNEMDVDMSIvPiA8ZGM6dGl0bGU+IDxyZGY6QWx0PiA8cmRmOmxpIHhtbDpsYW5nPSJ4LWRlZmF1bHQiPmdseXBoaWNvbnM8L3JkZjpsaT4gPC9yZGY6QWx0PiA8L2RjOnRpdGxlPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PkX/peQAAACrSURBVHja7JSLCYAwDEQbJ3AER+kouoFu0FEcqSM4gk4QE4ggVRPxg1A8OFCSvkqC5xDRaSZ5ciTjyvzuzbMnwKjY34FHAx618yCQXQHAcVFE5+GoVijgyt3UN1/+hPKFd0a9ubxQa6naMjOdOY2jJAdjZIH7tJ8gzRNuZuho5MriUfpLNbhINXk4Cd27pN3AJVqvQlMPSxSz+oegqXuQhz9bNvDpJfY0CzAA6Ncngv5RALIAAAAASUVORK5CYII=) no-repeat 15px center;text-indent: 28px;x:4px;y:4px;background-color:white"})
    sex =  SelectField(u'* 性别:', choices=[('1',u'男'),('2',u'女')],)
    studentid = StringField(u'* 学号:', validators=[Required(), length(10, 10, message=u'请正确填写学号')])
    phone = StringField(u'* 手机号:', validators=[Required(), length(11, 11, message=u'请正确填写手机号'), Regexp('[0-9]')],render_kw={"style": "background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAYCAYAAADKx8xXAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA+5pVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ1dWlkOjY1RTYzOTA2ODZDRjExREJBNkUyRDg4N0NFQUNCNDA3IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjkxMkIyRkNGMDY5ODExRTI5OUZEQTZGODg4RDc1ODdCIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjkxMkIyRkNFMDY5ODExRTI5OUZEQTZGODg4RDc1ODdCIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDUzYgKE1hY2ludG9zaCkiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDowMTgwMTE3NDA3MjA2ODExODA4M0ZFMkJBM0M1RUU2NSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDowNjgwMTE3NDA3MjA2ODExODA4M0U3NkRBMDNEMDVDMSIvPiA8ZGM6dGl0bGU+IDxyZGY6QWx0PiA8cmRmOmxpIHhtbDpsYW5nPSJ4LWRlZmF1bHQiPmdseXBoaWNvbnM8L3JkZjpsaT4gPC9yZGY6QWx0PiA8L2RjOnRpdGxlPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Ps0LhyQAAABYSURBVHjaYmBgYHAA4g9A/J9I/AGqhyRNcM2MUAbJgImBTMCCxPYjUs8mimwc1TiqcdhrpElGToRinABbmbLg////DCAMYuNQg7OwSoBiXCUdecUjQIABAPPLSC2fm7UQAAAAAElFTkSuQmCC) no-repeat 15px center;text-indent: 28px;x:4px;y:4px;background-color:white"})
    grade = SelectField(u'* 年级:', validators=[Required()],choices=[('1',u'大一'),('2',u'大二'),('3',u'大三'),('4',u'大四')])
    major =  StringField(u'* 专业:', validators=[Required()])
    email = StringField(u'邮箱:',render_kw={"style": "background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAQCAYAAAAMJL+VAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA+5pVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ1dWlkOjY1RTYzOTA2ODZDRjExREJBNkUyRDg4N0NFQUNCNDA3IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjlGNDRFNDhFMDY3MzExRTI5OUZEQTZGODg4RDc1ODdCIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjI0QkFDRTQwMDY3MzExRTI5OUZEQTZGODg4RDc1ODdCIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDUzYgKE1hY2ludG9zaCkiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDowMTgwMTE3NDA3MjA2ODExODA4M0ZFMkJBM0M1RUU2NSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDowNjgwMTE3NDA3MjA2ODExODA4M0U3NkRBMDNEMDVDMSIvPiA8ZGM6dGl0bGU+IDxyZGY6QWx0PiA8cmRmOmxpIHhtbDpsYW5nPSJ4LWRlZmF1bHQiPmdseXBoaWNvbnM8L3JkZjpsaT4gPC9yZGY6QWx0PiA8L2RjOnRpdGxlPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PlSYaIgAAAB8SURBVHjavFQBDoAgCLz10p6GLyVtruWyC1RiYzo87mCiACDZNcgFqmUNEZHKfW0kgLxwPgIryRXkYAV5IzAr8pZrBo6QdwW8IhS7gVhO3POSCCRVDDVWEavOivtsdyZmHtORrhoBy6WeGCvu/tBcE+OerF8+u8jv+hBgADHfmSbFytyUAAAAAElFTkSuQmCC) no-repeat 15px center;text-indent: 28px;x:4px;y:4px;background-color:white"})
    wants1 = SelectField(u'* 第一志愿:', validators=[Required()],choices=[('2',u'电器部'),('1',u'电脑部'),('4',u'人资部'),('5',u'文宣部'),('3',u'财外部')])
    whywants1 = TextAreaField(u'* 请简述你选择该部门作为第一志愿的原因。', validators=[Required()])
    wants2 = SelectField(u'* 第二志愿:', validators=[Required()],choices=[('3',u'财外部'),('2',u'电器部'),('1',u'电脑部'),('4',u'人资部'),('5',u'文宣部')])
    whywants2 = TextAreaField(u'* 请简述你选择该部门作为第二志愿的原因。', validators=[Required()])
    intro = TextAreaField(u'* 个人简介（包括性格特点、社团经历、爱好特长等方面）:', validators=[Required()])
    why = TextAreaField(u'* 请简述你想加入E志者协会的理由。', validators=[Required()])
    what = TextAreaField(u'* 请简述你能给E志者带来什么。', validators=[Required()])
    follow = BooleanField(u'服从调剂请打勾')
    day25 = BooleanField(u'9.25晚18:30-22:00')
    day26 = BooleanField(u'9.26晚18:30-22:00')
    day27 = BooleanField(u'9.27晚18:30-22:00')
    day28 = BooleanField(u'9.28晚18:30-22:00')
    day291 = BooleanField(u'9.29下午14:00-17:30')
    day29 = BooleanField(u'9.29晚18:30-22:00')
    day30 = BooleanField(u'9.30下午14:00-17:30')
    remarks = StringField(u'有关面试时间的备注:')
    photo = FileField(u'照片上传(上传纯中文名照片可能会出错)，大小限制：3MB', validators=[
        FileAllowed(photos, u'只能上传图片！'),
        FileRequired(u'文件未选择！')
    ])
    ver = StringField(u'* 请输入验证码(不区分大小写):', validators=[Required(), length(4, 4, message=u'请正确填写验证码')])
    submit = SubmitField(u'提交')


class UploadForm(FlaskForm):
    photo = FileField(validators=[
        FileAllowed(photos, u'只能上传图片！'),
        FileRequired(u'文件未选择！')])
    submit = SubmitField(u'上传')
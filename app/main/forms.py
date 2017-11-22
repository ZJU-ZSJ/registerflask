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
    sex =  SelectField(u'* 性别:', choices=[('0', u'请选择'),('1',u'男'),('2',u'女')],)
    studentid = StringField(u'* 学号:', validators=[Required(), length(10, 10, message=u'请正确填写学号')])
    phone = StringField(u'* 手机号:', validators=[Required(), length(11, 11, message=u'请正确填写手机号'), Regexp('[0-9]')],render_kw={"style": "background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAYCAYAAADKx8xXAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA+5pVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ1dWlkOjY1RTYzOTA2ODZDRjExREJBNkUyRDg4N0NFQUNCNDA3IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjkxMkIyRkNGMDY5ODExRTI5OUZEQTZGODg4RDc1ODdCIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjkxMkIyRkNFMDY5ODExRTI5OUZEQTZGODg4RDc1ODdCIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDUzYgKE1hY2ludG9zaCkiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDowMTgwMTE3NDA3MjA2ODExODA4M0ZFMkJBM0M1RUU2NSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDowNjgwMTE3NDA3MjA2ODExODA4M0U3NkRBMDNEMDVDMSIvPiA8ZGM6dGl0bGU+IDxyZGY6QWx0PiA8cmRmOmxpIHhtbDpsYW5nPSJ4LWRlZmF1bHQiPmdseXBoaWNvbnM8L3JkZjpsaT4gPC9yZGY6QWx0PiA8L2RjOnRpdGxlPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Ps0LhyQAAABYSURBVHjaYmBgYHAA4g9A/J9I/AGqhyRNcM2MUAbJgImBTMCCxPYjUs8mimwc1TiqcdhrpElGToRinABbmbLg////DCAMYuNQg7OwSoBiXCUdecUjQIABAPPLSC2fm7UQAAAAAElFTkSuQmCC) no-repeat 15px center;text-indent: 28px;x:4px;y:4px;background-color:white"})
    grade = SelectField(u'* 年级:', validators=[Required()],choices=[('0', u'请选择'),('1',u'大一'),('2',u'大二'),('3',u'大三'),('4',u'大四')])
    major =  StringField(u'* 行政班:', validators=[Required()])
    email = StringField(u'邮箱:',render_kw={"style": "background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAQCAYAAAAMJL+VAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA+5pVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ1dWlkOjY1RTYzOTA2ODZDRjExREJBNkUyRDg4N0NFQUNCNDA3IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjlGNDRFNDhFMDY3MzExRTI5OUZEQTZGODg4RDc1ODdCIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjI0QkFDRTQwMDY3MzExRTI5OUZEQTZGODg4RDc1ODdCIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDUzYgKE1hY2ludG9zaCkiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDowMTgwMTE3NDA3MjA2ODExODA4M0ZFMkJBM0M1RUU2NSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDowNjgwMTE3NDA3MjA2ODExODA4M0U3NkRBMDNEMDVDMSIvPiA8ZGM6dGl0bGU+IDxyZGY6QWx0PiA8cmRmOmxpIHhtbDpsYW5nPSJ4LWRlZmF1bHQiPmdseXBoaWNvbnM8L3JkZjpsaT4gPC9yZGY6QWx0PiA8L2RjOnRpdGxlPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PlSYaIgAAAB8SURBVHjavFQBDoAgCLz10p6GLyVtruWyC1RiYzo87mCiACDZNcgFqmUNEZHKfW0kgLxwPgIryRXkYAV5IzAr8pZrBo6QdwW8IhS7gVhO3POSCCRVDDVWEavOivtsdyZmHtORrhoBy6WeGCvu/tBcE+OerF8+u8jv+hBgADHfmSbFytyUAAAAAElFTkSuQmCC) no-repeat 15px center;text-indent: 28px;x:4px;y:4px;background-color:white"})
    question1 = SelectField(u'* 之前有没有自己拆过机或是在他人的协助下拆过机:', choices=[('0', u'请选择'),('1',u'有且是自己一个人'),('2',u'有但是有朋友协助'),('3',u'没有')],)
    question2 = SelectField(u'* 如果我们给你拆的是一台款式老旧、结构古怪的机子你是否有信心和伙伴一起完成？:',
                            choices=[('0', u'请选择'),('1', u'我对这类机子有很多了解'), ('2', u'拆机使我快乐，遇到困难也会想办法克服'), ('3', u'我是拆机萌新，需要小e在旁指导')], )
    question3 = SelectField(u'* 当小e叫你拆如下图所示的这样一台机子时，你会从哪里入手开始拆？',
                            choices=[('0', u'请选择'),('1', u'背面'), ('2', u'键盘一面'), ('3', u'显示屏')], )
    question4 = SelectField(u'* 第一个被我们拆下的是哪部分重要硬件？',
                            choices=[('0', u'请选择'),('1', u'光驱'), ('2', u'电池'), ('3', u'触控板'),('4', u'CPU')], )
    question5 = SelectField(u'* 笔记本电脑的键盘下的控制主板是用什么和显示屏相连的？？',
                            choices=[('0', u'请选择'),('1', u'排线'), ('2', u'转轴'), ('3', u'螺丝')])
    question6 = SelectField(u'* 下列各图中所示的部件是显卡的是？',
                            choices=[('0', u'请选择'), ('1', u'A'), ('2', u'B'),('3', u'C')])
    day242 = BooleanField(u'11.24   13:00-15:00')
    day243 = BooleanField(u'11.24   15:15-17:15')
    day244 = BooleanField(u'11.24   18:30-20:30')
    day251 = BooleanField(u'11.25   9:00-11:00')
    day252 = BooleanField(u'11.25   13:00-15:00')
    day253 = BooleanField(u'11.25   15:15-17:15')
    day254 = BooleanField(u'11.25   18:30-20:30')
    day261 = BooleanField(u'11.26   9:00-11:00')
    day262 = BooleanField(u'11.26   13:00-15:00')
    day263 = BooleanField(u'11.26   15:15-17:15')
    remarks = StringField(u'我们会将参与的同学们分成两人一组，如果你有心仪的小伙伴，请务必在备注里写上他的名字:')
    ver = StringField(u'* 请输入验证码(不区分大小写):', validators=[Required(), length(4, 4, message=u'请正确填写验证码')])
    submit = SubmitField(u'提交')
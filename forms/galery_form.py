# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField


class GaleryForm(FlaskForm):
    img = FileField('Добавить картинку', validators=[FileRequired('Вы не выбрали файл')])
    submit = SubmitField('Отправить')

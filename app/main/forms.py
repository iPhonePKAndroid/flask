from flask import Flask,render_template,redirect,url_for,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


class NameForm(FlaskForm):
	name = StringField('名字：', validators=[DataRequired()])
	submit = SubmitField('提交')
		
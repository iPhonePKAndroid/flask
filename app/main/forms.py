from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
	email = StringField('邮箱', validators=[ DataRequired(), Length(1,64), Email() ])
	password = PasswordField('密码', validators=[ DataRequired() ])
	remember_me = BooleanField('记住登录')
	submit = SubmitField('登录')
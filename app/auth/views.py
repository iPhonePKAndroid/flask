from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from . import auth
from ..models import User
from ..forms import LoginForm

@auth.route('/login')
def login():
	form = LoginForm()
	if form.validate_on_submit():
		pass
	return render_template('auth/login.html')
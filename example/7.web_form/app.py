"""
表单
:author <wenidng> postmaster@g000.cn
"""

from flask import Flask,render_template,redirect,url_for,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'sasa'

class NameForm(FlaskForm):
	name = StringField('名字：', validators=[DataRequired()])
	submit = SubmitField('提交')
		

@app.route('/', methods=['GET','POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		# name = form.name.data
		# form.name.data = ''

		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('您的名称已经更改！')

		session['name'] = form.name.data
		return redirect(url_for('index'))

	return render_template('index.html',form=form,name=session.get('name'))

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
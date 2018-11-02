"""
在视图中操作数据库
:author <wenidng> postmaster@g000.cn
"""

from flask import Flask,render_template,redirect,url_for,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
# 引入SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'sasa'

# 数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] =\
'postgresql://username:@127.0.0.1/dbname'
# 在不需要跟踪对象变化时降低内存消耗
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化模型实例
db = SQLAlchemy(app)

# 集成Python Shell，创建并注册一个shell上下文控制器
@app.shell_context_processor
def make_shell_context():
	return dict(db=db, User=User, Role=Role)

# 定义模型
class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	# 模型关联：lazy='dynamic'禁用自动查询
	users = db.relationship('User', backref='role', lazy='dynamic')

	# Python中这个_repr_函数，对应repr(object)这个函数，返回一个可以用来表示对象的可打印字符串
	def __repr__(self):
		return '<Role %r>' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	# 模型关联
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	# Python中这个_repr_函数，对应repr(object)这个函数，返回一个可以用来表示对象的可打印字符串
	def __repr__(self):
		return '<User %r>' % self.username


class NameForm(FlaskForm):
	name = StringField('名字：', validators=[DataRequired()])
	submit = SubmitField('提交')


@app.route('/', methods=['GET','POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username=form.name.data)
			db.session.add(user)
			db.session.commit()
			session['known'] = False
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('index.html',
		form=form,name=session.get('name'),
		known=session.get('known', False))

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
# 密码散列

# 定义模型
class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	# 一对多模型关联：lazy='dynamic'禁用自动查询，backref='role'也就是user.role，uselist=False为一对一
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
	password_hash = db.Column(db.String(128))

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	# 当设置User().password的时候出发该方法
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	# Python中这个_repr_函数，对应repr(object)这个函数，返回一个可以用来表示对象的可打印字符串
	def __repr__(self):
		return '<User %r>' % self.username
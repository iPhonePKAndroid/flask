"""
数据库ORM
:author <wenidng> postmaster@g000.cn
"""

from flask import Flask,jsonify
# 引入SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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


"""命令行操作

创建所有模型到数据库
db.create_all()
删除所有模型的数据库表
db.drop_all()

创建用户和角色插入数据
admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')

user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=user_role)
user_david = User(username='david', role=user_role)

print(admin_role.id) # None

# 数据库事务
#db.session.add(admin_role)
#db.session.add(mod_role)
#db.session.add(user_role)

db.session.add_all([admin_role, mod_role,user_role,user_john,user_susan,user_david])

# 提交事物
db.session.commit()

# 事物回滚
db.session.rollback()

#关联查询
print(admin_role.id)
# SQL语句
print(admin_role.users)

print(user_john.role)
print(user_john.role.id)
print(user_john.role.name)

# 修改数据
admin_role.name = 'Administrator'
db.session.add(admin_role)
db.session.commit()

# 删除行
db.session.delete(admin_role)
db.session.commit()

# 查询行
Role.query.all()

# 筛选查询
User.query.filter_by(role=user_role).all()
User.query.filter_by(role=user_role).first()

# 获得SQL语句
str(User.query.filter_by(role=user_role))

# 查询过滤器
filter() 把过滤器加到原查询上，返回一个新的查询
filter_by() 把等值的过滤器添加在原查询上，返回一个新的查询
limit() 数量
offset() 便宜查询结果
order_by() 按照条件排序
group_by() 按照条件分组

# 查询执行方法
all()
first()
first_or_404()
get()
get_or_404()
count()
paginate()

"""


@app.route('/')
def index():
	return jsonify('ok')

@app.route('/test/')
def test():
	return __name__

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
"""
模板
:author <wenidng> postmaster@g000.cn
"""


from flask import Flask,render_template,abort
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

"""
jinja2变量过滤器
safe 不转义
capitalize 首字母大写
lower 子母转小写
upper 子母转大写
title 每个单词首字母大写
trim 去除首尾空格
striptags 把所有html标签删除
"""

class ClassName():
	def test():
		return 'demo ok'
		
# 首页
@app.route('/', methods=['GET'])
def index():
	name='名称'
	clas = ClassName
	lists = ['1',2,True,['5']]
	dicts = {'key':'val','foo':'bar'}
	return render_template('index.html',name=name,dicts=dicts,lists=lists,clas=clas)

# 模板
@app.route('/template')
def template():
	return render_template('pro/index.html')

# Bootstrap
@app.route('/bootstrap')
def bootstrap():
	return render_template('bootstrap/index.html', name='问鼎',current_time=datetime.utcnow())

# 自定义错误页
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

@app.route('/500')
def error():
	abort(500)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
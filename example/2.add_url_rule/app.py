"""
添加到路由app.add_url_rule()函数的使用
:author <wenidng> postmaster@g000.cn
"""

from flask import Flask

app = Flask(__name__)

# 定义视图函数
def index():
	return 'hello wolrd'

# URL、端点名、视图函数
app.add_url_rule('/','index',index)

# 启动
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
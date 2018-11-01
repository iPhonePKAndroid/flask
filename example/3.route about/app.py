"""
路由匹配和格式化字符串
:author <wenidng> postmaster@g000.cn
"""


from flask import Flask

app = Flask(__name__)


@app.route('/id/<user_id>')
def userid(user_id):
	return '您的用户ID：{}'.format(user_id)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
"""
响应
:author <wenidng> postmaster@g000.cn
"""


from flask import Flask,make_response,redirect,abort

app = Flask(__name__)


"""
响应对象
status_code
headers
set_cookie()
delete_cookie()
content_length
content_type
set_data() 使用字符串或字节值设定响应
get_date() 获得响应主体
"""


# 设置响应状态码
@app.route('/')
def index():
	return '请求无效', 400

# 设置响应
@app.route('/make_response')
def response():
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('carries', '42')
	return response

# 跳转
@app.route('/redirect')
def go():
	return redirect('https://www.fakajun.com/')

# 抛出异常
@app.route('/post/<id>')
def get_post(id):
	if not id:
		abort(404)
	return '文章ID：{}'.format(id)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
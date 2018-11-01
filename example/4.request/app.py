"""
请求
:author <wenidng> postmaster@g000.cn
"""


from flask import Flask
from flask import request


app = Flask(__name__)


"""
请求对象的属性和方法
form 表单字段
args 通过URL传递的参数
values form和args的合集
cookies
headers
files
get_data() 请求缓冲的数据
get_json() 返回一个python字典，包含解析请求主体后得到的json
blueprint 处理请求蓝本的名称
endpoint 处理请求flask端点的名称，flask把视图函数的名称作为路由端点的名称
method
scheme http或https
is_secure() 通过安全的连接（https），发送请求时返回True
host 主机名或带端口号
path url的路径部分
query_string 查询字符串，默认返回原始二进制
full_path url的路径和查询字符串
url 完整url
base_url 没有查询字符串的url
remote_addr 客户端IP地址
environ 请求原始的WSGI环境字典

请求钩子：在请求开始之前可能需要创建数据库或者验证发起用户身份，为了避免在每个视图中重复编写提供的通用函数
before_request 每次请求之前运行
before_first_request 只处理第一个请求之前运行，可以通过它添加服务器初始化任务
after_request 如果没有抛出异常则在每次请求之后运行
teardown_request 即使有未处理的异常也在每次请求之后运行
"""

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	res = '''
	<pre>
	浏览器设备信息：{agent}
	其他暂无
	<pre>
	'''
	return res.format(agent=user_agent)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
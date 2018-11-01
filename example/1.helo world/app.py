"""
初始化定义路由简单实例
:author <wenidng> postmaster@g000.cn
"""


# 导入包	
from flask import Flask

# 初始化
app = Flask(__name__)

# 定义路由
@app.route('/', methods=['GET','POST'])
def index():
	return 'hello world'

# 启动
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
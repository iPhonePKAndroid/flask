## Flask最佳实践




#### 命令行

```sh

export FLASK_APP=server.py
export FLASK_DEBUG=1

export SECRET_KEY=keyasd
export MAIL_SERVER=smtp.qq.com
export MAIL_PORT=465
export MAIL_USE_TLS=true
export MAIL_USERNAME=71314126@qq.com
export MAIL_PASSWORD=sdadsd
export FLASK_ADMIN=postmaster@g000.cn

flask run
flask shell



```


***虚拟环境***

```sh
source venv/bin/activate
pip freeze

```



### 数据库迁移
```sh
export FLASK_APP=server.py

# 添加数据库迁移支持
flask db init

# 生成数据库迁移文件
flask db migrate -m 'initial migrate'

# 更新迁移
flask db upgrade
***如果不能更新迁移，则删除数据库已建立的表或者flask db stamp***

# 还原迁移
flask db downgrade

```






#### 关于我们

* 微信iPhonePKAndroid
* [https://www.g000.cn](https://www.g000.cn)
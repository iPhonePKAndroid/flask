## 说明

```sh
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
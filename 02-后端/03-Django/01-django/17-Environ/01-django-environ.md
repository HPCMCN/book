# Django-environ

使用linux环境变量来达到环境分离, 读取顺序:

​	linux > file

## 安装

```shell
pip install django-environ
```



## 使用

```python
import environ

env = environ.Env()
env.read_env(".env")  # 读取指定位置的变量
env("SECRET_KEY", default="xxx") # str
env.db("DATABASE_URL") # 以url形式配置数据库
env.dict("DATABASE_TEST", {}) # dict
env.list() # list
env.int() # int
env.email("EMAILS") # 以url形式配置email参数, 内部类似db
```

## 配置文件

```shell
# --- django --------------------------------------------------
DEBUG=true
SECRET_KEY='v***i'
MESSAGE_ASYNC_COUNT=10


# --- mysql ----------------------------------------------
# 注意?号后面的将会被配置在options内, email也是一样
# {'default': {'NAME': 'cmdb1', 'USER': 'root', 'PASSWORD': 'd***0', 'HOST': '127.0.0.1', 'PORT': 3306, 'OPTIONS': {'init_command': 'SET foreign_key_checks=0;', 'charset': 'utf8'}, 'TEST': {'CHARSET': 'utf8', 'COLLATION': 'utf8_general_ci'}}}
DATABASE_URL='mysql://root:d***0@127.0.0.1:3306/cmdb?init_command=SET foreign_key_checks=0%3B;&charset=utf8'
DATABASE_TEST='CHARSET=utf8;COLLATION=utf8_general_ci;'

# --- mail ----------------------------------------------
EMAILS="smtp+tls://username:password@邮件服务器域名:25/?from=邮箱&name=运维平台-CMDB"
```


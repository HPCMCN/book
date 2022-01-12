
## 1.1 ORM框架

Object Relation Mapping(ORM), 数据库对象关系映射

将数据库中的表, 字段等转化成Python的对象, 直接通过对象去操作数据库. 

* 屏蔽了不同数据库的sql语言的差异
* 牺牲了Python对象向数据库转化时间, 和sql语句转化时间

## 1.2 安装mysql驱动

```python
pip install pymysql
```

## 1.3 配置

### 1.3.1 驱动

```python
import pymysql

pymysql.version_info = (1, 4, 13, "final", 0)  # 强制指定客户端版本
pymysql.install_as_MySQLdb()
```

### 1.3.2 数据库

修改`setting.py`中`DATABASES`参数

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "localhost",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": "dong10",
        "NAME": "cmdb1",
        "TEST": {
            "CHARSET": "utf8",
            "COLLATION": "utf8_general_ci",
        },
        "OPTIONS": {
            "charset": "utf8",
            "init_command": "SET foreign_key_checks=0;"  # 不进行外键检查, 不然test时可能会报错, 一定要加分号
            "isolation_level": None
        }
    }
}


TIME_ZONE = "Asia/Shanghai"  # 采用本地时区, 可以直接用datetime库
USE_TZ = False
```


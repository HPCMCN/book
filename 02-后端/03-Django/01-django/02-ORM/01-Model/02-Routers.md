# 1. 数据库读写分离

为了提高数据库的读写效率, 对分布式数据库高效的利用, 可以进行读写分离

## 1.1 setting配置

```python
# 数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'meiduo'  # 数据库名字
    },
    'slave': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 8306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'meiduo'  # 数据库名字
    }
}
```

## 1.2 实现

### 1.2.1 自动操作

#### 分发规则

```python
class MaterSlaveRouter(object):
    """数据库主从读写分离"""

    def db_for_read(self, model, **hints):
        """读取数据库"""
        # 也可以多个数据库随机性读取
        return "slave"

    def db_for_write(self, model, **hints):
        """写入数据库"""
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return True
```

#### 引用

```python
# settings
DATABASE_ROUTERS = ["utils.routers.MaterSlaveRouter"]
```

### 1.2.2 手动操作

只需要在orm编写是指定对应的数据库即可

```python
Users.objects.using("slave").create(xxx)
Users.objects.filter(xx).using("default").first()
```

# 2. 示例

```python
# noinspection PyProtectedMember,PyMethodMayBeStatic
class MysqlRouter(object):
    """mysql routers"""
    read_only_databases = ("auths",)
    read_only_tables = ("users", "third_auth", "third_tokens")

    def db_for_read(self, model, **hints):
        logging.info(model._meta.db_table)
        if model._meta.db_table in self.read_only_tables:
            logging.info(f"use database auths: {model._meta.db_table}")
            return "auths"
        return "default"

    def db_for_write(self, model, **hints):
        logging.info(f"{model}, {hints}")
        if model._meta.db_table in self.read_only_tables:
            raise OSError(f"Table {model._meta.db_table} can't write data!")
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, *args, **hints):
        if db in self.read_only_databases or \
                hints.get("model") and hints["model"]._meta.db_table in self.read_only_tables:
            logging.info(f"Skip migrate: database={db} {hints.get('model') and hints['model']._meta.db_table}")
            return False
        return True
```


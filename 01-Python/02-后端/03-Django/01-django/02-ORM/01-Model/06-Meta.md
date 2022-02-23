#### abstract

是否为抽象类, 不会对应数据库中的表, 一般用于继承, 默认False

#### managed

是否通过迁移命令管理数据库, 默认True, False表示`makemigrations`, `migrate`等迁移命令将不会对此模型进行操作

#### app_label

如果一个model定义在默认的models.py，例如如果你的app的models在myapp.models子模块下，你必须定义app_label让Django知道它属于哪一个app, `app_label = 'myapp'`

#### db_table

定义数据库 表名字

#### db_tablespace

定义数据库 表空间

#### ordering

#### order_with_respect_to

#### verbose_name

#### verbose_name_plural

#### index_together

#### proxy

#### permissions

#### get_latest_by
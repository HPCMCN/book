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

## 1.3 示例

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

# 2. 跨库外键处理

django是不支持跨库外键查询的, 查询时的策略: 

* 一条查询中不得跨越两个数据库, 
* 但是使用.的形式是可以获取两个数据库的数据的, 比如`asset.user.id`, 但是不能使用`Asset.objects.filter(user__id=1).all()`, 同样`django_filters`也是依赖于此操作, 一旦调用就会报错字段不存在

处理方案:

```python
# noinspection PyUnresolvedReferences
class QueryMixin(object):
    """
    queryset = self.objects.filter(name="xxx")
        添加对 queryset.update(xxx)/delete(xxx) 支持
    """

    def get_queryset(self):
        return QuerySet(self.model).exclude(is_deleted=True)


# noinspection PyUnresolvedReferences
class SignDeleteMixin(object):
    def delete(self, *args, soft=True, **kwargs):
        if soft:
            return self.update(is_deleted=True, deleted_at=datetime.now(), deleted_by=get_current_authenticated_user())
        return super(SignDeleteMixin, self).delete(*args, **kwargs)


class QuerySet(QueryMixin, SignDeleteMixin, QuerySetBase):
    """增加软删除"""
    pass


# noinspection PyProtectedMember
class FilterQuerySet(QuerySet):

    def filter(self, *args, **kwargs):
        """检测是否跨库查询"""
        replace_fields = {}
        for field, value in kwargs.items():
            if not value or "__" not in field:
                continue
            st = time.time()
            try:
                fields = field.split("__")
                model = self.model._meta.concrete_model
                model_field_mappings = []
                suffix = ""
                for i, f in enumerate(fields):
                    # print(f)
                    relate_field = model._meta.get_field(f)
                    model_field_mappings.append((model, relate_field))
                    if not relate_field.related_model:
                        suffix = "__".join(fields[i + 1:]) or "exact"
                        break
                    model = relate_field.related_model._meta.concrete_model
                dbs = {m[0]._meta.db_table in MysqlRouter.read_only_tables for m in model_field_mappings}
                if len(dbs) == 1:
                    # 同库操作, 无需切分查询
                    continue
                s = True
                last = len(model_field_mappings)
                for i, (m, relate_field) in enumerate(model_field_mappings[::-1]):
                    tb_name = m._meta.db_table
                    db_name = "auths" if m._meta.db_table in MysqlRouter.read_only_tables else "default"
                    if isinstance(value, QuerySetBase):
                        value = [getattr(x, relate_field.target_field.name) for x in value]
                    if last - 1 == i:
                        in_filed = f"{relate_field.name}__in"
                        if in_filed in replace_fields:
                            replace_fields[in_filed]["fields"].add(field)
                            replace_fields[in_filed]["value"] = value
                        else:
                            replace_fields[in_filed] = {"fields": {field}, "value": value}
                        break
                    if s:
                        # print(m, db_name, {relate_field.name: value})
                        value = m._default_manager.using(db_name).filter(
                            **{f"{relate_field.name}__{suffix}": value})
                        s = False
                    else:
                        # print(m, db_name, {f"{relate_field.name}__in": value})
                        value = m._default_manager.using(db_name).filter(**{f"{relate_field.name}__in": value})
            except FieldDoesNotExist:
                pass
            logging.info(f"{field} 跨库filter请求耗时: {time.time() - st}")
        for k, v in replace_fields.items():
            for f in v["fields"]:
                if f in kwargs:
                    kwargs.pop(f)
            kwargs[k] = v["value"]
        st = time.time()
        res = super().filter(*args, **kwargs)
        logging.info(f"原始filter策略请求耗时: {time.time() - st}")
        return res


class FilterManager(manager.BaseManager.from_queryset(FilterQuerySet)):
    """针对跨库查询"""
    pass


class Asset(Model):
    objects = FilterManager()
```




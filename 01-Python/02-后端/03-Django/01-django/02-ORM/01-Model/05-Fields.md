# 2. 字段

## 2.1 类型字段

`id`字段默认会自动创建, 无需进行再次创建, 创建后可以用`id`或者`pk`字段都可以查询到

| 字段             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| AutoField        | 自动增长                                                     |
| BooleanField     | 布尔类型                                                     |
| NullBooleanField | 支持Null, True, False三种                                    |
| CharField        | 字符串  max_length限时长度                                   |
| TextField        | 大文本(一般超过4000字符)                                     |
| IntegerField     | 整形                                                         |
| DecimalField     | 十进制浮点型,  参数max_digits为总位数，参数decimal_places为小数位数 |
| FloatField       | 浮点数                                                       |
| DateField        | 日期, 参数: auto_now(每次保存时自动记录时间), auto_now_add(创建时自动保存)  两个参数相互排斥, 只能二选一 |
| TimeField        | 时间, 参数同上                                               |
| DateTimeField    | 日期时间, 参数同上                                           |
| FileField        | 上传文件字段                                                 |
| ImageField       | 继承FileField, 对上传内容进行校验                            |

## 2.2 字段限制

| 参数           | 说明                                                   |
| -------------- | ------------------------------------------------------ |
| null           | 默认False(非空), 字段可以设置null                      |
| blank          | 默认False(非空白), 字段设置什么都行, 但是必须需要设置. |
| db_column/name | 数据库中字段名称, 如果不指定使用属性名                 |
| db_index       | 是否为字段创建索引, 默认False                          |
| default        | 默认值                                                 |
| primary_key    | 主键, 默认False                                        |
| unique         | 唯一, 默认False                                        |

## 2.3 外键限制

外键默认使用的字段是`on_delete`

| 参数        | 说明                                      |
| ----------- | ----------------------------------------- |
| CASCADE     | 删除主表关联删除约束表                    |
| PROTECT     | 抛出异常禁止删除                          |
| SET_NULL    | 将约束表中约束字段改为null(需要null_True) |
| SET_DEFAULT | 将约束表中约束字段改为默认(需要有默认值)  |
| SET()       | 删除主表并给约束表中约束字段指定值        |
| DO_NOTHING  | 不做任何操作, 抛出异常                    |

**实例**

```python
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class MyModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
```

## 2.4 HelloWorld

```python
from django.db import models
class Book(models.Model):
    # Django中不用设置主键, 自动生成主键id, 可以使用id/pk(primary key)查询
    b_title = models.CharField(max_length=20, verbose_name="书名")
    class Meta:
        # Django中如果不设置表名, 默认以app名字_小写模型类作为名字
        db_table = "tb_books"              # 表名
        verbose_name = "图书"              # 自定义字段名字
        verbose_name_plural = verbose_name # 开启自定义字段
        def __str__(self):
            return self.b_title  # 让输出是书名  这里不能使用repr
```


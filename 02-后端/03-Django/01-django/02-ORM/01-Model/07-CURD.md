# 3. 操作

## 3.1 增删改

### 3.1 增加

* 单个

  ```python
  t = Table.objects.create()
  t = Table()
  t.save()
  ```

* 批量

  ```python
  t_list = []
  for _ in range(10):
      t = Table()
      t_list.append(t)
  Table.objects.bulk_create(t_list)
  ```


### 3.1.2 删除

* 单个删除

  ```python
  t = Table.objects.get()
  t.delete()
  ```

* 批量删除

  ```python
  Table.objects.all().delete()
  Table.objects.filter().delete()
  ```

### 3.1.3 修改

* 单个

  ```python
  t = Table.objects.get()
  t.name = xx
  t.save()
  
  t = Table.objects.all().first()
  t.name = xx
  t.save()
  ```

  

* 批量

  ```python
  Table.objects.filter().update(name=xxx)
  ```

  

## 3.2 查询

ORM查询存在惰性

实例

```python
tables = Table.objects.all()   # 未访问数据库
print(tables)  # 获取到的是查询语句
[table for talbe in tables]  # 获取orm查询集对象
```

### 3.4.1 查询方法

#### F/Q

* F对象

  表中字段运算后, 与其他字段进行对比

  ```python
  Table.objects.filter(num1__gt=F(num2) * 2)
  # where num1 > num2 * 2
  ```

* Q对象

  或且非操作(&|~)

  ```python
  Table.objects.filter(Q(num1__gt=20) | Q(num2__gt=5))
  # where num1 > 20 or num2 > 5
  
  Table.objects.filter(~Q(id=3))
  # where id!=3
  ```

  

#### 查询

| 方法     | 返回      | 说明                                                         |
| -------- | --------- | ------------------------------------------------------------ |
| get      | any       | 主键查询. 主键为id/pk                                        |
| all      | list(any) | 返回一个查询集, 转化后为list, 全部查询, 默认限制查询21个, 即limit=21 |
| filter   | list(any) | 返回一个查询集, 转化后为list , 过滤查询                      |
| order_by | list(any) | 返回一个查询集, 转化后为list, 排序查询                       |
| exclude  | list(any) | 返回一个查询集, 转化后为list, 取反查询                       |
| exists   | bool      | 判断查询集是否存在数据                                       |

#### 聚合

聚合函数调用需要使用`appregate`方法

| 方法 | 返回 | 说明   |
| ---- | ---- | ------ |
| Avg  | dict | 平均数 |
| Max  | dict | 最大数 |
| Min  | dict | 最小数 |
| Sum  | dict | 求和   |

**实例**

```python
from django.db.models import Sum
Table.objects.aggregate(Sum("t_num"))

# 返回
# {"t_num__sum": 3}
```

#### 关联查询

filter(对方类名__对方属性\_\_条件=xxx)

filter(约束字段__对方属性\_\_条件=xxx)

```python
Table.objects.filter(tb_table1__name__contains="test")
```

### 3.4.2 查询过滤

| 方法                                                     | 作用                                                     | 实例                                                         |
| -------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------ |
| exact/iexact                                             | 等于, 等价于使用`=`号<br>增加符号`i`表示不区分大小写匹配 | id_exact=1<br>id=1                                           |
| contains/icontains                                       | 包含某个字<br/>增加符号`i`表示不区分大小写匹配           | name__contains="name"                                        |
| startswith/endswith<br>istartswith/iendswith             | 以某个字开头/结尾<br/>增加符号`i`表示不区分大小写匹配    | name__startswith="n"                                         |
| in                                                       | 范围查询                                                 | id__in=[1, 3, 4, 5]                                          |
| gt/gte                                                   | 大于/大于等于                                            | id__gte=8                                                    |
| lt/lte                                                   | 小于/小于等于                                            | id__lte=8                                                    |
| isnull                                                   | 判断是否为空                                             | name__isnull=False                                           |
| datetime/date/year/month/day/week_day/hour/minute/second | 时间操作                                                 | login_year=1980  等于1980年<br>login_gte=date(1980, 2, 2)  大于1980年 |



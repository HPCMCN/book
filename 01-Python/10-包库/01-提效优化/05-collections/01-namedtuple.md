# namedtuple

元组的子类

**特点**

* 可以像普通对象调用一样来处理类似字典功能的容器
* 占用内存少

<hr>
```Python
def namedtuple(typename, field_names, rename=False, defaults=None, module=None)
	return namedtuple
```

* typename: str, 对namedtuple进行命名
* field_names: str/iterable, nametuple可以使用的属性. str需要用`, `或者空格分开
* rename: bool, 如果`filed_names`与系统关键字, 或者出现重复, 是否进行重命名处理, False表示直接抛出异常. True表示利用索引进行重命名`_1`, `_2`...
* defaults: iterable, 对`filed_names`设置缺省值. 可以是list, tuple, dict.
* module: str, 设置`__module__`属性

# 1. 存储

## 1.1 设值

### 1.1.1 初始化

* 位置参数设置

  ```python
  Test = namedtuple("Test", "a b c")
  nt = Test(1, 2, 3)
  ```


* 关键字参数设置

  ```python
  Test = namedtuple("Test", "a,b,c", defaults={"a": 1, "b": 2, "c": 3})
  ```

* 设置`__doc__`属性

  ```Python
  from collections import *
  
  Test = namedtuple("Test", ["x", "y", "z"], defaults=[1, 2])
  Test.x.__doc__ = "x description"
  help(Test.x)
  ```

  输出

  ```python
  Help on property:
  
      x description
  ```

### 1.1.2 \_make

类方法, 将可迭代对象强转为`namedtuple`中的value

```Python
@classmethod
def _make(cls, iterable):
    return namedtuple
```

* iterable: 可迭代对象

**示例**

   ```python
Test = namedtuple("Test", ["x", "y", "z"], defaults=[1, 2])
t = Test(5)
print(t)
a = [7, 8, 9]
print(t._make(a))
   ```

**输出**

```bash
Test(x=5, y=1, z=2)
Test(x=7, y=8, z=9)
```

## 1.1 取值

* getattr: `getattr(t, "x", 1)`

* 切片索引取值: `t[1]`

* 像调用属性一样处理字典

  ```python
  Test = namedtuple("Test", "a,b,c")
  nt = Test(1, 2, 3)
  print(nt.a, nt.b, nt.c)
  ```

  输出

  ```bash
  1 2 3
  ```

## 1.3 自省

### 1.3.1 \_fields

输出`namedtuple`配置的属性

* 示例

  ```python
  from collections import *
  
  Test = namedtuple("Test", ["x", "y", "z"], defaults=[1, 2])
  t = Test(5)
  print(t._fields)
  ```

* 输出

  ```bash
  ('x', 'y', 'z')
  ```

### 1.3.2 _field_defaults

输出`namedtuple`的缺省键值对, 以`dict`表示

* 示例

  ```python
  Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
  print(Account._field_defaults)
  ```

* 输出

  ```bash
  {'balance': 0}
  ```

## 1.4 修改

### 1.4.1 \_replace()

修改并生成一个新的`namedtuple`

```Python
def _replace(**kwargs):
```

* kwargs: 所要修改的值, 以关键字参数传入

**示例**

```python
Test = namedtuple("Test", ["x", "y", "z"], defaults=[1, 2])
t = Test(5)
print(t)
a = {"x": 5, "y": 7}
print(t._replace(**a))
```

**输出**

```bash
Test(x=5, y=1, z=2)
Test(x=5, y=7, z=2)
```

# 2. 类型转换

## 2.1 字典

### 2.1.1 \_asdict

* < Python3.8: 将`namedtuple`转化为`OrderedDict`, 即有序字典
* \>=Python3.8: 返回`dict`

```Python
@classmethod
def _asdict(cls, iterable):
    return OrderedDict/Dict
```

**示例**

```Python
from collections import *

Test = namedtuple("Test", ["x", "y", "z"], defaults=[1, 2])
t = Test(5)
print(t)
print(t._asdict())
```

**输出**

```bash
Test(x=5, y=1, z=2)
OrderedDict([('x', 5), ('y', 1), ('z', 2)])
```

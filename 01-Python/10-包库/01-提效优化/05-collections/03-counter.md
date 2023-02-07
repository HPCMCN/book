# Counter

`dict`的子类, 用于数据的统计.

```python
def __init__([iterable or mapping]):
    return Counter
```

**注意**:

* Counter没有实现字典的`fromkey`函数.

# 1. 更新数据

## 1.1 增加

### 1.1.1 update

增加需要统计的数据

```python
def update(self, __m, **kwargs)
	return None
```

* \_\_m: mapping/iterable, 需要新增统计的数据, 如果为mapping, 则是增加. 不会直接使用mapping中的值
* \*\*kwargs:  类似dict传值.

示例

```Python
from collections import *

c_a = ["a", "b", "c"]
c_b = "abcesoiamo"
c_d = {"a": 3, "c": 2}
c = Counter(c_a)
c.update(c_d)
c.update(c_b, b=5)
print(c)
```

输出

```bash
Counter({'b': 7, 'a': 6, 'c': 4, 'o': 2, 'e': 1, 's': 1, 'i': 1, 'm': 1})
```

## 1.2 减少

### 1.2.1 subtract

与`update`相反的操作. 减去元素

```python
@overload
def subtract(self, __mapping:)
```

* \_\_mapping: mapping/iterable, 需要减去的次数. 或者元素

实例

```Python
from collections import *

c_b = "abracadabra"
c = Counter(c_b)
c.subtract("abc")
print(c)
```

输出

```Python
Counter({'a': 4, 'r': 2, 'b': 1, 'd': 1, 'c': 0})
```

# 2. 排序获取

## 2.1 获取keys

### 2.1.1 elements

按照顺序将`key`(重复的将在一起)依次排列出来

```Python
def elements(self):
    return iterable
```

实例

```Python
from collections import *

c_b = "abcesoiamo"
c = Counter(c_b)
print(list(c.elements()))
```

输出

```Python
['a', 'a', 'b', 'c', 'e', 's', 'o', 'o', 'i', 'm']
```

## 2.2 获取最大的几个

### 2.2.1 most_common

从高到低截取最大的`n`个key/value. 相同时会按照加入的顺序排序.

```Python
def most_common(self, n):
    return [(k1, v1)...]
```

实例

```python
from collections import *

c_b = "abracadabra"
c = Counter(c_b)
print(list(c.most_common(3)))
```

输出

```python
[('a', 5), ('b', 2), ('r', 2)]
```


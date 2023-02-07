# 1. OrderedDict

有序字典, `dict`的子类. 由于Python3.7以上版本, `dict`做了变动, 支持了排序功能

```Python
def __init__([items]):
    return OrderedDict
```

* 传入参数与`dict`相同

| 功能                         | `dict`              | `OrderedDict`                  |
| ---------------------------- | ------------------- | ------------------------------ |
| 排序算法                     | 支持, 但不擅长      | 擅长                           |
| 映射/存储/迭代/空间效率/更新 | 擅长                | 支持, 但不擅长                 |
| 等号校验数据是否相等         | 只比较数据          | 比较数据和顺序                 |
| `popitem()`                  | `FIFO`弹出末尾元素  | 可以指定`FIFO`开始或者末尾弹栈 |
| `move_to_end()`              | 不支持              | 将指定元素移动到末尾           |
| `__reversed__()`             | Python3.8之前不支持 | 支持翻转字典                   |

示例一:

```Python
# 实现url_cache功能
from collections import OrderedDict

class LruCache(OrderedDict):
    """缓存"""

    def __init__(self, max_size=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_size = max_size

    def __setitem__(self, key, value):
        if len(self) >= self.max_size:
            first = next(iter(self))
            del self[first]
        super().__setitem__(key, value)

    def __getitem__(self, item):
        value = super().__getitem__(item)
        self.move_to_end(item)
        return value

    def __call__(self, size=100):
        self.max_size = size
        def func(fun):
            def wrapper(*args, **kwargs):
                if args in self:
                    res = self[args]
                else:
                    res = fun(*args, **kwargs)
                    self[args] = res
                return res
            return wrapper
        return func

uc = LruCache()

@uc(size=100)
def fib(x):
    print(x)
    if x < 2:
        return 1
    return fib(x - 1) + fib(x - 2)

print(fib(20))
print(fib(30))
print(fib(20))
```

支持`dict`中的全部功能, 并拓展了部分功能

## 1.1 删除

### 1.1.1 popitem

依照`FIFO`, 指定左边或者右边弹栈

```Python
def popitem(self, last=True):
    return (key, value)
```

* last: bool.  True表示右边出栈

实例

```Python
from collections import *

od = OrderedDict(x=2, y=3, z=4)
print(od.popitem(False))
print(od.popitem(True))
```

输出

```Python
('x', 2)
('z', 4)
```

## 1.2 移动

### 1.2.1 move_to_end

将某个键值移动到末尾

```python
def move_to_end(self, key, last)
```

* key: key, 指定需要移动的键

实例

```Python
od = OrderedDict(x=2, y=3, z=4)
od.move_to_end("y", last=True)
print(od)
```

输出

```python
OrderedDict([('x', 2), ('z', 4), ('y', 3)])
```

## 1.3 翻转

### 1.3.1 reversed

利用`__reversed__()`翻转字典, 返回值为`iter`

实例

```Python
from collections import *

od = OrderedDict(x=2, y=3, z=4)
print(list(reversed(od)))
```

输出

```bash
['z', 'y', 'x']
```

# 2. defaultdict

继承于`dict`, 增加了字典的缺省值功能

```Python
def __init__([default_factory=None], **kwargs)
	return defaultdict
```

* default_factory: 可调用的函数/对象/None, 第一个参数为缺省值
* **kwargs: 其他参数, 用于构建字典的key/value对

## 2.1 缺省值

### 2.1.1 \__missing__

自动赋予缺省值. 只能用切片, 不能用`.get()`, 否则不能获取到缺省值

```Python
def __missing__(self, key):
    self[key] = default_factory()
```

* key: key, 需要赋予缺省值的可以

示例

```python
class DD(defaultdict):

    def __missing__(self, key):
        value = self.default_factory()
        print("当前key值: ", key)
        self[key] = value
        return value

d = DD(int)
print("切片正常获取到缺省值: ", d[1])
print("get不能获取到缺省值: ", d.get(2))
```

输出

```bash
当前key值:  1
切片正常获取到缺省值:  0
get不能获取到缺省值:  None
```

### 2.1.2 default_factory

存储用来提供缺省值的函数

* 示例

  ```python
  def test1():
      return 2
  
  dd = defaultdict(test1)
  print(dd.default_factory.__name__, dd.default_factory)
  ```

  

* 输出

  ```bash
  test1 <function test1 at 0x000001FEBC66D378>
  ```

## 2.2 示例

* 统计

  ```python
  dd = defaultdict(int)
  count_str = "ashomoasoiuhoie"
  
  for s in count_str:
      dd[s] += 1
  
  print(dd)
  ```

  输出

  ```bash
  defaultdict(<class 'int'>, {'a': 2, 's': 2, 'h': 2, 'o': 4, 'm': 1, 'i': 2, 'u': 1, 'e': 1})
  ```

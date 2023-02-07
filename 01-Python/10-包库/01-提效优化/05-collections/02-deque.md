## deque

双端队列,  是通过`queue`队列实现的. 支持线程安全.

```Python
def __init__(self, iterable=None, maxlen=None)
	return queue
```

* iterable: 需要转换为双端队列的可迭代对象

* maxlen: int/None, 限制队列的长度, 超过长度时, 再次添加会从队列的另一端弹出一个. 可以利用这个特性实现`tail`功能

示例一

  ```Python
# 查看后几行: tail -n 10 xx.txt
from collections import *

def tail(filename, n=5):
    with open(filename, "r", encoding="utf-8") as f:
        print("".join(deque(f, n)))

tail(r"E:\project\test\t_ftp\t_ftp.py", 10)
  ```

  示例二

```Python
# 轮询遍历
abc, d, ef  --> a d e b f c

def roundrobin(*iterable):
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n

print(list(roundrobin(["abc", "d", "ef"])))
```



支持的列表方法如下:

* `len()`
* `reversed(d)`
* `copy.copy(d)`
* `copy.deepcopy(d)`
* `x in d`
* `d1 + d2`
* `for x in d`
* 切片
* `d1 * 2`

**注**: 由于此节的方法全部为重复方法, 暂时不举例说明

# 1. CURD

## 1.1 增加

### 1.1.1 append

从右侧添加元素

```Python
def append(self, x)
return None
```

### 1.1.2 appendleft

从左侧添加元素

```Python
def appendleft(self, x)
return None
```

### 1.1.3 extend

从右侧批量添加元素

```Python
def extend(self, iterable):
    return None
```

### 1.1.4 extendleft

从右侧批量添加元素

```Python
def extendleft(self, iterable):
    return None
```

## 1.2 删除

### 1.2.1 clear

清空元素

```Python
def clear(self)
	return None
```

### 1.2.2 pop

删除最右侧的元素, 并返回

```python
def pop(self):
    return obj/IndexError
```

### 1.2.3 popleft

删除最左侧的元素, 并返回

```Python
def popleft(self):
    return obj/IndexError
```

## 1.3 查找

### 1.3.1 index

找出某个元素在队列的位置. 

```Python
def index(self, x, start, stop):
    return int/ValueError
```

* x: obj, 需要查找的元素
* start: int, 查找的起始位置
* stop: int, 查找的终止位置

# 2. 队列操作

## 2.1 移动

### 2.1.1 rotate

队列向右移动.  等价于: 循环删除右边的元素, 并添加到左边.   负数反过来. 

```Python
def rotate(self, n=1):
    return None
```

* n: int, 需要移动几个元素. 

示例

```Python
from collections import *

d = deque([1, 2])
d.rotate(3)  # 队列整体移动3次
print(d)
```

输出

```Python
deque([2, 1])
```

### 2.1.2 reverse

翻转队列

```Python
def reverse(self):
    return None
```

## 2.2 统计

### 2.2.1 count

统计某个元素的个数

```Python
def count(self, x):
    return int
```

### 2.2.2 maxlen

获取队列的上限.  如果没有限制, 则为`None`

## 2.3 队列复制

### 2.3.1 copy

浅copy

```Python
def copy(self):
    return deque
```

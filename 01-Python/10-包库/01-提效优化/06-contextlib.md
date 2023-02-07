# 1. 转换为上下文对象

## 1.1 类

### 1.1.1 ContextDecorator

转换类

```python
from contextlib import ContextDecorator

class Demo(ContextDecorator):
    def __enter__(self):
        print("上文")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("下文")
        return None

@Demo()
def demo():
    print("正文")

demo()
# 输出:
上文
正文
下文
```

## 1.2 生成器

### 1.2.1 contextmanager

转换生成器

```python
class Demo:
    def pt(self):
        print("正文")

# 开启上下文
@contextlib.contextmanager
def demo():
    print("上文")
    try:
        yield Demo()
    finally:
        print("下文")

with demo() as f:
    f.pt()
```

输出

```shell
上文
正文
下文
```

# 2. 下文处理

## 2.1 关闭操作

### 2.1.1 closing

自动关闭下文操作

```python
class Demo:
    def __init__(self):
        self._is_close = False

    def close(self):
        if self._is_close is True:
            raise OSError("Demo is closed!")
        self._is_close = True

    def pt(self):
        print("do something", self._is_close)

# 自动关闭
with contextlib.closing(Demo()) as f:
    f.pt()
f.pt()  # 抛出异常!
```

## 2.2 异常拦击

### 2.2.1 suppress

屏蔽特定异常, 让特定异常不抛出

```python
import os

# 关闭指定异常
with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')
    raise FileNotFoundError("xxx")

with contextlib.suppress(FileNotFoundError):
    os.remove('someotherfile.tmp')
```

## 2.3 修改标准输入输出

### 2.3.1  redirect_stdout

在上下文中托管标准输出

```python
from io import StringIO
f = StringIO()
with contextlib.redirect_stdout(f):
    help(pow)
s = f.getvalue()
print(s)
f.close()

import sys
with contextlib.redirect_stdout(sys.stderr):
    # 重定向到标准错误里, 直接打印出来
    help(pow)
```

### 2.3.2 redirect_stderr

在上下文中托管标准输出

```python
f = open("111.txt", "wb")
with contextlib.redirect_stderr(f):
    raise Exception("aaaa")
f.close()
with open("111.txt", "rb") as f:
    print(f.read())
```


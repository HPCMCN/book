# functools

本模块主要用于: 

* 函数 参数/功能 拓展
* 函数 执行缓存
* 数学运算功能补全



# 模块报错处理

## 1. 版本报错

* 错误信息

  ```shell
    File "C:\Python27\lib\functools.py", line 56, in <lambda>
      '__lt__': [('__gt__', lambda self, other: other < self),
    ...
    File "C:\Python27\lib\functools.py", line 56, in <lambda>
      '__lt__': [('__gt__', lambda self, other: other < self),
  RuntimeError: maximum recursion depth exceeded in cmp
  ```

* 解决方案

  修改源码, 将如下信息进行修改

  ```python
  convert = {
          '__lt__': [('__gt__', lambda self, other: other < self),
                     ('__le__', lambda self, other: not other < self),
                     ('__ge__', lambda self, other: not self < other)],
          '__le__': [('__ge__', lambda self, other: other <= self),
                     ('__lt__', lambda self, other: not other <= self),
                     ('__gt__', lambda self, other: not self <= other)],
          '__gt__': [('__lt__', lambda self, other: other > self),
                     ('__ge__', lambda self, other: not other > self),
                     ('__le__', lambda self, other: not self > other)],
          '__ge__': [('__le__', lambda self, other: other >= self),
                     ('__gt__', lambda self, other: not other >= self),
                     ('__lt__', lambda self, other: not self >= other)]
      }
  
  ```

  修改为

  ```python
      convert = {
          '__lt__': [('__gt__', lambda self, other: not (self < other or self == other)),
                     ('__le__', lambda self, other: self < other or self == other),
                     ('__ge__', lambda self, other: not self < other)],
          '__le__': [('__ge__', lambda self, other: not self <= other or self == other),
                     ('__lt__', lambda self, other: self <= other and not self == other),
                     ('__gt__', lambda self, other: not self <= other)],
          '__gt__': [('__lt__', lambda self, other: not (self > other or self == other)),
                     ('__ge__', lambda self, other: self > other or self == other),
                     ('__le__', lambda self, other: not self > other)],
          '__ge__': [('__le__', lambda self, other: (not self >= other) or self == other),
                     ('__gt__', lambda self, other: self >= other and not self == other),
                     ('__lt__', lambda self, other: not self >= other)]
      }
  
  ```


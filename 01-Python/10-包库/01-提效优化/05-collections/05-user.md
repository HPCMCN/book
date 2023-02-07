## UserList

`UserList`与`list`对象基本相同, 一般继承并改写`List`时最好是使用`UserList`, 这样`list`还可以用于其他用途, 不会出现冲突.

```Python
def __init__(list):
    return UserList
```

* `self.data`: 用于存储数据的变量

## UserString

同`UserString`

```Python
def __init__(sting):
    return UserString
```

* self.data: 用于存储str的变量

## UserDict

`UserDict`与`Dict`对象基本相同, 一般继承并改写`Dict`时最好是使用`UserDict`, 这样`dict`还可以用于其他用途, 不会出现冲突.

```Python
def __init__(dict):
    return UserDict
```

* self.data: 用于保存`UserDict`的变量

# 1. 对象

## 1.1 获取属性和方法

### 1.1.1 attrgetter

批量获取属性或方法

```python
def attrgetter(*attrs):
return list/one
```

* `attrs`: `str`, 需要获取的方法, 支持多个和单个, 单个返回单个的属性和方法, 多个返回`list`

**示例**

```python
class Demo:
    def __init__(self):
        self.a = "a"
        self.b = "c"


class Test:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = Demo()

    def pt(self, a, b):
        print("do something", a, b)
        return self.a, self.b

# attrgetter批量获取对象属性
t = Test()
f = operator.attrgetter("c.a", "b", "a", "c.b", "pt")
print(f(t))
```

输出

```python
('a', 2, 1, 'c', <bound method Test.pt of <__main__.Test object at 0x000001F5B763FB00>>)
```

## 1.2 动态执行方法

### 1.2.1 methodcaller

直接获取并执行函数

```python
def methodcaller(name, /, *args, **kwargs):
return function_value
```

* args: `*args`, 不定长参数, 为函数的参数值
* kwargs: `**kwargs`, 不定长参数, 为函数的参数值

**示例**

```python
t = Test()
f = operator.methodcaller("pt", 3, 4)
print(f(t))
```

输出

```python
do something 3 4
(1, 2)
```

# 2. 其他

## 2.1 索引映射

### 2.1.1 itemgetter

批量获取索引值对应的值

```python
def itemgetter(*items):
return one/list
```

* items: `index/key`,如果动态获取的为`list`, 则`items`为索引, 如果为`dict`, 则`items`为`key` . 支持单个或者多个

**示例**

```python
t_list = [1, 2, 3, 4, 5]
f = operator.itemgetter(1, 2, 3, 4)  # 类似t_list[1],t_list[2],t_list[3],t_list[4]
print(f(t_list))
t_dict = {"a": 2, "b": 1, "e": 3}
print(operator.itemgetter("b")(t_dict))  # 类似直接取值 t_dict["b"]
print(sorted(t_dict.items(), key=operator.itemgetter(1))) # 类似:lambda x: x[1]
```

输出

```python
(2, 3, 4, 5)
1
[('b', 1), ('a', 2), ('e', 3)]
```


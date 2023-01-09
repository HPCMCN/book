### 1. argparser

#### ArgumentParser.add_argument

```python
def add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
```

* name or flags: str/list, 命令的名称, 例如: `-p`/`(-p, --host)`/`p`

* dest: str, 解析后读取参数的名称, 默认是从`name or flags`中寻找`--`或者`-`来获取的

  ```python
  parser.add_argument("p")
  # 此时参数获取: args.p
  
  parser.add_argument("-p")
  # 参数传递: python filename -p 111
  # 此时参数获取: args.p
  
  parser.add_argument("-p", "--port-ip")
  # 参数传递: 
  #	python filename -p 111
  #	python filename --port-ip=111
  # 此时参数获取: args.port_ip  # 注意-要转化为_
  
  parser.add_argument("-p", "--port-ip", dest="p")
  # 此时参数获取: args.p
  ```

* action: 

  * store: 默认值, 如果被调用则返回命令行值, 否则则视情况报错.

  * store_const: 如果被调用则返回`const`值, 否则返回`None`

    ```python
    parser.add_argument('-x', action='store_const', const=111) 
    parser.add_argument('-y', action='store_const', const=222)
    # python filename.py -x
    # args.x ==> 111, args.y ==> None
    ```

  * store_flase/true: 如果被调用则返回`True`, 否则返回`False`/`True`

    ```python
    parser.add_argument('-x', action='store_False') 
    parser.add_argument('-y', action='store_False')
    # python filename.py -x
    # args.x ==> False, args.y ==> True
    ```

  * append: 可以设置多个value, 返回一个list

    ```python
    parser.add_argument('-x', action='append') 
    # python filename -x 1 -x 2
    # args.x ==> ["1", "2"]
    ```

  * append_const: 类似`store_const`, 创建一组调用后产生的默认值.

    ```python
    parser.add_argument('-x', action="append_const", dest="a", const="2")
    parser.add_argument('-y', action="append_const", dest="a", const="1")
    # python filename -x -y
    # 注意: 这里需要调用dest
    # args.a ==> ["2", "1"]
    ```

  * count: 统计被调用的次数

    ```python
    parser.add_argument('-x', action="count")
    # python filename -x -x -x
    # python filename -xxx
    # args.x ==> 3
    ```

  * extend: int/`*`/`+`, 一次性传递多个参数, 生成一个列表

    ```python
    parser.add_argument('-x', action="extend", nargs=3, type=int)
    # python filename -x 1 2 3
    # args.x ==> [1, 2, 3]
    ```

  * version: 指定版本信息

    ```python
    import argparse
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('--version', action='version', version='%(prog)s 2.0')
    # python filename --version
    # 调用后返回: PROG 2.0, 然后直接退出程序
    ```

  * help: 打印help信息, 然后直接退出

* nargs: 指定命令行参数后面的值的个数, 默认为None, 表示1个

  * `int`: 表示指定数量个

  * `?`: 表示被调用时传递参数则使用传递的value, 如果没有传递参数, 则使用const值, 如果没有被调用, 则使用default值

    ```python
    parser.add_argument('-x', nargs="?", const="a", default=2)
    # python filename -x 1
    # args.x ==> 1
    ###############################
    # python filename -x
    # args.x ==> a
    ###############################
    # python filename
    # args.x ==> 2
    ```

  * `*`: 表示可以传递一个或者多个值

  * `+`: 表示至少传递一个值

* const: 此值设置时, 必须有一下情况

  * `action='store_const'`/`action='append_const'`
  * `nargs="?"`

  参数被调用,但是没有传递数据进来, 将会引用const设置的值, 例如

  ```python
  parser.add_argument('-x', nargs="?", const="a")
  # python filename -x
  # args.x ==> a
  ```

* default: 缺省值

* type: 类型转换, 将传递参数或者缺省参数, 调用type执行后返回, 参见类型

  ```python
  int/float/ascii/ord
  open: 读取文件
  argparse.FileType("w", encoding="utf-8"): 读/写入文件
  pathlib.Path: 路径对象
  自定义:
      def add_1(string):
          return int(string) + 1
  ```

* choices: 指定只允许传递的参数, 否则会报错

* metavar: 给传递进来的value的提示信息

  ```python
  parser.add_argument('-x', metavar="int类型")
  parser.add_argument('-y', nargs=2, metavar=("host", "port"))
  # python filename -h
  ```

  输出信息如下

  ```python
  usage: ProgramName [-h] [-x int类型] [-y host port]
  
  What the program does
  
  options:
    -h, --help    show this help message and exit
    -x int类型
    -y host port
  ```

* required: 此参数是否必须传递, 默认False

* help: 提示给用户的说明文本信息

#### 读取文件

```python
parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
```

#### 参数分组

```python
group1 = parser.add_argument_group(group_name, description)
group1.add_argument(xxx)
group2 = parser.add_argument_group(group_name, description)
group2.add_argument(xxx)
```

#### 参数互斥

```python
mult_param = add_mutually_exclusive_group()
mult_param.add_argument("a")
mult_param.add_argument("b")
# 此时 a和b参数, 只能被调用一个
```

### 示例

```python
import argparser

# 不要用 -h, 与内置的help冲突, 会报错的.
parser = argparse.ArgumentParser(description="xxx")
# bool类型
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('-v', '--verbose',action='store_true') 

args = parser.parse_args()
print(args.verboser, args.v)
print(args.integers)
```


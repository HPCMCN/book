# 1. 安装

* Python3.4版本安装

  ```shell
  altgraph==0.17
  future==0.18.2
  macholib==1.14
  pefile==2019.4.18
  PyInstaller==3.4
  pywin32-ctypes==0.2.0
  wheel==0.33.6
  ```

# 2. 异常处理

# 2.1 场景一

* 错误代码

  ```shell
  # main.py
  import a
  
  # a.py
  import b
  ```

* 错误信息

  执行 `pyinstaller -F main.py`, 报错信息如下:

  ```shell
  # main.py
  import a
  
  # a.py
  import b
  ```

* 解决方式

  在入口文件中, 提前导入全部需要用到的包, 防止打包时未打入.

  ```shell
  # main.py
  import a
  import b
  ```

## 2.2 场景二

* 错误代码

  ```shell
  os.path.dirname(os.path.abspath(__file__))
  ```

* 报错信息

  执行 `pyinstaller -F main.py`, 报错信息如下:

  ```shell
  OSError: [Errno 2] No such file or directory: '/tmp/_MEJIOSNzGe/test.txt'
  [100180] Failed to execute script run
  ```

* 解决方式

  使用`sys.argv[0]`来代替`__file__`即

  ```shell
  BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
  ```

## 2.3 场景三

* 错误场景

  当前系统中存在多个虚拟环境, `pyinstaller`安装在默认环境中, 在虚拟环境中使用`pyinstaller`打包程序, 在可执行软件运行时会报错找不到模块的错误 

* 解决方式

  在`pyinstaller`打包时要注意输出的日志中是否所有导入的模块的`hook`都存在, 如果不存在, 可能是当前环境引发的问题
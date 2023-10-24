# Tarfile

> ```python
> def __init__(self, name=None, mode="r", fileobj=None, format=None,
>             tarinfo=None, dereference=None, ignore_zeros=None, encoding=None,
>             errors="surrogateescape", pax_headers=None, debug=None,
>             errorlevel=None, copybufsize=None):
> ```

* name: str, 待操作的压缩文件名称
* mode: str, 压缩文件打开模式
* fileobj: file-object, 带待操作压缩文件对象, 优先级高于name
* tarinfo: tar包操作对象
* dereference: bool, 软连接压缩时, 是否直接压缩软连接的文本内容, 而不是软连接文件.
* ignore_zeros: bool, 是否压缩空文本块
* encoding: 对于压缩文件内容的打开编码方式
* errors: 对于encoding编码异常处理方式
* pax_headers: pax压缩字典
* debug: 调试模式等级
* errorlevel: 控制如何处理提取错误
* copybufsize: tar包copy时, 缓存区大小控制

**示例一**

```python
with open("b.tar.gz", "wb+") as fileobj:
    # open内部调用的是TarFile
    with tarfile.open(mode="w", fileobj=fileobj, dereference=True) as fp:
        for file in get_zip_files(zip_path):
            filename = os.path.basename(file)
            fp.add(file, filename)
```

**示例二**

```python
with open("b.tar.gz", "wb+") as fileobj:
    with tarfile.TarFile(mode="w", fileobj=fileobj, dereference=True) as fp:
        for file in get_zip_files(zip_path):
            filename = os.path.basename(file)
            fp.add(file, filename)
```

# 1. 压缩

### 1.1.1 add

压缩文件

> ```python
> def add(self, name, arcname=None, recursive=True, *, filter=None):
> ```

* name: str, 需要进行压缩的文件
* arcname: str, 重命名压缩文件的文件名字
* recursive: bool, 如果name是文件夹, 是否进行递归压缩
* filter: function, 压缩文件时, 进行filter过滤规则

**示例**

```python
with tarfile.open("a.tar.gz", mode="w:gz", dereference=True) as fp:
    for file in get_zip_files(zip_path):
        filename = os.path.basename(file)
        fp.add(file, filename)
```

# 2. 解压

### 2.1.1 extractall

> ```python
> def extractall(self, path=".", members=None, *, numeric_owner=False):
> ```

* path: str, 解压文件到指定位置
* members: Iterable, 需要解压的文件, 默认是全部
* numeric_owner: bool, 是否使用tar包内部提供的group和user信息, 默认False

# 3. 查看压缩文件

### 1.3.1 getmembers

### 1.3.2 getmember

### 1.3.3 list

> ```python
> def list(self, verbose=True, *, members=None):
> ```

* verbose: bool, True类似`ls -l`, False将会调用`getmembers`
* members: Iterable, 压缩文件中的文件, 默认是全部
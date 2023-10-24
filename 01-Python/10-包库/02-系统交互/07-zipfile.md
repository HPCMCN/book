### 1.1.1 压缩

> TarFile
>
> ```python
> def __init__(self, name=None, mode="r", fileobj=None, format=None,
>             tarinfo=None, dereference=None, ignore_zeros=None, encoding=None,
>             errors="surrogateescape", pax_headers=None, debug=None,
>             errorlevel=None, copybufsize=None)
> ```

* name: str, 需要操作压缩文件名字
* mode: str, 压缩文件打开模式
* fileobj: file-object, 需要操作的压缩文件流对象, 优先级大于name
* format: 压缩模式
* tarinfo: tar包操作对象
* dereference: bool, True表示打包时, 遇到软连接直接将链接的文件内容打包, 而不是软连接.
* ignore_zeros: bool, 是否在打包时, 忽略空数据块
* encoding: 对于操作的压缩文件内容, 采用的文件打开编码格式
* errors: 对于encoding异常的错误处理方式
* pax_headers: pax字典
* debug: 调试模式
* errorlevel: 异常控制

**示例**:

```python
with open("b.tar.gz", "wb+") as fileobj:
    with tarfile.TarFile(mode="w", fileobj=fileobj, dereference=True) as fp:
        for file in get_zip_files(zip_path):
            filename = os.path.basename(file)
            fp.add(file, filename)
```

### 1.1.2 解压


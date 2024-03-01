# 1. Sphinx

## 1.1 安装

```shell
pip install sphinx
# 注意这玩意有很多插件, 如果使用对应的插件需要自己下载
```

# 2. 使用

1. 项目初始化

   ```shell
   sphinx-quickstart
   # 中文是: zh_CN
   ```

2. 配置文件(MakeFile)

   ```shell
   # 项目路径为: /opt/project
   # 文档路径: /opt/project/docs
   # 注意这里我改了, 默认为source, 同时需要将_template, _build, conf.py文件copy到docs下
   # mv sources/* /opt/project/docs
   SOURCEDIR     = .  # 配置文件所在文件夹, 也是rst生成的位置
   BUILDDIR      = build  # 编译html等文件生成的文件夹
   ```

3. 配置文件(conf.py)

   ```python
   # 屏蔽目录
   exclude_patterns = [
       "migrations/*",
       "tests/*",
       "mytest/*",
       "grpc_procto/*"
       "docs"
   ]
   
   # 扫描代码时, 存在模块导入失败, 这里用来mock失败模块, 防止报错无法正常扫描
   autodoc_mock_imports = [
       "*",
   ]
   ```

4. 设置index.rst

   ```shell
   #/opt/project/docs/index.rst
   # 这个文件可以参考 github上的, 有很多
   Welcome to prject documentation!
   ======================================
   
   .. toctree::
      :glob: 2
   	
   	*
   
   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
   ```

   

5. 开始生成目录文件rst

   ```shell
   # 所在位置: /opt/project/docs
   sphinx-apidoc -o . /opt/project/src
   ```

6. 将生成好的rst编译为html

   ```shell
   make html
   # 注意这里可能出现module导入失败, 那就将该modules添加到autodoc_mock_imports中, 重新执行即可
   ```

   


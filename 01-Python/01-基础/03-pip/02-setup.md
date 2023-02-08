# 1. pypi源

## 1.1 包构建

* 目录构建 如下

  ```shell
  [root@VM-4-12-centos cron-log]# tree
  .
  |-- LICENSE
  |-- pyproject.toml  # pip 配置参数
  |-- README.md
  `-- src
      |-- cron_log  # 项目所在目录
      |   |-- expressions.py
      |   |-- fields.py
      |   |-- handlers.py
      |   |-- __init__.py
      |   |-- trigger.py
      |   `-- util.py
      `-- __init__.py
  
  2 directories, 10 files
  ```

* pip打包文件 `pyproject.toml`

  可以查看官方文档进行配置: https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
  
  ```
  [build-system]
  requires = ["setuptools"]
  build-backend = "setuptools.build_meta"
  
  [project]
  name = "cron_log"
  version = "1.0.0"
  keywords = ["logging", "cron"]
  authors = [
      { name = "hpcm", email = "hpcm@foxmail.com" }
  ]
  maintainers = [
      { name = "hpcm", email = "hpcm@foxmail.com" }
  ]
  description = "cron logging"
  
  readme = { file = "README.md", content-type = "text/markdown" }
  license = { text = "MIT License" }
  requires-python = ">= 3.4"
  classifiers = [
      "Operating System :: Microsoft :: Windows",
      "Operating System :: Unix",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Programming Language :: Python :: 3 :: Only",
      "Programming Language :: Python :: Implementation :: CPython",
      "Programming Language :: Python :: Implementation :: PyPy",
  ]
  # 安装时候生成exe, 并加入环境变量中, 可以直接执行这个exe
  entry-points={console_scripts=['cmd_name = cookiecutter.__main__:main']}
  dependencies = [
      #  "httpx",
      #  "gidgethub[httpx]>4.0.0",
      #  "django>2.1; os_name != 'nt'",
      #  "django>2.0; os_name == 'nt'",
  ]
  
  # dynamic = ["version", "description"]
  [project.urls]
  homepage = "https://github.com/HPCMCN"
  documentation = "https://github.com/HPCMCN"
  repository = "https://github.com/HPCMCN"
  changelog = "https://github.com/HPCMCN"
  
  
  [project.optional-dependencies]
  gui = ["PyQt5"]
  cli = [
      "rich",
      "click",
  ]
  
  [project.scripts]
  spam-cli = "spam:main_cli"
  
  [project.gui-scripts]
  spam-gui = "spam:main_gui"
  
  [project.entry-points."spam.magical"]
  tomatoes = "spam:main_tomatoes"
  ```

## 2.2 打包

官网:  https://pypa-build.readthedocs.io/en/stable/release.html

* 下载打包工具

  ```shell
  pip install build
  ```

* 开始打包

  ```shell
  python -m build
  ```

  ![image-20230202165553268](02-%E8%87%AA%E5%AE%9A%E4%B9%89packages/.image/01-setup/image-20230202165553268.png)

* 检查打包好的文件

  ```shell
  ls dist/
  ```

  ![image-20230202165710108](02-%E8%87%AA%E5%AE%9A%E4%B9%89packages/.image/01-setup/image-20230202165710108.png)

## 2.3 发布到pypi

### 2.3.1 认证文件

* 登录官网申请token

  ```html
  https://pypi.org/manage/account/token/
  ```

  ![image-20230202170023628](02-%E8%87%AA%E5%AE%9A%E4%B9%89packages/.image/01-setup/image-20230202170023628.png)

* 根据官方提示创建文件`$HOME/.pypirc`

  ```cfg
  [pypi]
    username = __token__
    password = pypi-AgEIcHl**s3t1Q
  ```

### 2.3.2 发布

官网: https://twine.readthedocs.io/en/latest/

* 安装发布工具

  ```shell
  pip install twine
  ```

* 发布到pypi

  ```shell
  python -m twine upload dist/*
  ```

  ![image-20230202170337440](02-%E8%87%AA%E5%AE%9A%E4%B9%89packages/.image/01-setup/image-20230202170337440.png)

## 2.4 版本更新

* 修改 `pyproject.toml`中的`version`

* 删除`dist/`中的文件, 否则会提示已存在错误

* 发布到pypi

  ```shell
  python -m twine upload dist/*
  ```

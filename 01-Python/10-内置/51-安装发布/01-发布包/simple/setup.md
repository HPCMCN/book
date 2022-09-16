#### 1. 配置文件

`setup.cfg`

```config
[metadata]
name = simple

author = w***g
author_email = w***m

version = 0.0.1

description = Provides the ability to access the auths.
long_description = file: README.md
long_description_content_type = text/markdown
keywords = auth, db

platforms = Linux

url = ""
download_url = ""

license = MIT

classifiers =
    Operating System :: Microsoft :: Windows
    Operating System :: Unix
    Programming Language :: Python
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.7

[options]
zip_safe = false
packages = find:
python_requires = >=3.6

```

`setup.py`

```python
from setuptools import setup

install_requires = [
    "django",
    "requests",
    "djangorestframework"
]

setup(
    install_requires=install_requires,
)
```


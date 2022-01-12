默认celery是不能以root权限执行的, 否则会报错

```python
Running a worker with superuser privileges when the
worker accepts messages serialized with pickle is a very bad idea!

If you really want to continue then you have to set the C_FORCE_ROOT
environment variable (but please think about this before you do).
```

#### 方法一

```python
from celery import Celery, platforms
platforms.C_FORCE_ROOT = True  # 开启root执行模式
```

#### 方法二

```python
# 临时增加linux变量
export C_FORCE_ROOT = "true"
# 或者持久化增加到 /etc/profile中
C_FORCE_ROOT = "true"
# 或者 使用Python向linux中添加
os.environ["C_FORCE_ROOT"] = True
```

#### 方法三

* 全局禁用

  终极手段, 直接禁用Python断言功能

  ```python
  # 利用Python
  export PYTHONOPTIMIZE=1
  # 或者 利用celery
  celery -O 1 -A celery_tasks worker -l info
  ```

* 局部禁用

  由于此断言错误是由multiprocessing模块报错导致, 所以直接修改multiprocessing.processing.py中102行, 关闭断言错误即可.


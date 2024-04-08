注册表获取环境变量数据

```python
import winreg


def get_system_path_variable(name):
    """从系统变量中获取"""
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment") as key:
        try:
            value, _ = winreg.QueryValueEx(key, name)
            return value
        except FileNotFoundError:
            return None

def get_user_path_variable(name):
	"""从用户变量中获取"""
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
        try:
            value, _ = winreg.QueryValueEx(key, name)
            return value
        except FileNotFoundError:
            return None


def get_variable_from_env(key):
    return get_user_path_variable(key) or get_system_path_variable(key)
```


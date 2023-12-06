# 1. 安装

```shell
pip install cx_Freeze
```

# 2. 打包MSI

* 创建`setup.py`文件

  ```python
  import sys
  from cx_Freeze import setup, Executable
  
  build_exe_options = {
      "excludes": ["tkinter", "unittest"],
      "zip_include_packages": ["encodings", "PySide6"],
  }
  
  
  base = "Win32GUI" if sys.platform == "win32" else None
  
  setup(
      name="kyUKeys",
      version="0.1",
      description="My GUI application!",
      options={"build_exe": build_exe_options},
      executables=[Executable("main.py", base=base)],
  )
  ```

* 打包为msi

  ```shell
  python setup.py bdist_msi
  ```

  
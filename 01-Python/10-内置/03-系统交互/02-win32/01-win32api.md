# 1. win32

## 1.1 鼠标

* 获取绝对坐标

  ```shell
  x, y = win32api.GetCursorPos()
  ```

* 修改绝对坐标

  ```shell
  win32api.SetCursorPos(x, y)
  ```
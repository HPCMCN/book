# 1. selenium

用于浏览器控制

## 1.1 驱动下载

* 使用chrome驱动[[点击下载配套的chrome以及驱动]](https://pan.baidu.com/s/1FhdKT2N1AybRn2p_jbmIfg)

  ```python
  http://chromedriver.storage.googleapis.com/index.html
  https://chromedriver.chromium.org/downloads
  ```

* 使用phantomjs浏览器

  ```python
  wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
  tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 
  sudo cp -R phantomjs-2.1.1-linux-x86_64 /usr/local/share/ 
  sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/
  ```

## 1.2 模块安装

```python
pip install selenium
```

# 2. 使用

## 2.1 操作已打开浏览器

* 配置浏览器启动

  选择图标, 将如下代码添加到启动脚本中, 开启浏览器的debug模式

  ```shell
  "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9527 --user-data-dir="F:\selenium\AutomationProfile"
  ```

* 调用方式

  ```python
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  
  webdriver_path = r"E:\chromedriver_win32\chromedriver.exe"
  host = "127.0.0.1"
  port = 9530
      
  options = Options()
  options.add_experimental_option("debuggerAddress", f"{host}:{port}")
  driver = webdriver.Chrome(webdriver_path, options=options)
  ```

  

## 2.2 常规使用

```python
from selenium import webdriver
# 打开对应的浏览器
driver = webdriver.Chrome()
# 打卡网页
driver.get("http://www.baidu.com")
# 获取网页内容
html = driver.page_source
# 获取网页截图
driver.save_screenshot("xx.png")
# 获取class并点击此标签
driver.find_element_by_name("tj_trnews").click()
# 向搜索框中输入数据
driver.find_element_by_id("ww").send_keys(u"百度一下")
# 清除输入框内容
driver.find_element_by_id("kw").clear()
# 模拟Enter回车键
driver.find_element_by_id("su").send_keys(Keys.RETURN)
# 点击搜索到的新闻页面中的第一个
driver.find_element_by_xpath("//div[@id='1']//a").click()
# 查询共有几个窗口
driver.window_handles
# 切换第二个窗口
driver.swith_to_window(driver.window_handlesp[1])
# 截屏
driver.save_screenshot("b***u.com")
# 获取网页title
driver.title
# 获取当前url
driver.current_url
# 关闭当前窗口
driver.quit()
# 调用键盘按键操作时需要引入的Keys包
from selenium.webdriver.common.keys import Keys
# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# 获取当前页面Cookie
print(driver.get_cookies())
```


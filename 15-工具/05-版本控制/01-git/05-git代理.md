### 1. 使用vpn

* 查看代理

  ```shelll
  git config --list | grep proxy  # 查看配置列表
  ```

* 修改代理

  ```shell
  # socks5代理
  git config --global http.proxy socks5://127.0.0.1:10808
  git config --global https.proxy socks5://127.0.0.1:10808
  
  # http代理
  git config --global http.proxy http://127.0.0.1:1080
  git config --global https.proxy https://127.0.0.1:1080
  ```

* 删除代理

  ```shell
  # 取消代理
  git config --global --unset http.proxy
  git config --global --unset https.proxy
  ```

  


# 1. CentOS 7

* 安装client

  ```shell
  yum install pptp pptp-setup
  ```

* 设置 myvpn 认证信息

  ```shell
  pptpsetup --create myvpn --server 101.34.38.199 --username username --password myPassword --encrypt
  ```

* 加载内核模块

  ```shell
  modprobe ppp_mppe
  modprobe nf_conntrack_pptp
  ```

* 启动 myvpn 

  ```shell
  pppd call myvpn
  ```

* 查看启动状况和使用的ip

  ```shell
  grep pppd /var/log/messages | tail -n 10
  ```

* 创建路由信息, 通过vpn进行通讯

  ```shell
  route add -net 192.168.0.0/16 dev eth0
  route add -net 0.0.0.0 dev ppp0
  ```

* 关闭vpn

  ```shell
  killall pppd
  ```

  


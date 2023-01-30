# 1. CentOS 7

* 系统可用性检测

  ```shell
  modprobe ppp-compress-18 && echo ok
  ```

* 服务安装

  ```shell
  yum install epel-release -y
  
  yum install ppp ppp-devel pptpd -y
  ```

* 配置文件

  ```shell
  vim /etc/pptpd.conf
  localip 192.168.0.1 # eth0内网ip地址, 不是公网ip
  remoteip 192.168.0.234-238,192.168.0.245 # 确保给定的网段ip都未被占用
  ```

* 协议配置

  ```shell
  vim /etc/ppp/options.pptpd
  name pptpd
  refuse-pap
  refuse-chap
  refuse-mschap
  require-mschap-v2
  require-mppe-128
  ms-dns 8.8.8.8
  ms-dns 114.114.114.114
  proxyarp
  lock
  nobsdcomp 
  novj
  novjccomp
  nologfd
  logfile /var/log/pptpd.log
  ```

* 账号密码配置

  ```shell
  vim /etc/ppp/chap-secrets
  # 注意: 每个username只能被一个client使用, 否则会出现抢占现象.
  username1 * password1 *
  username2 * password2 *
  ```

* 开启转发功能

  ```shell
  vim /etc/sysctl.conf
  # 生效命令: sysctl -p
  net.ipv4.ip_forward=1
  net.ipv6.conf.all.forwarding=1
  ```

* 启动pptpd

  ```shell
  systemctl start pptpd
  # 注意防火墙需要放开端口: 1723
  ```

  
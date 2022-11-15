# 1. LVS

## 1.1 安装

ipvs是LVS的核心模块

```shell
yum install -y ipvs ipvsadm
```

## 1.2 配置

```shell
# 添加如下信息
vim /etc/modules-load.d/ipvs.conf 
ip_vs
ip_vs_lc
ip_vs_wlc
ip_vs_rr
ip_vs_wrr
ip_vs_lblc
ip_vs_lblcr
ip_vs_dh
ip_vs_sh
ip_vs_fo
ip_vs_nq
ip_vs_sed
ip_vs_ftp
ip_vs_sh
nf_conntrack
ip_tables
ip_set
xt_set
ipt_set
ipt_rpfilter
ipt_REJECT
ipip
```

## 1.3 加载配置

```shell
# 加载到内核
systemctl enable --now systemd-modules-load.service
```

# 2. Haproxy

## 2.1 安装

```shell
yum install haproxy -y
```

## 2.2 配置

```shell
mkdir /etc/haproxy
# 覆盖内容
echo > /etc/haproxy/haproxy.cfg 
vim /etc/haproxy/haproxy.cfg
global
  maxconn  2000
  ulimit-n  16384
  log  127.0.0.1 local0 err
  stats timeout 30s

defaults
  log global
  mode  http
  option  httplog
  timeout connect 5000
  timeout client  50000
  timeout server  50000
  timeout http-request 15s
  timeout http-keep-alive 15s

frontend monitor-in
  bind *:33305
  mode http
  option httplog
  monitor-uri /monitor

frontend master
  bind 0.0.0.0:16443
  bind 127.0.0.1:16443
  mode tcp
  option tcplog
  tcp-request inspect-delay 5s
  default_backend master

backend master
  mode tcp
  option tcplog
  option tcp-check
  balance roundrobin
  default-server inter 10s downinter 5s rise 2 fall 2 slowstart 60s maxconn 250 maxqueue 256 weight 100
  server master01	10.111.0.10:6443  check
  server master02	10.111.0.11:6443  check
  server master03	10.111.0.12:6443  check
```

# 3. Keepalived

## 3.1 安装

```shell
yum install -y keepalived
```

## 3.2 配置

```shell
# 分别修改/etc/keepalived/keepalived.conf文件

# master01
echo > /etc/keepalived/keepalived.conf
vim /etc/keepalived/keepalived.conf

! Configuration File for keepalived
global_defs {
    router_id LVS_DEVEL
script_user root
    enable_script_security
}
vrrp_script chk_apiserver {
    script "/etc/keepalived/check_apiserver.sh"
   interval 5
    weight -5
    fall 2  
rise 1
}
vrrp_instance VI_1 {
    state BACKUP
    interface ens33
    mcast_src_ip 10.111.0.10
    virtual_router_id 51
    priority 100
    advert_int 2
    authentication {
        auth_type PASS
        auth_pass K8SHA_KA_AUTH
    }
    virtual_ipaddress {
        10.111.0.111
    }
    track_script {
       chk_apiserver
    }
}

#master02
echo > /etc/keepalived/keepalived.conf
vim /etc/keepalived/keepalived.conf

! Configuration File for keepalived
global_defs {
    router_id LVS_DEVEL
script_user root
    enable_script_security
}
vrrp_script chk_apiserver {
    script "/etc/keepalived/check_apiserver.sh"
   interval 5
    weight -5
    fall 2  
rise 1
}
vrrp_instance VI_1 {
    state BACKUP
    interface ens33
    mcast_src_ip 10.111.0.11
    virtual_router_id 51
    priority 100
    advert_int 2
    authentication {
        auth_type PASS
        auth_pass K8SHA_KA_AUTH
    }
    virtual_ipaddress {
        10.111.0.111
    }
    track_script {
       chk_apiserver
    }
}

#master03
echo > /etc/keepalived/keepalived.conf
vim /etc/keepalived/keepalived.conf

! Configuration File for keepalived
global_defs {
    router_id LVS_DEVEL
script_user root
    enable_script_security
}
vrrp_script chk_apiserver {
    script "/etc/keepalived/check_apiserver.sh"
   interval 5
    weight -5
    fall 2  
rise 1
}
vrrp_instance VI_1 {
    state BACKUP
    interface ens33
    mcast_src_ip 10.111.0.12
    virtual_router_id 51
    priority 100
    advert_int 2
    authentication {
        auth_type PASS
        auth_pass K8SHA_KA_AUTH
    }
    virtual_ipaddress {
        10.111.0.111
    }
    track_script {
       chk_apiserver
    }
}
```

## 3.3 设置健康检查

```shell
vim /etc/keepalived/check_apiserver.sh # 配置如下信息
#!/bin/bash
err=0
for k in $(seq 1 3)
do
    check_code=$(pgrep haproxy)
    if [[ $check_code == "" ]]; then
        err=$(expr $err + 1)
        sleep 1
        continue
    else
        err=0
        break
    fi
done

if [[ $err != "0" ]]; then
    echo "systemctl stop keepalived"
    /usr/bin/systemctl stop keepalived
    exit 1
else
    exit 0
fi
```

# 4. 启动高可用集群

## 4.1 启动

```shell
chmod +x /etc/keepalived/check_apiserver.sh

systemctl daemon-reload
systemctl enable --now haproxy && systemctl start  haproxy 
systemctl enable --now keepalived && systemctl start keepalived 
```

## 4.1 测试

```shell
 ping 10.111.0.111 -c 4
 telnet 10.111.0.111 16443  # telnet不通, 认为vip未设置成功
```

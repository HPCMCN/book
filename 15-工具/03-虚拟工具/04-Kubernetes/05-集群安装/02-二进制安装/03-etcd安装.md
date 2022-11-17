#### 配置etcd配置

* master01

  ```shell
  vim /etc/etcd/etcd.config.yml
  
  name: 'master01'  # 这里需要修改
  data-dir: /var/lib/etcd
  wal-dir: /var/lib/etcd/wal
  snapshot-count: 5000
  heartbeat-interval: 100
  election-timeout: 1000
  quota-backend-bytes: 0
  listen-peer-urls: 'https://10.111.0.10:2380'
  listen-client-urls: 'https://10.111.0.10:2379,http://127.0.0.1:2379'
  max-snapshots: 3
  max-wals: 5
  cors:
  initial-advertise-peer-urls: 'https://10.111.0.10:2380'  # 修改本机ip
  advertise-client-urls: 'https://10.111.0.10:2379' # 修改本机ip
  discovery:
  discovery-fallback: 'proxy'
  discovery-proxy:
  discovery-srv:
  initial-cluster: 'master01=https://10.111.0.10:2380,master02=https://10.111.0.11:2380,master03=https://10.111.0.12:2380' # 修改master节点ip
  initial-cluster-token: 'etcd-k8s-cluster'
  initial-cluster-state: 'new'
  strict-reconfig-check: false
  enable-v2: true
  enable-pprof: true
  proxy: 'off'
  proxy-failure-wait: 5000
  proxy-refresh-interval: 30000
  proxy-dial-timeout: 1000
  proxy-write-timeout: 5000
  proxy-read-timeout: 0
  client-transport-security:
    cert-file: '/etc/kubernetes/pki/etcd/etcd.pem'
    key-file: '/etc/kubernetes/pki/etcd/etcd-key.pem'
    client-cert-auth: true
    trusted-ca-file: '/etc/kubernetes/pki/etcd/etcd-ca.pem'
    auto-tls: true
  peer-transport-security:
    cert-file: '/etc/kubernetes/pki/etcd/etcd.pem'
    key-file: '/etc/kubernetes/pki/etcd/etcd-key.pem'
    peer-client-cert-auth: true
    trusted-ca-file: '/etc/kubernetes/pki/etcd/etcd-ca.pem'
    auto-tls: true
  debug: false
  log-package-levels:
  log-outputs: [default]
  force-new-cluster: false
  
  ```

* master02

  ```shell
  vim /etc/etcd/etcd.config.yml
  
  name: 'master02'  # 这里需要修改
  data-dir: /var/lib/etcd
  wal-dir: /var/lib/etcd/wal
  snapshot-count: 5000
  heartbeat-interval: 100
  election-timeout: 1000
  quota-backend-bytes: 0
  listen-peer-urls: 'https://10.111.0.11:2380'
  listen-client-urls: 'https://10.111.0.11:2379,http://127.0.0.1:2379'
  max-snapshots: 3
  max-wals: 5
  cors:
  initial-advertise-peer-urls: 'https://10.111.0.11:2380'  # 修改本机ip
  advertise-client-urls: 'https://10.111.0.11:2379' # 修改本机ip
  discovery:
  discovery-fallback: 'proxy'
  discovery-proxy:
  discovery-srv:
  initial-cluster: 'master01=https://10.111.0.10:2380,master02=https://10.111.0.11:2380,master03=https://10.111.0.12:2380' # 修改master节点ip
  initial-cluster-token: 'etcd-k8s-cluster'
  initial-cluster-state: 'new'
  strict-reconfig-check: false
  enable-v2: true
  enable-pprof: true
  proxy: 'off'
  proxy-failure-wait: 5000
  proxy-refresh-interval: 30000
  proxy-dial-timeout: 1000
  proxy-write-timeout: 5000
  proxy-read-timeout: 0
  client-transport-security:
    cert-file: '/etc/kubernetes/pki/etcd/etcd.pem'
    key-file: '/etc/kubernetes/pki/etcd/etcd-key.pem'
    client-cert-auth: true
    trusted-ca-file: '/etc/kubernetes/pki/etcd/etcd-ca.pem'
    auto-tls: true
  peer-transport-security:
    cert-file: '/etc/kubernetes/pki/etcd/etcd.pem'
    key-file: '/etc/kubernetes/pki/etcd/etcd-key.pem'
    peer-client-cert-auth: true
    trusted-ca-file: '/etc/kubernetes/pki/etcd/etcd-ca.pem'
    auto-tls: true
  debug: false
  log-package-levels:
  log-outputs: [default]
  force-new-cluster: false
  
  ```

* master03

  ```shell
  vim /etc/etcd/etcd.config.yml
  
  name: 'master03'  # 这里需要修改
  data-dir: /var/lib/etcd
  wal-dir: /var/lib/etcd/wal
  snapshot-count: 5000
  heartbeat-interval: 100
  election-timeout: 1000
  quota-backend-bytes: 0
  listen-peer-urls: 'https://10.111.0.12:2380'
  listen-client-urls: 'https://10.111.0.12:2379,http://127.0.0.1:2379'
  max-snapshots: 3
  max-wals: 5
  cors:
  initial-advertise-peer-urls: 'https://10.111.0.12:2380'  # 修改本机ip
  advertise-client-urls: 'https://10.111.0.12:2379' # 修改本机ip
  discovery:
  discovery-fallback: 'proxy'
  discovery-proxy:
  discovery-srv:
  initial-cluster: 'master01=https://10.111.0.10:2380,master02=https://10.111.0.11:2380,master03=https://10.111.0.12:2380' # 修改master节点ip
  initial-cluster-token: 'etcd-k8s-cluster'
  initial-cluster-state: 'new'
  strict-reconfig-check: false
  enable-v2: true
  enable-pprof: true
  proxy: 'off'
  proxy-failure-wait: 5000
  proxy-refresh-interval: 30000
  proxy-dial-timeout: 1000
  proxy-write-timeout: 5000
  proxy-read-timeout: 0
  client-transport-security:
    cert-file: '/etc/kubernetes/pki/etcd/etcd.pem'
    key-file: '/etc/kubernetes/pki/etcd/etcd-key.pem'
    client-cert-auth: true
    trusted-ca-file: '/etc/kubernetes/pki/etcd/etcd-ca.pem'
    auto-tls: true
  peer-transport-security:
    cert-file: '/etc/kubernetes/pki/etcd/etcd.pem'
    key-file: '/etc/kubernetes/pki/etcd/etcd-key.pem'
    peer-client-cert-auth: true
    trusted-ca-file: '/etc/kubernetes/pki/etcd/etcd-ca.pem'
    auto-tls: true
  debug: false
  log-package-levels:
  log-outputs: [default]
  force-new-cluster: false
  
  ```

#### 创建service

所有master节点上执行

* 创建启动服务

  ```shell
  vim /usr/lib/systemd/system/etcd.service
  
  [Unit]
  Description=Etcd Service
  Documentation=https://coreos.com/etcd/docs/latest/
  After=network.target
  
  [Service]
  Type=notify
  ExecStart=/usr/local/bin/etcd --config-file=/etc/etcd/etcd.config.yml
  Restart=on-failure
  RestartSec=10
  LimitNOFILE=65536
  
  [Install]
  WantedBy=multi-user.target
  Alias=etcd3.service
  ```

* 创建证书目录

  ```shell
  mkdir /etc/kubernetes/pki/etcd
  ln -s /etc/etcd/ssl/* /etc/kubernetes/pki/etcd/
  ```

* 加载启动

  ```shell
  systemctl daemon-reload
  systemctl enable --now etcd
  ```
  
* 查看状态

  ```shell
  export ETCDCTL_API=3
  etcdctl --endpoints="10.111.0.10:2379,10.111.0.11:2379,10.111.0.12:2379" --cacert=/etc/kubernetes/pki/etcd/etcd-ca.pem --cert=/etc/kubernetes/pki/etcd/etcd.pem --key=/etc/kubernetes/pki/etcd/etcd-key.pem  endpoint status --write-out=table
  
  systemctl status etcd -l    # 不要出现E开头的错误
  tail -f /var/log/messages
  ```


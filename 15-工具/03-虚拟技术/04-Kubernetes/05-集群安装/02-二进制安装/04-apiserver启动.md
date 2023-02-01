# [高可用部署](..\..\..\..\01-代理负载\03-高可用\01-LVS\02-高可用安装.md) 

# 1. 配置文件

注意: 一定要确保配置文件中的证书存在

* master01

  ```shell
  # 注意service-cluster-ip-range=10.0.0.0/12   是server 网段
  # /usr/lib/systemd/system/kube-apiserver.service 
  [Unit]
  Description=Kubernetes API Server
  Documentation=https://github.com/kubernetes/kubernetes
  After=network.target
  
  [Service]
  ExecStart=/usr/local/bin/kube-apiserver \
        --v=2  \
        --feature-gates=EphemeralContainers=true  \  # 开启临时容器
        --logtostderr=true  \
        --allow-privileged=true  \
        --bind-address=0.0.0.0  \
        --secure-port=6443  \
        --insecure-port=0  \
        --advertise-address=10.111.0.10 \
        --service-cluster-ip-range=10.0.0.0/12  \
        --service-node-port-range=30000-32767  \
        --etcd-servers=https://10.111.0.10:2379,https://10.111.0.11:2379,https://10.111.0.12:2379 \
        --etcd-cafile=/etc/etcd/ssl/etcd-ca.pem  \
        --etcd-certfile=/etc/etcd/ssl/etcd.pem  \
        --etcd-keyfile=/etc/etcd/ssl/etcd-key.pem  \
        --client-ca-file=/etc/kubernetes/pki/ca.pem  \
        --tls-cert-file=/etc/kubernetes/pki/apiserver.pem  \
        --tls-private-key-file=/etc/kubernetes/pki/apiserver-key.pem  \
        --kubelet-client-certificate=/etc/kubernetes/pki/apiserver.pem  \
        --kubelet-client-key=/etc/kubernetes/pki/apiserver-key.pem  \
        --service-account-key-file=/etc/kubernetes/pki/sa.pub  \
        --service-account-signing-key-file=/etc/kubernetes/pki/sa.key  \
        --service-account-issuer=https://kubernetes.default.svc.cluster.local \
        --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname  \
        --enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,DefaultTolerationSeconds,NodeRestriction,ResourceQuota  \
        --authorization-mode=Node,RBAC  \
        --enable-bootstrap-token-auth=true  \
        --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.pem  \
        --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.pem  \
        --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client-key.pem  \
        --requestheader-allowed-names=aggregator  \
        --requestheader-group-headers=X-Remote-Group  \
        --requestheader-extra-headers-prefix=X-Remote-Extra-  \
        --requestheader-username-headers=X-Remote-User
        # --token-auth-file=/etc/kubernetes/token.csv
  
  Restart=on-failure
  RestartSec=10s
  LimitNOFILE=65535
  
  [Install]
  WantedBy=multi-user.target
  ```

  

* master02

  ```shell
  # /usr/lib/systemd/system/kube-apiserver.service 
  # 注意service-cluster-ip-range=10.0.0.0/12   是server 网段
  [Unit]
  Description=Kubernetes API Server
  Documentation=https://github.com/kubernetes/kubernetes
  After=network.target
  
  [Service]
  ExecStart=/usr/local/bin/kube-apiserver \
        --v=2  \
        --feature-gates=EphemeralContainers=true  \  # 开启临时容器
        --logtostderr=true  \
        --allow-privileged=true  \
        --bind-address=0.0.0.0  \
        --secure-port=6443  \
        --insecure-port=0  \
        --advertise-address=10.111.0.11 \
        --service-cluster-ip-range=10.0.0.0/12  \
        --service-node-port-range=30000-32767  \
        --etcd-servers=https://10.111.0.10:2379,https://10.111.0.11:2379,https://10.111.0.12:2379 \
        --etcd-cafile=/etc/etcd/ssl/etcd-ca.pem  \
        --etcd-certfile=/etc/etcd/ssl/etcd.pem  \
        --etcd-keyfile=/etc/etcd/ssl/etcd-key.pem  \
        --client-ca-file=/etc/kubernetes/pki/ca.pem  \
        --tls-cert-file=/etc/kubernetes/pki/apiserver.pem  \
        --tls-private-key-file=/etc/kubernetes/pki/apiserver-key.pem  \
        --kubelet-client-certificate=/etc/kubernetes/pki/apiserver.pem  \
        --kubelet-client-key=/etc/kubernetes/pki/apiserver-key.pem  \
        --service-account-key-file=/etc/kubernetes/pki/sa.pub  \
        --service-account-signing-key-file=/etc/kubernetes/pki/sa.key  \
        --service-account-issuer=https://kubernetes.default.svc.cluster.local \
        --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname  \
        --enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,DefaultTolerationSeconds,NodeRestriction,ResourceQuota  \
        --authorization-mode=Node,RBAC  \
        --enable-bootstrap-token-auth=true  \
        --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.pem  \
        --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.pem  \
        --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client-key.pem  \
        --requestheader-allowed-names=aggregator  \
        --requestheader-group-headers=X-Remote-Group  \
        --requestheader-extra-headers-prefix=X-Remote-Extra-  \
        --requestheader-username-headers=X-Remote-User
        # --token-auth-file=/etc/kubernetes/token.csv
  
  Restart=on-failure
  RestartSec=10s
  LimitNOFILE=65535
  
  [Install]
  WantedBy=multi-user.target
  ```
  
* master03

  ```shell
  # /usr/lib/systemd/system/kube-apiserver.service 
  # 注意service-cluster-ip-range=10.0.0.0/12   是server 网段
  [Unit]
  Description=Kubernetes API Server
  Documentation=https://github.com/kubernetes/kubernetes
  After=network.target
  
  [Service]
  ExecStart=/usr/local/bin/kube-apiserver \
        --v=2  \
        --feature-gates=EphemeralContainers=true  \  # 开启临时容器
        --logtostderr=true  \
        --allow-privileged=true  \
        --bind-address=0.0.0.0  \
        --secure-port=6443  \
        --insecure-port=0  \
        --advertise-address=10.111.0.12 \
        --service-cluster-ip-range=10.0.0.0/12  \
        --service-node-port-range=30000-32767  \
        --etcd-servers=https://10.111.0.10:2379,https://10.111.0.11:2379,https://10.111.0.12:2379 \
        --etcd-cafile=/etc/etcd/ssl/etcd-ca.pem  \
        --etcd-certfile=/etc/etcd/ssl/etcd.pem  \
        --etcd-keyfile=/etc/etcd/ssl/etcd-key.pem  \
        --client-ca-file=/etc/kubernetes/pki/ca.pem  \
        --tls-cert-file=/etc/kubernetes/pki/apiserver.pem  \
        --tls-private-key-file=/etc/kubernetes/pki/apiserver-key.pem  \
        --kubelet-client-certificate=/etc/kubernetes/pki/apiserver.pem  \
        --kubelet-client-key=/etc/kubernetes/pki/apiserver-key.pem  \
        --service-account-key-file=/etc/kubernetes/pki/sa.pub  \
        --service-account-signing-key-file=/etc/kubernetes/pki/sa.key  \
        --service-account-issuer=https://kubernetes.default.svc.cluster.local \
        --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname  \
        --enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,DefaultTolerationSeconds,NodeRestriction,ResourceQuota  \
        --authorization-mode=Node,RBAC  \
        --enable-bootstrap-token-auth=true  \
        --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.pem  \
        --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.pem  \
        --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client-key.pem  \
        --requestheader-allowed-names=aggregator  \
        --requestheader-group-headers=X-Remote-Group  \
        --requestheader-extra-headers-prefix=X-Remote-Extra-  \
        --requestheader-username-headers=X-Remote-User
        # --token-auth-file=/etc/kubernetes/token.csv
  
  Restart=on-failure
  RestartSec=10s
  LimitNOFILE=65535
  
  [Install]
  WantedBy=multi-user.target
  ```

# 2. 启动服务

* 全部节点创建

  ```shell
  mkdir -p /etc/kubernetes/manifests/ /etc/systemd/system/kubelet.service.d /var/lib/kubelet /var/log/kubernetes
  ```

* 启动服务

  ```shell
  systemctl daemon-reload 
  systemctl enable --now kube-apiserver
  ```

* 检查

  ```shell
  systemctl status kube-apiserver
  tail -f /var/log/messages   #  不要出现E开头日志, [-]poststarthook/rbac/bootstrap-roles failed: not  这种不是错误
  ```

  


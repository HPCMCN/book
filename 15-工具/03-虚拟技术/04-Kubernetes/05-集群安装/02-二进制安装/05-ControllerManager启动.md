# 1. 配置文件

* 全部master节点配置

  ```shell
  # /usr/lib/systemd/system/kube-controller-manager.service
  [Unit]
  Description=Kubernetes Controller Manager
  Documentation=https://github.com/kubernetes/kubernetes
  After=network.target

  [Service]
  ExecStart=/usr/local/bin/kube-controller-manager \
        --v=2 \
        --feature-gates=EphemeralContainers=true  # 开启临时容器
        --logtostderr=true \
        --address=127.0.0.1 \
        --root-ca-file=/etc/kubernetes/pki/ca.pem \
        --cluster-signing-cert-file=/etc/kubernetes/pki/ca.pem \
        --cluster-signing-key-file=/etc/kubernetes/pki/ca-key.pem \
        --service-account-private-key-file=/etc/kubernetes/pki/sa.key \
        --kubeconfig=/etc/kubernetes/controller-manager.kubeconfig \
        --leader-elect=true \
        --use-service-account-credentials=true \
        --node-monitor-grace-period=40s \
        --node-monitor-period=5s \
        --pod-eviction-timeout=2m0s \
        --controllers=*,bootstrapsigner,tokencleaner \
        --allocate-node-cidrs=true \
        --cluster-cidr=172.16.0.0/12 \
        --requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.pem \
        --node-cidr-mask-size=24
        
  Restart=always
RestartSec=10s
  
  [Install]
  WantedBy=multi-user.target  
  ```


# 2. 启动服务

* 启动服务

  ```shell
  systemctl daemon-reload
  systemctl enable --now kube-controller-manager
  ```

* 检查验证

  ```shell
  systemctl  status kube-controller-manager
  tail -f /var/log/messages
  ```

  
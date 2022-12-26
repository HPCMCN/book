# 1. 配置文件

## 1.1 构建配置信息

* 创建服务

  ```shell
  kubectl -n kube-system create serviceaccount kube-proxy
  kubectl create clusterrolebinding system:kube-proxy   --clusterrole system:node-proxier         --serviceaccount kube-system:kube-proxy
  ```

* 将证书导入配置

  ```shell
  SECRET=$(kubectl -n kube-system get sa/kube-proxy \
      --output=jsonpath='{.secrets[0].name}')
  
  JWT_TOKEN=$(kubectl -n kube-system get secret/$SECRET \
  --output=jsonpath='{.data.token}' | base64 -d)
  
  PKI_DIR=/etc/kubernetes/pki
  K8S_DIR=/etc/kubernetes
  
  # 此处的server为apiserver, 应该是vip地址
  kubectl config set-cluster kubernetes     --certificate-authority=/etc/kubernetes/pki/ca.pem     --embed-certs=true     --server=https://10.111.0.111:16443     --kubeconfig=${K8S_DIR}/kube-proxy.kubeconfig
  
  kubectl config set-credentials kubernetes     --token=${JWT_TOKEN}     --kubeconfig=/etc/kubernetes/kube-proxy.kubeconfig
  
  kubectl config set-context kubernetes     --cluster=kubernetes     --user=kubernetes     --kubeconfig=/etc/kubernetes/kube-proxy.kubeconfig
  
  kubectl config use-context kubernetes     --kubeconfig=/etc/kubernetes/kube-proxy.kubeconfig
  ```

## 1.2 同步

* 将配置发送到其他节点

  ```shell
  MasterNodes='master02 master03'
  WorkNodes='node01 node02'
  
  for NODE in $MasterNodes; do
       scp /etc/kubernetes/kube-proxy.kubeconfig  $NODE:/etc/kubernetes/kube-proxy.kubeconfig
   done
  
  for NODE in $WorkNodes; do
       scp /etc/kubernetes/kube-proxy.kubeconfig $NODE:/etc/kubernetes/kube-proxy.kubeconfig
   done
  
  ```

* 全部节点

  ```shell
  # /usr/lib/systemd/system/kube-proxy.service
  [Unit]
  Description=Kubernetes Kube Proxy
  Documentation=https://github.com/kubernetes/kubernetes
  After=network.target
  
  [Service]
  ExecStart=/usr/local/bin/kube-proxy \
    --config=/etc/kubernetes/kube-proxy.yaml \
    --feature-gates=EphemeralContainers=true  # 开启临时容器
    --v=2
  
  Restart=always
  RestartSec=10s
  
  [Install]
  WantedBy=multi-user.target
  
  ```
  
* 配置yaml文件

  ```shell
  # /etc/kubernetes/kube-proxy.yaml
  apiVersion: kubeproxy.config.k8s.io/v1alpha1
  bindAddress: 0.0.0.0
  featureGates:  # 开启临时容器
    EphemeralContainers: true
  clientConnection:
    acceptContentTypes: ""
    burst: 10
    contentType: application/vnd.kubernetes.protobuf
    kubeconfig: /etc/kubernetes/kube-proxy.kubeconfig
    qps: 5
  clusterCIDR: 172.168.0.0/12   # 自己Pod网段
  configSyncPeriod: 15m0s
  conntrack:
    max: null
    maxPerCore: 32768
    min: 131072
    tcpCloseWaitTimeout: 1h0m0s
    tcpEstablishedTimeout: 24h0m0s
  enableProfiling: false
  healthzBindAddress: 0.0.0.0:10256
  hostnameOverride: ""
  iptables:
    masqueradeAll: false
    masqueradeBit: 14
    minSyncPeriod: 0s
    syncPeriod: 30s
  ipvs:
    masqueradeAll: true
    minSyncPeriod: 5s
    scheduler: "rr"
    syncPeriod: 30s
  kind: KubeProxyConfiguration
  metricsBindAddress: 127.0.0.1:10249
  mode: "ipvs"
  nodePortAddresses: null
  oomScoreAdj: -999
  portRange: ""
  udpIdleTimeout: 250ms
  ```

# 2. 启动

* 启动组建

  ```shell
  systemctl daemon-reload
  systemctl enable --now kube-proxy
  ```

* 检查

  ```shell
  tail -f /var/log/messages
  kubectl get svc
  ```

  ![image-20221117162225014](.image/10-kube-porxy%E5%AE%89%E8%A3%85/image-20221117162225014.png)
# 1. 配置文件

全部节点都执行

## 1.1 启动配置

* 配置kubelet.service

  ```shell
  # 所有节点
  vim  /usr/lib/systemd/system/kubelet.service
  
  [Unit]
  Description=Kubernetes Kubelet
  Documentation=https://github.com/kubernetes/kubernetes
  
  [Service]
  ExecStart=/usr/local/bin/kubelet
  
  Restart=always
  StartLimitInterval=0
  RestartSec=10
  
  [Install]
  WantedBy=multi-user.target
  ```

## 1.2 配置文件

所有节点, 二选一即可

### 1.2.1 主配置文件

* Runtime为Containerd

  ```shell
  # /etc/systemd/system/kubelet.service.d/10-kubelet.conf
  # 注意: Runtime为Containerd 的配置
  [Service]
  Environment="KUBELET_KUBECONFIG_ARGS=--bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.kubeconfig --kubeconfig=/etc/kubernetes/admin.kubeconfig"
  Environment="KUBELET_SYSTEM_ARGS=--network-plugin=cni --cni-conf-dir=/etc/cni/net.d --cni-bin-dir=/opt/cni/bin --container-runtime=remote --runtime-request-timeout=15m --container-runtime-endpoint=unix:///run/containerd/containerd.sock --cgroup-driver=systemd"
  Environment="KUBELET_CONFIG_ARGS=--config=/etc/kubernetes/kubelet-conf.yml"
  Environment="KUBELET_EXTRA_ARGS=--node-labels=node.kubernetes.io/node='' "
  ExecStart=
  ExecStart=/usr/local/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_SYSTEM_ARGS $KUBELET_EXTRA_ARGS
  ```
  
* Runtime为Docker

  ```shell
  # /etc/systemd/system/kubelet.service.d/10-kubelet.conf
  # 注意: Runtime为Docker 的配置
  [Service]
  Environment="KUBELET_KUBECONFIG_ARGS=--bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.kubeconfig --kubeconfig=/etc/kubernetes/admin.kubeconfig"
  Environment="KUBELET_SYSTEM_ARGS=--network-plugin=cni --cni-conf-dir=/etc/cni/net.d --cni-bin-dir=/opt/cni/bin"
  Environment="KUBELET_CONFIG_ARGS=--config=/etc/kubernetes/kubelet-conf.yml --pod-infra-container-image=registry.cn-hangzhou.aliyuncs.com/google_containers/pause:3.5"
  Environment="KUBELET_EXTRA_ARGS=--node-labels=node.kubernetes.io/node='' "
  ExecStart=
  ExecStart=/usr/local/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_SYSTEM_ARGS $KUBELET_EXTRA_ARGS
  ```

### 1.2.2 二级配置文件

* 启动加载配置文件

  ```shell
  # /etc/kubernetes/kubelet-conf.yml
  # 注意clusterDNS的ip为Server网段的第十个ip
  apiVersion: kubelet.config.k8s.io/v1beta1
  kind: KubeletConfiguration
  address: 0.0.0.0
  port: 10250
  readOnlyPort: 10255
  authentication:
    anonymous:
      enabled: false
    webhook:
      cacheTTL: 2m0s
      enabled: true
    x509:
      clientCAFile: /etc/kubernetes/pki/ca.pem
  authorization:
    mode: Webhook
    webhook:
      cacheAuthorizedTTL: 5m0s
      cacheUnauthorizedTTL: 30s
  cgroupDriver: systemd
  cgroupsPerQOS: true
  clusterDNS:
  - 10.0.0.10
  clusterDomain: cluster.local
  containerLogMaxFiles: 5
  containerLogMaxSize: 10Mi
  contentType: application/vnd.kubernetes.protobuf
  cpuCFSQuota: true
  cpuManagerPolicy: none
  cpuManagerReconcilePeriod: 10s
  enableControllerAttachDetach: true
  enableDebuggingHandlers: true
  enforceNodeAllocatable:
  - pods
  eventBurst: 10
  eventRecordQPS: 5
  evictionHard:
    imagefs.available: 15%
    memory.available: 100Mi
    nodefs.available: 10%
    nodefs.inodesFree: 5%
  evictionPressureTransitionPeriod: 5m0s
  failSwapOn: true
  fileCheckFrequency: 20s
  hairpinMode: promiscuous-bridge
  healthzBindAddress: 127.0.0.1
  healthzPort: 10248
  httpCheckFrequency: 20s
  imageGCHighThresholdPercent: 85
  imageGCLowThresholdPercent: 80
  imageMinimumGCAge: 2m0s
  iptablesDropBit: 15
  iptablesMasqueradeBit: 14
  kubeAPIBurst: 10
  kubeAPIQPS: 5
  makeIPTablesUtilChains: true
  maxOpenFiles: 1000000
  maxPods: 110
  nodeStatusUpdateFrequency: 10s
  oomScoreAdj: -999
  podPidsLimit: -1
  registryBurst: 10
  registryPullQPS: 5
  resolvConf: /etc/resolv.conf
  rotateCertificates: true
  runtimeRequestTimeout: 2m0s
  serializeImagePulls: true
  staticPodPath: /etc/kubernetes/manifests
  streamingConnectionIdleTimeout: 4h0m0s
  syncFrequency: 1m0s
  volumeStatsAggPeriod: 1m0s
  ```

# 2. 启动

* 启动服务

  ```shell
  systemctl daemon-reload
  systemctl enable --now kubelet
  ```
  
* 检查测试

  ```shell
  systemctl status kubelet
  
  kubectl get node
  tail -f /var/log/messages
  # 这里会提示CNI not initalezed和not Read问题
  ```
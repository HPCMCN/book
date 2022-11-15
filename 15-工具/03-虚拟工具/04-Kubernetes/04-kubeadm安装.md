# 1. 安装

## 1.1 kubeadm安装

* 配置镜像源

  ```shell
  cat <<EOF > /etc/yum.repos.d/kubernetes.repo
  [kubernetes]
  name=Kubernetes Repository
  baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
  enabled=1
  gpgcheck=0
  EOF
  ```

* 安装kubeadm组建

  ```shell
  # 查看所有版本信息
  yum list kubeadm.x86_64 --showduplicates | sort -r
  
  # 安装指定版本, 并忽略k8s安装, 直接安装需要修改大量配置, 这里直接手动安装
  yum install -y kubeadm-1.20* kubelet-1.20* kubectl-1.20* --disableexcludes=kubernetes
  
  # 卸载
  # yum remove -y kubeadm-1.20* kubelet-1.20* kubectl-1.20*
  ```
  
* k8s的驱动变更

  此操作包含两个步骤: 

  1. 配置diver, 与docker保持一致
  2. 配置镜像源

  ```shell
  cat >/etc/sysconfig/kubelet<<EOF
  KUBELET_EXTRA_ARGS="--cgroup-driver=systemd --pod-infra-container-image=registry.cn-hangzhou.aliyuncs.com/google_containers/pause-amd64:3.2"
  EOF
  ```

* 刷新环境

  ```shell
  systemctl daemon-reload && systemctl daemon-reload
  systemctl enable docker && systemctl start docker
  ```

## 1.2 K8s环境搭建

* 生成k8s配置文件

  ```shell
  kubeadm config print init-defaults > master-k8s.yaml
  # vi master-k8s.yaml, 直接使用以下数据即可
  
  apiVersion: kubeadm.k8s.io/v1beta2
  bootstrapTokens:
  - groups:
    - system:bootstrappers:kubeadm:default-node-token
    token: 7t2weq.bjbawausm0jaxury
    ttl: 24h0m0s
    usages:
    - signing
    - authentication
  kind: InitConfiguration
  localAPIEndpoint:
    advertiseAddress: 10.111.0.10
    bindPort: 6443
  nodeRegistration:
    criSocket: /var/run/dockershim.sock
    name: master01
    taints:
    - effect: NoSchedule
      key: node-role.kubernetes.io/master
  ---
  apiServer:
    certSANs:
    - 10.111.0.111
    timeoutForControlPlane: 4m0s
  apiVersion: kubeadm.k8s.io/v1beta2
  certificatesDir: /etc/kubernetes/pki
  clusterName: kubernetes
  controlPlaneEndpoint: 10.111.0.111:16443
  controllerManager: {}
  dns:
    type: CoreDNS
  etcd:
    local:
      dataDir: /var/lib/etcd
  imageRepository: registry.cn-hangzhou.aliyuncs.com/google_containers
  kind: ClusterConfiguration
  kubernetesVersion: v1.20.0
  networking:
    dnsDomain: cluster.local
    podSubnet: 172.168.0.0/12
    serviceSubnet: 10.0.0.0/12
  scheduler: {}
  ```

* yaml语法校验更新

  ```shell
   # 为防止此语法, 或者版本老旧问题, 使用自带命令进行更新, 将新文件同步到其他机器上
  kubeadm config migrate --old-config master-k8s.yaml --new-config new.yaml
  rm -f master-k8s.yaml
  mv new.yaml master-k8s.yaml
  ```
  
* 下载k8s镜像

  ```shell
  kubeadm config images pull --config=master-k8s.yaml
  # 如果拉取失败可以直接使用docker拉取
  # vim images.sh
  # -----------------------------------
  #!/bin/bash
  url=registry.cn-hangzhou.aliyuncs.com/google_containers
  version=v1.20.0
  images=(`kubeadm config images list --kubernetes-version=$version|awk -F '/' '{print $2}'`)
  for imagename in ${images[@]} ; do
    docker pull $url/$imagename
    #docker tag $url/$imagename k8s.gcr.io/$imagename
    #docker rmi -f $url/$imagename
  done
  # -----------------------------------
  # 注意如果失败, 需要重置后才能重新初始化
  kubeadm reset -f ; ipvsadm --clear  ; rm -rf ~/.kube
  ```

## 1.3 安装master

* 安装master节点

  ```shell
  systemctl enable kubelet && systemctl start kubelet
  kubeadm init --config=master-k8s.yaml --upload-certs
  # 注意: 如果中途失败, 调整问题后, 请执行: kubeadm reset 再重试
  # 结束后, 根据提示命令, 修改配置(没有的话就不用管了)
  #mkdir -p $HOME/.kube
  #cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  #chown $(id -u):$(id -g) $HOME/.kube/config
  
  # 输出结果将会有两种join
  # 此节点为master节点加入操作
  1.  kubeadm join xx --token xx
      --discovery-token-ca-cert-hash xx
      --control-plane --certificate-key xx
      
  # 此节点为node加入操作
  2. kubeadm join 10.111.0.111:16443 --token xxx
      --discovery-token-ca-cert-hash xxx
  ```
  
  ![image-20221114155816959](.image/03-%E5%AE%89%E8%A3%85/image-20221114155816959.png)
  
* 生成token

  由于token时效只有24h, 过期后需要重新生成

  ```shell
  # 将主节点的输出结果复制到node/master执行即可, 如果过期, 则需要如下操作
  # 1. 生成token
  kubeadm token create --print-join-command
  ```

* 配置master环境变量

  ```shell
  cat <<EOF >> /root/.bashrc
  export KUBECONFIG=/etc/kubernetes/admin.conf
  EOF
  source /root/.bashrc
  ```

* 检测节点运行状态

  ```shell
  kubectl get nodes
  kubectl get pods -n kube-system -o wide
  ```

## 1.4 安装Node

* 在node节点上先把步骤1, 2执行一遍

* 启动kubelet

  ```shell
  systemctl enable kubelet && systemctl start kubelet
  ```

* 方式一: 直接加入

  ```shell
  kubeadm join 10.111.0.111:16443 --token xxx --discovery-token-ca-cert-hash xxx
  ```

* 方式二: 配置文件, 编辑如下

  ```yaml
  # kubeadm config print init-default > node-k8s.yaml
  # vi node-k8s.yaml, 设置为如下信息
  apiVersion: kubeadm.k8s.io/v1beata1
  kind: JoinConfiguration
  discovery:
    bootstrapToken:
      apiServerEndpoint: 10.111.0.11:6443  # 上面分配的endpoint
      token: o7v3vh.nr8w04ghaepmq1my  # 上面分配的token
      unsafeSkipCAVerfication: true
    tilBootstrapToken: o7v3vh.nr8w04ghaepmq1my # 还是token
    
  # 然后直接执行:
  kubeadm join --config=node-k8s.yaml
  ```

# 2. 验证集群

* 查看pod(确定每个Pod都正常运行)

  ```shell
  kubectl get pods --all-namespaces
  ```


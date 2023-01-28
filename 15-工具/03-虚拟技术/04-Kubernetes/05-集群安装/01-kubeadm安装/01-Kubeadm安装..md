本教程采用kubeadm1.23.x版本搭建.

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
  yum install -y kubeadm-1.23* kubelet-1.23* kubectl-1.23* --disableexcludes=kubernetes
  
  # 卸载
  # yum remove -y kubeadm-1.23* kubelet-1.23* kubectl-1.23*
  ```
  
* 指定Containerd的sock位置(**使用docker的话, 不用执行**)

  ```shell
  cat >/etc/sysconfig/kubelet<<EOF
  KUBELET_KUBEADM_ARGS="--container-runtime=remote --runtime-request-timeout=15m --container-runtime-endpoint=unix:///run/containerd/containerd.sock"
  EOF
  ```

* 刷新环境

  ```shell
  systemctl daemon-reload
  systemctl enable --now kubelet
  ```

## [高可用安装](..\..\..\..\01-代理\03-高可用\01-LVS\02-高可用安装.md) 

不需要的话可以直接跳过
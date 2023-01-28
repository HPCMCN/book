# 1. 选型

如果K8s>1.24, 那么需要采用Container作为Runtime, 小于1.24两者均可.

以下安装方式选择一个即可

# 2. 安装

## 2.1 Containerd

**注意**: 不用启用docker, 这里同样使用了docker, 原因如下:

* docker安装会携带Containerd一起安装, 不用单独安装来调配环境, 相对简单
* 平时测试, docker使用相对方便一些

### 安装流程

* 配置加载模块

  ```shell
  cat <<EOF | sudo tee /etc/modules-load.d/containerd.conf
  overlay
  br_netfilter
  EOF
  ```

* 加载模块

  ```shell
  modprobe -- overlay
  modprobe -- br_netfilter
  ```

* 配置内核

  ```shell
  cat <<EOF | sudo tee /etc/sysctl.d/99-kubernetes-cri.conf
  net.bridge.bridge-nf-call-iptables  = 1
  net.ipv4.ip_forward                 = 1
  net.bridge.bridge-nf-call-ip6tables = 1
  EOF
  ```

* 加载内核

  ```shell
  sysctl --system
  ```

* 创建配置文件

  ```shell
  mkdir -p /etc/containerd
  containerd config default | tee /etc/containerd/config.toml
  ```

* 修改Cgroup为Systemd

  ```shell
  vim /etc/containerd/config.toml
  # containerd.runtimes.runc.options，添加或修改SystemdCgroup = true
  # sandbox_image 修改为: registry.cn-hangzhou.aliyuncs.com/google_containers/pause:3.6
  ```

* 刷新配置

  ```shell
  systemctl daemon-reload
  systemctl enable --now containerd
  ```

* 配置socket文件

  ```shell
  cat > /etc/crictl.yaml <<EOF
  runtime-endpoint: unix:///run/containerd/containerd.sock
  image-endpoint: unix:///run/containerd/containerd.sock
  timeout: 10
  debug: false
  EOF
  ```

## 2.2 Docker

docker安装极为简单

* 修改配置

  ```shell
  mkdir /etc/docker
  cat > /etc/docker/daemon.json <<EOF
  {
    "exec-opts": ["native.cgroupdriver=systemd"],
    "registry-mirrors": ["https://geqyx8d1.mirror.aliyuncs.com"]
  }
  EOF
  ```

* 启用docker

  ```shell
  systemctl daemon-reload && systemctl enable --now docker
  ```

  
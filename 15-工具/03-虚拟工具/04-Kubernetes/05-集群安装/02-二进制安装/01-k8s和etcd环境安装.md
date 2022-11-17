现在一个节点上安装, 安装完成后, 发送到其他节点

* 搞错后清理

  ```shell
  rm -rf /usr/local/bin/etcd*
  rm -rf /usr/local/bin/kube*
  rm -rf /opt/cni/bin
  rm -rf /etc/etcd/ssl 
  rm -rf /etc/kubernetes/pki
  ```

* 资源下载

  ```shell
  https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.23.md
  #kubernetes-server-linux-amd64.tar.gz
  
  https://github.com/etcd-io/etcd/releases/tag/v3.5.1
  #etcd-v3.5.1-linux-amd64.tar.gz
  ```

* k8s安装

  ```shell
  tar -zxf kubernetes-server-linux-amd64.tar.gz  --strip-components=3 -C /usr/local/bin kubernetes/server/bin/kube{let,ctl,-apiserver,-controller-manager,-scheduler,-proxy}
  ```

* etcd安装

  ```shell
  tar -zxf etcd-v3.5.1-linux-amd64.tar.gz --strip-components=1 -C /usr/local/bin etcd-v3.5.1-linux-amd64/etcd{,ctl}
  ```

* 将安装信息发送到其他节点

  ```shell
  MasterNodes='master02 master03'
  WorkNodes='node01 node02'
  for NODE in $MasterNodes; do echo $NODE; scp /usr/local/bin/kube{let,ctl,-apiserver,-controller-manager,-scheduler,-proxy} $NODE:/usr/local/bin/; scp /usr/local/bin/etcd* $NODE:/usr/local/bin/; done
  
  for NODE in $WorkNodes; do     scp /usr/local/bin/kube{let,-proxy} $NODE:/usr/local/bin/ ; done
  ```

* 所有节点创建下面目录

  ```shell
  mkdir -p /opt/cni/bin
  
  kubelet --version
  etcdctl version
  ```

  


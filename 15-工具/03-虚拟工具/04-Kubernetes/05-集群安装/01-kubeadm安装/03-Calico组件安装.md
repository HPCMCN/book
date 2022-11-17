#### 安装流程

只需要在**master01**上面执行即可

* [配置文件](../../.image/07-Calico%E7%BB%84%E4%BB%B6%E5%AE%89%E8%A3%85/calico.yaml)

* 修改配置

  ```shell
  # 将master节点上的Pod网段信息读取出来
  POD_SUBNET=`cat /etc/kubernetes/manifests/kube-controller-manager.yaml | grep cluster-cidr= | awk -F= '{print $NF}'`
  
  # 修改网段信息
  sed -i "s#POD_CIDR#${POD_SUBNET}#g" calico.yaml
  ```

* 插件安装

  ```shell
  kubectl apply -f calico.yaml
  ```

* 查看安装进度

  ```shell
  # 这个阶段等待时间挺长的, 耐心等待一下
  kubectl get po -n kube-system
  ```

  ![image-20221115173839484](../../.image/07-Calico%E7%BB%84%E4%BB%B6%E5%AE%89%E8%A3%85/image-20221115173839484.png)

* 查看当前各节点状态

  ```shell
  kubectl get nodes
  # 已经Ready了
  ```

  ![image-20221115174052079](../../.image/07-Calico%E7%BB%84%E4%BB%B6%E5%AE%89%E8%A3%85/image-20221115174052079.png)
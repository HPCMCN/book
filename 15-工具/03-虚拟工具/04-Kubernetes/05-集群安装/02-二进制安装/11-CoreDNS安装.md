* 获取kubelet当时配置的DNS的ip

  ```shell
  COREDNS_SERVICE_IP=`kubectl get svc | grep kubernetes | awk '{print $3}'`0
  ```

* [下载配置](.image/12-CoreDNS%E5%AE%89%E8%A3%85/coredns.yaml)

  ```shell
  # 将DNS地址修改为设置的地址
  sed -i "s#KUBEDNS_SERVICE_IP#${COREDNS_SERVICE_IP}#g" coredns.yaml
  ```

* 安装

  ```shell
  kubectl  create -f coredns.yaml
  ```

* 查看校验

  ```shell
  kubectl get po -n kube-system
  ```

  


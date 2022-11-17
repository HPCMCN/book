* [下载配置文件](.image/10-%E9%85%8D%E7%BD%AEkube-proxy/calico.yaml)

  修改对应网段为自己的Pod网段

  ```shell
  sed -i "s#POD_CIDR#172.168.0.0/12#g" calico.yaml
  
  # 检查一下:
  grep "IPV4POOL_CIDR" calico.yaml  -A 1
  ```
  
* 安装calico

  ```shell
  kubectl apply -f calico.yaml
  ```

* 校验验证

  ```shell
  kubectl get po -n kube-system
  ```

  


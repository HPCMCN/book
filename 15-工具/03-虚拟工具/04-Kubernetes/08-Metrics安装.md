* 先将证书从master同步到node节点上

  master已经自动同步了

  ```shell
  for i in node01 node02;do scp /etc/kubernetes/pki/front-proxy-ca.crt $i:/etc/kubernetes/pki/front-proxy-ca.crt;done
  ```

* [配置文件](.image/08-Metrics%E5%AE%89%E8%A3%85/comp.yaml)

* 安装metrices

  ```shell
  ls kubeadm-metrics-server
  # comp.yaml
  kubectl apply -f kubeadm-metrics-server/
  ```

* 查看安装情况

  ```shell
  kubectl get po -n kube-system -o wide
  # 它会随机部署在node节点上
  ```

  ![image-20221115180325752](.image/08-Metrics%E5%AE%89%E8%A3%85/image-20221115180325752.png)

* 测试并使用

  ```shell
  kubectl top node
  kubectl top po -A
  ```

  ![image-20221115180440031](.image/08-Metrics%E5%AE%89%E8%A3%85/image-20221115180440031.png)
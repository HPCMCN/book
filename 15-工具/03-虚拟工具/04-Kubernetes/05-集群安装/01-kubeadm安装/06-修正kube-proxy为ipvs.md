默认代理使用iptables, 需要修改为ipvs.

* 查看当前代理

  ```shell
  curl 127.0.0.1:10249/proxyMode
  ```

* 修改代理模式

  ```shell
  kubectl edit cm kube-proxy -n kube-system
  # 搜索mode, 默认是空, 就是iptables, 改成ipvs
  ```

* 更新生效

  ```shell
  kubectl patch daemonset kube-proxy -p "{\"spec\":{\"template\":{\"metadata\":{\"annotations\":{\"date\":\"`date +'%s'`\"}}}}}" -n kube-system
  ```

* 校验

  ```shell
  kubectl get pod -n kube-system
  # 此时pod会重启, 等重启完成后, 模式将会被修改
  curl 127.0.0.1:10249/proxyMode
  ```

  
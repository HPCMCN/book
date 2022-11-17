* [下载配置](.image/14-%E5%AE%89%E8%A3%85dashboard/dashboard.tar.gz)

* 安装

  ```shell
  kubectl  create -f .
  ```

* 测试校验

  ```shell
  kubectl get po -n kubernetes-dashboard
  kubectl get svc -n kubernetes-dashboard
  
  https://10.111.0.10:32198/#/login
  # 具体登录操作参见 kubeadm安装教程
  ```

  


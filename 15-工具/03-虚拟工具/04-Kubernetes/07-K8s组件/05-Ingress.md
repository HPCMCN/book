# 1. Ingress

## 1.1 简介

k8s集群的服务入口

* 提供负载均衡
* SSL终止
* 域名管理
* 灰度发布等

## 1.2 安装

官方安装文档: https://kubernetes.github.io/ingress-nginx/deploy/#bare-metal-clusters

* 下载对应yaml

* 创建安装

  ```shell
  kubectl create -f ingress.yaml
  ```

* 检查

  ```shell
  # 确保controller可用即可
  kubectl get pod -n ingress-nginx
  
  # kubectl get ingress
  
  # 在k8s集群外部DNS解析, 配置到/etc/hosts中
  10.111.0.11	nginx.test.com
  ```

  ![image-20221220222415584](.image/05-Ingress/image-20221220222415584.png)

* 检测

  ```shell
  # 查看映射出来的端口
  kubectl get svc -n ingress-nginx
  
  # 在k8s集群外部访问此域名
  curl nginx.test.com:31898
  ```

* 原理

  1. 外部hosts文件解析后, 请求`ingress-nginx`

  2. `ingress-nginx`收到请求, 利用`nginx`转发到`svc`上

     ```shell
     kubectl exec -it ingress-nginx-controller-bdc4b7d6b-ncxm2 -n ingress-nginx -- bash -c 'grep -A 20 "nginx.test.com" nginx.conf'
     ```

  3. `svc`将会利用k8sDNS特征访问到对应的`pod`中
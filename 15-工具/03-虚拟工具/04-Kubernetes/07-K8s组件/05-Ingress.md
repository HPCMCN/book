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

  
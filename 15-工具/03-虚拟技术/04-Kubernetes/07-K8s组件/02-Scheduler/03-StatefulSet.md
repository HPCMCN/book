# 1. StatefulSet

## 1.1 简介

* 有状态服务部署(有序的部署, 拓展, 滚动更新)
* 持久化数据
* 提供独一无二的网络标识


## 1.2 创建

K8s官网: [点击跳转](https://kubernetes.io/zh-cn/docs/tutorials/stateful-application/basic-stateful-set/)

* 基本yaml

  ```shell
  apiVersion: v1
  kind: Service
  metadata:
    name: nginx
    labels:
      app: nginx
  spec:
    ports:
    - port: 80
      name: web
    clusterIP: None
    selector:
      app: nginx
  ---
  apiVersion: apps/v1
  kind: StatefulSet
  metadata:
    name: web
  spec:
    serviceName: "nginx"
    replicas: 2
    selector:
      matchLabels:
        app: nginx
    template:
      metadata:
        labels:
          app: nginx
      spec:
        containers:
        - name: nginx
          image: nginx
          ports:
          - containerPort: 80
            name: web
  ```

* 部署

  ```shell
  kubectl create -f statefulset.yaml
  
  # 循环检测创建流程
  kubectl get pod -w
  
  # 查看镜像
  kubectl get pod -l app=nginx -oyaml | grep image:
  ```

* 修改

  ```shell
  # 增加副本数量
  kubectl scale sts web --replicas=5
  
  # 动态查看
  kubectl get pods -w -l app=nginx
  
  # json模式修改副本
  kubectl patch sts web -p '{}"spec": {"replicas": 5}}'
  ```

  

# 2. 命令

#### spec.updateStrategy.Type

* RollingUpdate

  滚动更新, 采用序列更新, 删除时候按照倒序删除.

  * spec.updateStrategy.RollingUpdate.papartition

    滚动分区更新, 更新时候, 当标识大于这个数字时才会更新, 否则引用原来的镜像.

* OnDelete

  手动删除更新, 手动删除Pod, 才能创建新的Pod, 1.7版本之前默认值


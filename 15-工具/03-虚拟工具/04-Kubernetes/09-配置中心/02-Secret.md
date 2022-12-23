# 1. Secret

软加密, 使用base64进行加密, 整体用法类似ConfigMap

## 1.1 使用

* 设置账号密码

  ```yaml
  echo "admin" > secert/username.txt
  echo "password" > secert/password.txt
  ```

* 创建

  ```shell
  # generic: 类型
  kubectl create secret generic secret-file --from-file=secert/
  ```

* 查看

  ```shell
  # 查看
  kubectl get secret secret-file -oyaml
  
  # 源数据查看(解码)
  kubectl get secret db-user-pass -oyaml | grep password | awk '{print $NF}' | base64 -d
  ```

## 1.2 命令

```shell
kubectl create secret generic secret-name [OPTIONS]
```

* --from-file: 添加配置文件或者文件夹

  ```shell
  --from-file=conf/ --from-file=conf/a.conf
  --from-file=abc=conf/a.conf
  ```

* --from-env-file: 直接导入文件中的变量

  ```shell
  --from-env-file=game.conf
  ```

* --from-literal: 直接导入变量

  ```shell
  # 变量: {"level": "INFO"}
  --from-literal=level=INFO
  ```

# 2. yaml

## 2.1 generic

### 2.1.1 手动加密

* yaml

  ```yaml
  apiVersion: v1
  data:  # 密文数据
    password: cGFzc3dvcmQK  # base64编码
    username: YWRtaW4K  # base64编码
  kind: Secret
  metadata:
    name: db-user-pass
  type: Opaque  # 加密类型
  ```

### 2.1.2 自动加密

* yaml

  ```yaml
  apiVersion: v1
  StringData:  # 明文数据, 会自动加密
    password: cGFzc3dvcmQK
    username: YWRtaW4K
  kind: Secret
  metadata:
    name: db-user-pass
  type: Opaque  # 加密类型
  ```

## 2.2 docker-registry

私有仓库镜像拉取

### 2.2.1 aliyun使用镜像仓库

按照对应要求配置即可: https://cr.console.aliyun.com/repository/cn-hangzhou/hpcm

* 打包镜像

  ```shell
  docker tag 88736fe82739 registry.cn-hangzhou.aliyuncs.com/hpcm/repo:v1.0.0
  ```

* 登录仓库

  ```shell
  docker login --username=56***31@qq.com registry.cn-hangzhou.aliyuncs.com
  ```

* 上传镜像

  ```shell
  docker push registry.cn-hangzhou.aliyuncs.com/hpcm/repo:v1.0.0
  ```

* 拉取镜像

  ```shell
  docker pull registry.cn-hangzhou.aliyuncs.com/hpcm/repo:v1.0.0
  ```

### 2.2.2 登录拉取镜像

* 配置docker源账号密码信息

  ```shell
  # 创建一个
  # 类型为: docker-registry
  # name: docker-secret 的secret
  kubectl create secret docker-registry docker-secret --docker-username=56***1@qq.com --docker-password='ab***1' --docker-email=h***m@foxmail.com --docker-server=registry.cn-hangzhou.aliyuncs.com 
  ```

* yaml

  ```yaml
  # secret-aliyun.yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    labels:
      app: secret-deploy
    name: secret-deploy
  spec:
    replicas: 1
    selector:
      matchLabels:
        app: secret-deploy
    template:
      metadata:
        labels:
          app: secret-deploy
      spec:
        imagePullSecrets:
          - name: docker-secret  # 指定上面的secret的name
        containers:
        - image: nginx
          name: nginx
  ```

* 创建

  ```shell
  kubectl create -f secret-aliyun.yaml
  ```

* 检查

  ```shell
  # 查看pod是否创建完成
  kubectl get pod
  ```


## 2.3 tls

### 2.3.1 证书创建

生产模式中建议使用购买的证书

* 创建证书

  ```shell
  openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=test.com"
  ```

### 2.3.2 使用

* 创建证书配置

  ```shell
  # 创建一个类型为tls, 名字为test_tls的配置
  kubectl -n default create secret tls test_tls --key=tls.key --cert=tls.crt
  ```

* 使用

  ```yaml
  # 正常来说, ingress不会暴露在外, 所以一般证书是放在slb之前
  apiVersion: networking.k8s.io/v1beta1
  kind: Ingress
  metadata:
    name: nginx-https-test
    namespace: default
    annotations:
      kubernetes.io/ingress.class: "nginx"
  spec:
    rules:
    - host: test.com
      http:
        paths:
        - backend:
            serviceName: nginx-svc
            servicePort: 80
    tls:
     - secretName: test-tls
  ```

  


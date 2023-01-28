# 1. Volume

## 1.1 介绍

## 1.2 使用

# 2. 配置

## 2.1 emptyDir

共享文件, 同一个Pod中的文件共享

* yaml

  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    labels:
      app: nginx-deploy
    name: nginx-deployment
  spec:
    replicas: 1
    selector:
      matchLabels:
        app: nginx
    strategy:
      type: Recreate
    template:
      metadata:
        labels:
          app: nginx
      spec:
        containers:
          - image: nginx
            name: nginx1
            volumeMounts:
              - mountPath: /opt
                name: share-volume
          - image: nginx
            name: nginx2
            command:
              - sh
              - -c
              - sleep 3600;
            volumeMounts:
              - mountPath: /mnt
                name: share-volume
        volumes:
          - name: share-volume
            emptyDir: {}
              # medium: Memory  # 使用内存, 设置的大小会被计入到 Container 的内存限制当中
  ```

* 验证

  ```shell
  # 在nginx1中创建一个文件
  kubectl exec nginx-deployment-747fb5d5f8-5tkvm -c nginx1 -- bash -c 'echo abc > /opt/111'
  
  # 在nginx2中查看
  kubectl exec nginx-deployment-747fb5d5f8-5tkvm -c nginx2 -- bash -c 'cat /mnt/111'
  ```

## 2.2 hostPath

* yaml

  ```yaml
      spec:
        containers:
          - image: nginx
            name: nginx1
            volumeMounts:
              - mountPath: /etc/timezone
                name: timezone
        volumes:
          - name: timezone
            hostPath:
              path: /etc/timezone
              type: File
  ```

  type类型如下

  * 空: 默认选项, 不检查挂载信息
  * Directory: 挂载目录, 此目录必须存在, 否则报错
  * File: 挂载文件, 此文件必须存在, 否则报错
  * DirectoryOrCreate: 挂载目录, 如果目录不存在, 则自动创建
  * FileOrCreate: 挂载文件, 如果文件不存在, 则自动创建

  * Socket: UNIX套接字, 必须存在
  * CharDevice: 字符设备, 必须存在
  * BlockDevice: 块设备, 必须存在

## 2.3 NFS

### 2.3.1 NFS 服务搭建

* 安装

  ```shell
  # 其他节点也需要安装, 不用启动
  yum install -y nfs-utils
  ```

* 配置

  ```shell
  systemctl start nfs
  cat > /etc/exports << EOF
  /data/nfs 10.111.0.0/24(rw,no_root_squash,sync)
  EOF
  ```

* 重载生效

  ```shell
  exportfs -r
  systemctl reload nfs
  ```

* 本地测试生效

  ```shell
  mount -t nfs 10.111.0.10:/data/nfs /mnt
  # touch /mnt/111
  # ls /data/nfs
  ```

### 2.3.1 yaml

* yaml

  ```yaml
      spec:
        containers:
          - image: nginx
            name: nginx1
            volumeMounts:
              - mountPath: /opt
                name: name-nfs
        volumes:
          - name: name-nfs
            nfs:
              server: 10.111.0.10
              path: /data/nfs/k8s-test
  ```

* 测试

  ```shell
  # container内部创建文件
  kubectl exec -it nginx-deployment-54c7575555-sbl4v -- bash -c 'echo 12345 > /opt/abc'
  
  # nfs检测
  cat /data/nfs/k8s-test/abc
  ```
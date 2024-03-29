# 1. ConfigMap

## 1.1 常见用法

* yaml构建

  一般配置较多, 直接用yaml输入较为麻烦, 所以直接在文件中存入变量, 然后导入生成yaml即可

  ```shell
  # 导入文件夹
  kubectl create configmap cnfromfile --from-file=./conf/ --dry-run -oyaml > cm.yaml
  # 导入文件
  kubectl create configmap cnfromfile --from-file=./conf/game.conf --from-file=./conf/game1.conf --dry-run -oyaml > cm.yaml
  ```

* 创建

  ```shell
  kubectl create -f cm.yaml
  ```

* 查看

  ```shell
  kubectl get cm
  ```

## 1.2 命令

### 1.2.1 常规命令

```shell
kubectl create configmap cm-name [OPTIONS]
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

### 1.2.2 热更新

* 热更新

  ```shell
  kubectl create configmap cm-name --from-file=conf/a.conf --dry-run=client -oyaml | kubectl replace -f -
  ```

  由于直接编辑yaml会涉及换行符问题, 所以直接创建一个同名configmap, 再replace即可.

subPath 无法热更新

# 2. yaml

## 2.1 指定配置

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: cm-deploy
  name: cm-deploy
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cm-deploy
  template:
    metadata:
      labels:
        app: cm-deploy
    spec:
      containers:
      - image: nginx
        name: nginx
        env:
          - name: TEST_ENV
            value: testenv
          - name: LIVES
            valueFrom:
              configMapKeyRef:
                name: cm-iter  # 指定configmap的名字
                key: a         # 引用data.a 的value
```

## 2.2 批量导入

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: cm-deploy
  name: cm-deploy
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cm-deploy
  template:
    metadata:
      labels:
        app: cm-deploy
    spec:
      containers:
      - image: nginx
        name: nginx
        envFrom:
          - configMapRef:
              name: cm-iter  # 指定configmap的名字
          profix: TEST_      # 为导入的变量统一增加前缀, 例如: TEST_a
```

## 2.3 文件挂载

* yaml

  ```shell
  # cm-deploy-volume.yaml
  apiVersion: v1
  data:
    game1.conf: |
      a=1
      b=2
      c=3
    game2.conf: |
      e=5
      f=8
      g=9
  kind: ConfigMap
  metadata:
    name: cnfromfile
  ---
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    labels:
      app: cm-deploy
    name: cm-deploy
  spec:
    replicas: 3
    selector:
      matchLabels:
        app: cm-deploy
    template:
      metadata:
        labels:
          app: cm-deploy
      spec:
        containers:
          - image: nginx
            name: nginx
            volumeMounts:
              - name: redisconf  # 引用 volumes.name
                mountPath: /etc/config  # 指定同步到Pod中的位置, 注意:多个时, mountPath的value不能重复
              - name: mysqlconf
                mountPath: /etc/nginx/nginx.conf  # 仅挂载一个文件
                subPath: nginx.conf  # 指定挂载文件 nginx.config
        volumes:
          - name: redisconf
            configMap:
              name: cnfromfile  # 引用 configmap的name 
              defaultMode: 0777  # 文件权限设置
          - name: mysqlconf
            configMap:
              name: cnfromfile
              items  # 选择configmap中的指定key
                - key: mysqlconf  # 选择configmap的key
                - path: mysql.conf  # 将mysqlconf修改为mysql.conf
                  mode: 0777  # 配置文件权限, 优先级最高
              defaultMode: 0777
                
  ```

* 检查

  ```shell
  # 创建后, 进行检查
  kubectl exec -it cm-deploy-67784f78f9-rwrcv -- bash -c 'ls /etc/config'
  ```

* 更新

  ```shell
   # 修改配置文件
   kubectl edit cm cnfromfile
   
   # 等待生效, 大概30s左右
   kubectl exec -it cm-deploy-67784f78f9-rwrcv -- bash -c 'cat /etc/config/game1.conf'
  ```


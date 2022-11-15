官方网址: https://kubernetes.io/zh-cn/docs/reference/kubectl/cheatsheet/



### 1. 增加自动补全

```shell
source <(kubectl completion bash) # 在 bash 中设置当前 shell 的自动补全，要先安装 bash-completion 包。
echo "source <(kubectl completion bash)" >> ~/.bashrc # 在你的 bash shell 中永久地添加自动补全
```

### 2. 集群操作

#### 2.1 信息查看

* 集群核心配置

  ```shell
  # 默认配置位置
  KUBECONFIG=~/.kube/config:~/.kube/kubconfig2
  # 注意 我们在集群创建时, 我们修改了这个值, 正确的是
  KUBECONFIG=/etc/kubernetes/admin.conf
  ```

* 常用命令

  ```shell
  kubectl config view # 显示合并的 kubeconfig 配置。
  
  # 集群切换
  kubectl config use-context gce
  ```

#### 2.2 集群操作

* 创建Pod

  ```shell
  # 不创建资源, 生成yaml
  kubectl create deployment nginx2 --image=nginx --dry-run=client -oyaml > nginx2.client.yaml
  
  kubectl create xxx.yaml     # 存在会报错
  kubectl apply -f xxx.yaml   # 强制重新安装
  
  
  kubect get pod/svc
  ```

* 删除Pod

  ```shell
  kubectl delete
  ```

  


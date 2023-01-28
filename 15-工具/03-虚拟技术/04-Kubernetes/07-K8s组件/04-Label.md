# 1. Label

## 1.1 简介

Label(标签)可以对k8s的一些对象(Pod, Node)进行分组, 主要用于Selector的筛选.

## 1.2 常见操作

* 增加

  ```shell
  kubectl label node master01 master02 master03 role=master
  ```
  
* 修改

  ```shell
  # 指定覆盖
  kubectl label node master01 master02 master03 role=master --overwrite
  
  # 批量覆盖
  kubectl label node role role=master --overwrite
  ```

* 删除

  ```shell
  # 指定删除
  kubectl label node master01 master02 master03 role-
  
  # 批量删除
  kubectl label node -l role role-
  ```

* 查询

  ```shell
  # 查看全部的标签
  --show-labels
  
  # 查看各个节点的标签
  kubectl get node --show-labels
  
  # 查看指定标签的节点信息
  kubectl get node -l role --show-labels
  
  # 筛选标签查询
  kubectl get node -l 'subnet!=7, role in (master,node)'
  ```

  
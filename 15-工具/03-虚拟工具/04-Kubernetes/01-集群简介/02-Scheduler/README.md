# Kubernetes调度

主要包含:

* Replication Controller

  复制控制器, 简称RC.

  * 确保副本数量达到期望值, 让指定Pod总是处于可用状态

* Replication Set

  复制集, 简称RS

  * 相比RC, 增加了标签原则器
  * 主要用于Deployment协调创建, 删除, 更新Pod

* Deployment(dep)

  无状态集, 简称dep/deploy

  * 与RS相比, 增加了自动管理Pod, 可以自动扩容缩容
  * 可以回滚版本等操作

* Statefulset

  有状态集, 简称sfs

  * 与deploy相比, 可以部署有状态且有序启动的服务

* DaemonSet(ds)
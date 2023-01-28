## LVS(NAT)模式集群

ipvs: 内核中的协议栈上实现

ipvsadm: 用户空间的集群服务管理工具

## 用户量指标

PV(Page View), 页面浏览量

UV(Unique Visitor), IP访问量

## 集群方式

LB(Load Balance), 负载均衡集群

HA(High Availability), 高可用集群

HPC(High Perfermance Computing), 高可用计算集群

* LB实现方式
  * 硬件方式: 使用F5负载均衡器
  * 软件方式: LVS(4) + Nginx(7)
* HA实现方式
  * keepalived + nginx
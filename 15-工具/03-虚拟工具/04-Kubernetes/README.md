#### kubernetes

* 来源于谷歌Borg的开源版本.

* 属于Cloud Native Computing Foundation 云原生计算基金会(CNCF) 开源组织推广的 云原生应用(Cloud Native Application). 

基础架构的推进

* 物理机: 一旦物理机出现问题, 将会影响到全部服务和数据, 不利于服务维护
* 虚拟化: 构建出来的虚拟机太多, 不利于管理
* 云计算: 虚拟机的编排系统, 底层还是基于系统层面虚拟化(OS->Hypervisor(VM, KVM)-子OS>->LIB->APP), 太过于臃肿, 构建环境较慢
* 容器: 基于APP层面构建虚拟化(OS->Host OS(子OS)->Container(docker)->LIB->APP), 但容器太多不利于管理
* 容器编排: 容器的编排系统
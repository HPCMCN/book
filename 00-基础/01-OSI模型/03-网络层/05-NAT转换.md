# 1. NAT转换

## 1.1 问题

私有网络中的应用程序能和外部网络是无法进行通信的. 要想通讯需要借助NAT地址转换.

## 1.2 NAT地址转换

NAT(Network Address Translation), 网络地址转换.

* 动态NAT

  将多个私有IP绑定到一个公有IP上. 

* 静态NAT

  将一个私有IP绑定到一个公有IP上.

现在主要用的是动态NAT, 静态NAT不能解决IP地址短缺的问题.

### 1.2.1 动态NAT工作原理

![图片描述](.image/05-NAT%E8%BD%AC%E6%8D%A2/5e532e760001f9d510901022.png)

* 第一步

  192.168.0.1发送以太网帧到路由器192.168.0.254的mac地址

  ![图片描述](.image/05-NAT%E8%BD%AC%E6%8D%A2/5e55f04f000151a217280190.png)

  

* 第二步

  路由器收到后, 会对数据包使用NAT技术, 将源IP变更为当前公网IP, 重新将以太网帧发送出去.

  ![图片描述](.image/05-NAT%E8%BD%AC%E6%8D%A2/5e55f056000158d317230183.png)

  并使用NAT表记录: 源IP, 目标IP, 源端口, 目标端口信息.

  |               内网数据帧               |                转发数据帧                 |
  | :------------------------------------: | :---------------------------------------: |
  | 192.168.0.1，13.250.177.223，12345，80 | 117.148.64.237，13.250.177.223，12345，80 |

  但是在局域网中， 可能存在多个IP同时访问这个服务。 所以NAT表将会重新分配Port。防止发送数据帧冲突

  |               内网数据帧               |              转发数据帧               |
  | :------------------------------------: | :-----------------------------------: |
  | 192.168.0.1，13.250.177.223，12345，80 | 117.148.64.237，13.250.177.223，1，80 |
  | 192.168.0.2，13.250.177.223，12345，80 | 117.148.64.237，13.250.177.223，2，80 |

  所以在局域网中配置外网通讯的应用上限为65535个

* 第三步

  当服务端收到该数据帧后, 会做出相应. 发出对应的数据帧

  ![image-20200516161106234](.image/05-NAT%E8%BD%AC%E6%8D%A2/image-20200516161106234.png)

由于路由NAT转换提取到了Port, 所以对于网络数据OSI模型传递大概如下:

![图片描述](.image/05-NAT%E8%BD%AC%E6%8D%A2/5e5f5889000175aa24121368.png)

# 2. 端口转发

## 2.1 问题

通过地址转换， 可以完成局域网访问互联网。但是从互联网还是不能直接访问局域网的。

要想时间外网访问私有网络的主机程序， 需要对端口进行转发

## 2.2 端口转发

如果直接访问公网IP是没有限制的。 所以可以直接将局域网所使用的端口映射到公网IP上。

所以路由器还有一个端口转发表：

| 协议 | 外部IP         | 外部端口 | 内部IP      | 内部端口 |
| ---- | -------------- | -------- | ----------- | -------- |
| TCP  | 117.148.64.237 | 80       | 192.168.0.1 | 80       |

这样外网的程序就可以通过端口直接与局域网中的网络程序通信了.

## 2.3 端口转发的特点

提高了局域网主机的安全系数. 减少端口的暴露


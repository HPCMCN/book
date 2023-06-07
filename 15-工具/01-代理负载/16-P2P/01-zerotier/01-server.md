# 1. server搭建

1. 安装依赖环境

   ```shell
   yum install wget gcc gcc-c++ git json-devel -y
   ```

2. 下载zerotier**根服务**

   ```shell
   curl -s https://install.zerotier.com/ | sudo bash
   ```

3. 开放防火墙端口如下:

   ```shell
   TCP:9993  TCP: 3443
   ```

4. 查看秘钥信息

   ```shell
   cd /var/lib/zerotier-one/
   记住: identity.public, authtoken.secret的内容, 备用
   ```

5. 下载源码

   ```shell
   # /var/lib/zerotier-one/ZeroTierOne
   git clone https://github.com/zerotier/ZeroTierOne
   ```

6. 修改部分源代码

   ```shell
   vim /var/lib/zerotier-one/ZeroTierOne/attic/world/mkworld.cpp
   注释:  Los Angeles 等四个节点, 内容大概如下
   //roots.push_back(World::Root());
   //roots.back().identity = Identity("99***db7:0:206e***003ceb6");
   //roots.back().stableEndpoints.push_back(InetAddress("195.***.159/443"));
   //roots.back().stableEndpoints.push_back(InetAddress("2a0***0:c024::/443"));
   
   然后添加自己的节点信息:
       std::vector<World::Root> roots;
       const uint64_t id = ZT_WORLD_ID_EARTH;
       const uint64_t ts = 1567191349589ULL; // August 30th, 2019
   # --------------------- 修改部分[start] --------------------------------------------
        roots.push_back(World::Root());
        roots.back().identity = Identity("identity.public文件的内容");
       // 默认端口是9993，可以自行修改，但不建议
       roots.back().stableEndpoints.push_back(InetAddress("外网ip/9993"));
   
   # --------------------- 修改部分[end] --------------------------------------------
   	// Los Angeles
       //roots.push_back(World::Root());
       //roots.back().identity = Identity("3a46f1bf30:0:76e66fab33e28549a62ee2064d1843273c2c300ba45c3f20bef02dbad225723bb59a9bb4b13535730961aeecf5a163ace477cceb0727025b99ac14a5166a09a3");
       //roots.back().stableEndpoints.push_back(InetAddress("185.180.13.82/9993"));
       	                              //roots.back().stableEndpoints.push_back(InetAddress("2a02:6ea0:c815::/9993"));
   
   ```

7. 重新编译文件

   ```shell
   cd ./ZeroTierOne/attic/world/
   
   source ./build.sh
   ./mkworld
   mv ./world.bin ./planet
   ```

8. 替换planet

   ```shell
   cp -r ./planet /var/lib/zerotier-one/
   cp -r ./planet /root # 备用保存好
   ```

9. 重启zerotier

   ```shell
   systemctl restart zerotier-one.service
   ```

10. 检查服务和端口

    ```shell
    systemctl status zerotier-one.service
    netstat -ano | grep 9993
    ```

# 2. UI搭建

1. 安装ui

   ```shell
   yum install https://download.key-networks.com/el7/ztncui/1/ztncui-release-1-1.noarch.rpm -y
   yum install ztncui -y
   ```

2. 接入zerotier

   ```shell
   # /opt/key-networks/ztncui/.env
   # 加入一下信息
   ZT_TOKEN=这里是文件authtoken.secret的内容
   NODE_ENV=production
   ZT_ADDR=127.0.0.1:9993
   HTTPS_PORT=3443
   HTTP_ALL_INTERFACES=yes
   ```

3. 重启ui

   ```shell
   systemctl restart ztncui
   ```

4. 检查服务和端口

   ```shell
   systemctl status zerotier-one.service
   netstat -ano | grep 3443
   ```



# 3. 配置网络

如果上面的操作没有问题, 那么就可以直接到页面上进行配置操作了.

网址为: `https://服务器公网ip:3443`  协议为**https**

账号密码默认值为: admin/password

登录后可以重置

创建网络: 点击"添加网络", 按照要求添加一个网络

然后就可以到client中使用了




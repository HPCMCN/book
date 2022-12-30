# 1. 秘钥

## 1.1 创建

* 创建

  ```shell
  # 生成秘钥对
  ssh-keygen -o -t rsa -C "hpcm@foxmail.com" -b 4096
  ```

* 修改

  ```shell
  # 修改密码
  ssh-keygen -f id_rsa -p
  ```

## 1.2 管理

### 1.2.1 ssh-agent秘钥管理

ssh-agent就是一个秘钥管理器, 运行ssh-agent后, 将秘钥进行缓存, 在需要认证的时候, 直接从缓存中进行验证, 而不用在复杂的文件中寻找指定的秘钥.

* 启动管理器

  ```shell
  # 单独启动一个代理进程, 退出时需要手动关闭
  eval `ssh-agent -s`
  
  # 创建一个临时进程, 退出shell自动结束
  ssh-agent $SHELL
  ```

* 添加秘钥

  ```shell
  # 向缓存中加入私钥
  ssh-add ./id_rsa
  ```

* 查看

  ```shell
  # 查看缓存的私钥
  ssh-add -l
  
  # 查看公钥
  ssh-add -L
  ```

* 删除

  ```shell
  # 全删
  ssh-add -D
  
  # 删除指定公钥
  ssh-add -d ./id_rsa
  ```

* 锁定

  ```shell
  # 锁定当前秘钥管理器, 解锁的话再执行一次即可
  ssh-add -X
  ```

### 1.2.2 ssh-copy-id远程控制关系

ssh-copy-id, 将公钥部署到远程机器上, 建立受控关系.

注意: 如果不指定`-i`, 则默认将使用`ssh-add -L`中的公钥.

* 批量发送公钥

  ```shell
  # 将公钥批量发送到送控主机
  for i in master02 master03 node01 node02;do ssh-copy-id -i ~/.ssh/id_rsa.pub $i;done
  ```

  


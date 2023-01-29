* 开通OSS, 创建Bucket和AK, SK设置

  ![image-20230128173334641](.image/04-oss%E6%8C%82%E8%BD%BD/image-20230128173334641.png)

* 安装OSS挂载工具

  文档: https://help.aliyun.com/document_detail/153892.htm?spm=a2c4g.11186623.0.0.6b0d7f1fnwvI8B#concept-kkp-lmb-wdb

  ```shell
  yum install -y wget fuse fuse-devel fuse-libs fuse-libs-devel
  
  wget http://gosspublic.alicdn.com/ossfs/ossfs_1.80.6_centos7.0_x86_64.rpm
  rpm -hiv ossfs_1.80.6_centos7.0_x86_64.rpm
  ```

* 配置连接Bucket, ak和sk

  ```shell
  echo hz-hpcm:{AK}:{SK} > /etc/passwd-ossfs
  chmod 640 /etc/passwd-ossfs
  ```

* 文件挂载

  ```shell
  mkdir /data
  ossfs hz-hpcm /data -o url=http://oss-cn-hangzhou.aliyuncs.com
  ```

* 解除挂载

  ```shell
  fusermount -u /data
  ```

  
# 1. linux版挂载

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

* 同步时间

  ```shell
  # 需要同步时间, 否则挂载是会报错: RequestTimeTooSkewed
  ntpdate time2.aliyun.com
  ```

* 文件挂载

  ```shell
  mkdir /data
  ossfs hz-hpcm /data -o url=http://oss-cn-hangzhou.aliyuncs.com -o allow_other
  ```

* 解除挂载

  ```shell
  fusermount -u /data
  ```


# 2. win版挂载

* 工具下载

  链接: https://pan.baidu.com/s/1zwvHAxuiVlYdhHsL5YTTCw 提取码: ieqr

* 安装 winfsp, 采用默认即可

* 解压rclone, 并将文件目录加入到环境变量中, 保证在cmd中可以执行命令`rclone -h`

* 添加Bucket, ak和sk, **带箭头的表示需要填写的内容**

  ```shell
  E:\project>rclone config
  Current remotes:
  
  Name                 Type
  ====                 ====
  No remotes found, make a new one?
  n) New remote
  #....
  n/s/q> n  # --> 选择 n 创建配置
  name> ossfs
  Option Storage.
  Type of storage to configure.
  Choose a number from below, or type in your own value.
  #....
   5 / Amazon S3 Compliant Storage Providers including AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Lyve Cloud, Minio, RackCorp, SeaweedFS, and Tencent COS
     \ (s3)
  #....
  Storage> 5 # --> 选择 5 aliyun产品
  #....
   2 / Alibaba Cloud Object Storage System (OSS) formerly Aliyun
     \ (Alibaba)
  #....
  provider> 2 # --> 选择2 aliyun的 oss
  ...
   1 / Enter AWS credentials in the next step.
     \ (false)
  env_auth> 1 # --> 选择1 从命令行中录入ak, sk
  access_key_id> xxxx
  secret_access_key> xxx
  Option endpoint.
  #...
   3 / East China 1 (Hangzhou)
     \ (oss-cn-hangzhou.aliyuncs.com)
  #...
  endpoint> 3 # ->  选择 3 endpoint信息, 根据需求填写
  # --> 其余的一路回车即可
  创建完成后, 按q退出即可
  ```

* 建立连接

  ```shell
  rclone mount ossfs:/hz-hpcm   E:\project\ossfiles --no-check-certificate --allow-other --allow-non-empty
  ```

  * `ossfs`: 刚才在`rclone config`创建的name
  * `/hz-hpcm`: oss的bucket
  * `E:\project\ossfiles`: 映射到本地的位置

* 打开`E:\project\ossfiles`目录, 查看是否成功


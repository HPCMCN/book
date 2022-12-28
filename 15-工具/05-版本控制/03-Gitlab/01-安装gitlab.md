# 1. 安装

## 1.1 docker安装

```shell
docker run \
    --detach \
    --hostname 152.32.170.211 \
    --publish 4143:443 \
    --publish 4022:22 \
    --publish 4180:80 \
    --name gitlab \
    --restart unless-stopped \
    -v /home/hpcm/gitlab/etc:/etc/gitlab \
    -v /home/hpcm/gitlab/log:/var/log/gitlab \
    -v /home/hpcm/gitlab/data:/var/opt/gitlab \
    beginor/gitlab-ce:11.3.0-ce.0
    
docker run \
    --detach \
    --hostname 152.32.170.211 \
    --publish 4143:443 \
    --publish 4022:22 \
    --publish 4180:80 \
    --name gitlab \
    --restart unless-stopped \
    -v /home/hpcm/gitlab/etc:/etc/gitlab \
    -v /home/hpcm/gitlab/log:/var/log/gitlab \
    -v /home/hpcm/gitlab/data:/var/opt/gitlab \
    gitlab/gitlab-ce
```

## 1.2 rpm安装

下载路径: https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/

* 安装

  ```shell
  rpm -hiv xxx.rpm
  ```

# 2. 配置

## 2.1 禁用prometheus

* 禁用prometheus

  ```shell
  vim /etc/gitlab/gitlab.rb
  
  #prometheus['enable'] = false
  ```

* 生效

  ```shell
  gitlab-ctl reconfigure
  gitlab-ctl restart 
  ```

  


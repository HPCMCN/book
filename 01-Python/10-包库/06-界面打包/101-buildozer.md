#  1. buildozer

本教程采用docker构建, 想在实体机上搭建, 难度极高,浪费了2周时间, 出现了乱七八糟的错误:

* android的N什么错误
* ssl编译出错
* ld报错
* sqlite.org网站宕机

要注意是  注意观察报错信息, 如果是网站不可访问 , 过一段时间可能就行了, 要有耐心

## 1.1 docker构建

镜像需要采用`ubuntu20.04, id=54c9d81cbb44`

* 拉取镜像

  ```shell
  docker pull ubuntu:20.04
  ```

* 启动镜像

  ```shell
  docker run -itd --name ubuntu --privileged=true --volume "$PWD":/home/test --entrypoint /bin/bash ubuntu:20.04
  ```

* 进入镜像

  ```shell
  docker exec -it ubuntu /bin/bash
  ```

## 1.2 构建环境

* 安装vim, 编辑内容

  ```shell
  apt update
  apt install -y vim
  ```

* 更改镜像源

  ```shell
  vim /etc/apt/sources.list
  # 更换为国内源, 直接百度操作吧, 这里就略过了
  ```

* 下载需要的环境

  ```shell
  apt install -y git zip unzip openjdk-13-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
  ```

* 下载虚拟环境包

  ```shell
  pip3 install virtualenv virtualenvwrapper
  ```

* 创建普通用户, root账号会报错

  ```shell
  adduser appgess
  su - root
  ```

* 创建虚拟环境变量

  ```shell
  vim ~/.bashrc  # 这个文件没有的话, 从root下cp一个到~, 然后chown appgess: .bashrc
  # 添加如下内容
  # export VIRTUALENVWRAPPER_PYTHON=python3
  # source '/usr/local/bin/virtualenvwrapper.sh'
  # export PATH=$PATH:~/.local/bin/
  source ~/.bashrc
  ```

* 创建虚拟环境

  ```shell
  mkvirtualenv -p python3 test
  ```

* 安装python环境

  ```shell
  pip install cpython==0.29.19 buildozer
  ```

### 1.3 编译环境

接下来求佛吧, 希望不要报错

* 将需要编译的main文件copy过来

  ```shell
  cp /home/test/main.py ./
  ```

* 初始化环境

  ```shell
  buildozer init
  ```

* 先不用改这个文件了, 直接编译, 不成功便成仁, 成功再次一举了

  ```shell
  buildozer -v android debug
  ```

  成功到达这个页面说明通过了, 赶紧查看你的第一个apk吧

  ![image-20220219221020748](.image/02-buildozer/image-20220219221020748.png)

  






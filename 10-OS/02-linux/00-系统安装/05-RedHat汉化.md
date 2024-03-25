ReaHat汉化

1. 安装中文包

  * 挂载磁盘, VMware下部有个小光盘的东东, 启用挂载连接
  *  查看挂载的位置df -h

2. 修改yum源为本地源

  * 备份源文件

  * 创建:

    ```shell
    name=Red Hat Enterprise Linux $releasever - $basearch - Source
    baseurl='file:///media/RHEL_6.5 x86_64 Disc 1'
    enabled=1
    gpgcheck=0
    ```

  * 清理缓存

    ```shell
    yum clean all
    ```

3. 安装中文包

  ```shell
  yum install "@Chinese Support"
  ```

4. `system` --> `input method` --> 勾选`Enable input method feature` --> `Input Method preferences` --> `input Meth` --> `Select an input method` --> `pinyin` 重启后使用`ctrl`+空格切换

5. 页面汉化:
  su root
  vim /etc/sysconfig/i18n
  注释LANG="en_US", 添加:
  LANG="zh_CN.GB18030"

6. 重启即可
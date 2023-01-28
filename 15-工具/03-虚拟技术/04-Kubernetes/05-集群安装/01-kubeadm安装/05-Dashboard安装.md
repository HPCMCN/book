* 配置文件

  [dashboard-user.yaml](../../.image/09-Dashboard%E5%AE%89%E8%A3%85/dashboard-user.yaml)

  [dashboard.yaml](../../.image/09-Dashboard%E5%AE%89%E8%A3%85/dashboard.yaml)

* 安装指定版本

  ```shell
  kubectl  create -f .
  ```

* 查看启动端口号

  ```shell
  kubectl get svc -n kubernetes-dashboard
  ```

  ![image-20221115181233519](../../.image/09-Dashboard%E5%AE%89%E8%A3%85/image-20221115181233519.png)

* 查看登录密码

  ```shell
  kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep admin-user | awk '{print $1}')
  ```

* google浏览器需要进行兼容处理

  ```shell
  # 无所谓, 就是证书提示不安全, 加入信任即可, 不是必需选项
  --test-type --ignore-certificate-errors
  ```

  ![image-20221115181515218](../../.image/09-Dashboard%E5%AE%89%E8%A3%85/image-20221115181515218.png)

* 查看网站

  ```shell
  https://node_ip:刚才查看的port/
  # https://10.111.0.20:31499/
  ```

  ![image-20221115181845796](../../.image/09-Dashboard%E5%AE%89%E8%A3%85/image-20221115181845796.png)
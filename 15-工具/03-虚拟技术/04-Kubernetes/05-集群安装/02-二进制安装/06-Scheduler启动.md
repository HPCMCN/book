# 1. 配置文件

* 所有master节点都要配置

  ```shell
vim /usr/lib/systemd/system/kube-scheduler.service
  
  [Unit]
  Description=Kubernetes Scheduler
  Documentation=https://github.com/kubernetes/kubernetes
  After=network.target
  
  [Service]
  ExecStart=/usr/local/bin/kube-scheduler \
        --v=2 \
        --feature-gates=EphemeralContainers=true  # 开启临时容器
        --logtostderr=true \
        --address=127.0.0.1 \
        --leader-elect=true \
        --kubeconfig=/etc/kubernetes/scheduler.kubeconfig
  
  Restart=always
  RestartSec=10s
  
  [Install]
  WantedBy=multi-user.target
  ```

# 2. 启动服务

* 启动服务

  ```shell
  systemctl daemon-reload
  systemctl enable --now kube-scheduler
  ```
  
* 检查测试

  ```shell
  systemctl status kube-scheduler
  tail -f /var/log/messages
  ```

  
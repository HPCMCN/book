# 1. firewall

## 1.1 状态操作

```bash
# 如果有systemctl命令
systemctl stop firewalld.service   # 停止
systemctl start firewalld.service  # 开启
systemctl status firewalld.service # 状态
systemctl disable firewalld.service  # 禁用开机自启
systemctl enable firewalld.service  # 打开开机自启

# 如果有chkconfig命令
chkconfig --list | grep network  # 查看是否开机自启
chkconfig firewalld off  # 禁用开机自启
chkconfig firewalld on  # 启用开机自启
```

## 1.2 配置
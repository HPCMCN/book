#### 1. 给某个用户某个命令的权限

```shell
编辑/etc/sudoers文件
[root@xxx home]# visudo   # 只能用这个命令打开这个文件
# 为用户设置别名
User_Alias xxx = temp

# 为命令设置别名
Cmnd_Alias ccc = /usr/bin/gdb,/usr/bin/python

# 设置sudo权限信息
xxx ALL=(ALL) NOPASSWD:ccc,/usr/bin/gdb
```


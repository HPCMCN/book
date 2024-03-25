ssh连接过慢解决:
su root
vim /etc/ssh/sshd_config
修改:
UseDNS no
GSSAPIAuthentication no
```python
from xmlrpc.client import ServerProxy


class Client(ServerProxy):

    @property
    def state(self):
        return self.supervisor.getState()

    def get_processes(self):
        """获取全部服务"""
        return self.supervisor.getAllProcessInfo()

    def restart(self):
        """重启服务"""
        return self.supervisor.restart()


if __name__ == '__main__':
    # 注意: 这里使用的是tcp连接的, 默认是采用sokcet file连接, 需要修改配置, 并重启supervisord服务
    # 更多的操作, 可以查看官网进行
    client = Client("http://localhost:9001/RPC2")
    print(client.supervisor.getState())

```


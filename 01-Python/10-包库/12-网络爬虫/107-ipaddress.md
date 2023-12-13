1. 位数与掩码转换

   ```python
   network = "10.0.0.0"
   prefixlen = 22
   netmask = ipaddress.IPv4Network("{}/{}".format(network, prefixlen), strict=False).netmask
   print(f"prefixlen {prefixlen} ==> netmask {netmask}")
   netmask = "255.255.255.255"
   prefixlen = ipaddress.IPv4Network("{}/{}".format(network, netmask), strict=False).prefixlen
   print(f"netmask {netmask} ==> prefixlen {prefixlen}")
   ```

2. 判断某个ip是否是掩码约束范围内

   ```shell
   ipaddress.ip_address("10.0.0.1") not in ipaddress.ip_network("10.234.5.112/22", strict=False))
   ```

   
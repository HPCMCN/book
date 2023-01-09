```python
# 大端小端与int转换, 常用于TCP报文传输或者和C程序通讯时进行转换
import struct

data = 123

little_byte_data = struct.pack("<i", data)
big_byte_data = struct.pack(">i", data)
print(little_byte_data)
print(int.to_bytes(123, 4, "big"))
print(int.from_bytes(little_byte_data, "little"))
print(int.from_bytes(big_byte_data, "big"))
```


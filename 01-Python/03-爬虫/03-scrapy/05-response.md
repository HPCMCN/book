# 1. Response

```python
response.xpath("//title/text()")				类似xpath
response.xpath("//title/text()").extract		全部列表
response.xpath("//title/text()").extract_first  取出第一个first, 有数据返回数据, 没数据返回None
```




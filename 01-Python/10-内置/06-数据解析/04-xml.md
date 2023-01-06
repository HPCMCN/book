```python
import xml.etree.ElementTree as etree

data = """
<root>
    <head>
        <worktime>2</worktime>
        <run_script>3</run_script>
        <transid>4</transid>
    </head>
    <tail>
        <retcode>0</retcode>
        <retcode>1</retcode>
    </tail>
    <body>
        <private>
            <flag>1</flag>
        </private>
    </body>
</root>
"""

# 读取xml文本内容
parser = etree.fromstring(data.strip())
# 读取xml文件
parser = etree.parse("test.xml")

# 利用xpath解析dom树
print([x.text for x in parser.findall(".//tail/retcode")])
```


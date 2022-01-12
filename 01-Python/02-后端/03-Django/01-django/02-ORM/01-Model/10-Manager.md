## 3.3 自定义查询集

**注意:**  一经修改, objects管理器将会失效.

### 3.3.1 查询集

```python
class SomeTableManager(models.Manager):
    def all(self):
        # 让all方法继承filter方法, 并给filter传递参数
        return super().filter(is_delete=False)
    
    def create_table(self, title, pub_date):
        # 创建模型类对象: self.model
        st = self.model()
        st.filed = title
        st.save()
        return st
    
    def get_queryset(self):
        """此函数, 会过滤查询集. 通过此方法可以过滤被删除的信息"""
        return super().get_queryset().filter(id_delete=False)
```



### 3.3.2 激活查询集

```python
class SomeTable(models.Model):
    """orm模型"""
    query = TableManager()
    # 还可以定义系统自带的查询集, 达到两用的效果
    objects = models.Manager()
    
SomeTable.query.all()    # 受查询集的影响
SomeTable.objects.all()  # 不受查询集的影响
SomeTable.query.create_table("xx", "xx")
```

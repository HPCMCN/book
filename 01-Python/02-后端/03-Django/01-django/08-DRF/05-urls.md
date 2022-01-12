## action映射关系

* list: list
* retrieve/update/partial_update/delete:  detail
* action装饰后: 默认为function名称, name可以重置

## 反向查找

basename + name

示例

```python
from functools import partial
from django.urls import reverse

# list
print(reverse("api:organization-list"))
# detail
organization_users_url = partial(reverse, "api:organization-detail")
print(organization_users_url(args=(1,)))

# <pk>/tree
organization_tree_url = partial(reverse, "api:organization-tree")
print(organization_tree_url(args=(1,)))
```




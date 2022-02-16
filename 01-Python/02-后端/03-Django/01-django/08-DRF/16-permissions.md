# Permission

drf权限全部继承BasePermission, 包含两个限权方法:

* has_permission

  视图级限权

* has_object_permission

  对象级限权

示例

```python
class IsOwnerUser(BasePermission):
    """是否为用户自己  创建的条目
    当前权限为: 允许访问
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return hasattr(obj, "created_by") and request.user.id == obj.created_by.id


class TestView(APIView):
    permission_classes = (IsOwnerUser,)
```

注意: 权限管理默认为and模式, 即permission_classes中存在一个鉴权不通过, 则本次请求403

所以在用时最好进行权限叠加, BasePermission存在两个操作符  `|`, `&`, 经过使用操作符号后, 对象将变成`Hook`不能再次使用此操作符

示例

```python
IsOwnerUserOrAdmin = IsOwnerUser | IsSuperAdmin
IsOwnerThirdTokenOrAdmin = IsOwnerThirdToken | IsSuperAdmin
```


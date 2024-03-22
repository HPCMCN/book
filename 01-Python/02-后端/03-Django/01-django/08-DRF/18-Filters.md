# Django-filter

## 1.1 安装

* 安装

  ```shell
  pip install django-filter
  ```

## 1.2 quickstart

* settings配置

  ```python
  # 注册app
  INSTALLED_APPS = [
      ...
      "django_filters"
  ]
  
  # 全局注册backend
  REST_FRAMEWORK = {
      ...
      "DEFAULT_FILTER_BACKENDS": (
          "django_filters.rest_framework.DjangoFilterBackend",
          "rest_framework.filters.SearchFilter",
          "rest_framework.filters.OrderingFilter",
      ),
  }
  ```

* 快速接入

  ```python
  # views.py
  class UsersViewSet(viewsets.ModelViewSet):
  	queryset = models.Users.objects.all()
      filter_backends = (DjangoFilterBackend, SearchFilter)
      # 全表匹配字段: /api/users/?q=张三 ==> name=张三 or username=张三
      search_fields = ("name", "username")
      # 单个字段匹配: /api/users/?id=1&id__in=1,2,3
      #			  /api/users/?time__gte=2024-03-22 15:00:00&time__lte=2024-03-21 15:00:00
      filterset_fields = {
          "id": ["exact", "in"],
          "number": ["exact", "in"],
          "name": ["exact"],
          "car_number": ["exact", "in"],
          "time": ["gte", "lte", "gt", "lt"]
      }
  
      search_fields = ("name", "id", "id_card", "number")
      ordering_fields = ("id", "name", "number")
  ```

## 1.3 自定义查询

* 创建`filters.py`文件

  ```python
  # filters.py
  from django_filters import FilterSet, filters
  
  from . import models
  
  class DefaultFilter(object):
      """向查询filterset中注入default字段, 保证查询时存在缺省参数"""
  
      def __init__(self, *args, **kwargs):
          data = dict(kwargs["data"])
          update_data = {}
          for name, field in self.base_filters.items():
              default = field.extra.pop("default", "None")
              if default == "None" and getattr(field, "_default", "None") == "None":
                  continue
              if getattr(field, "_default", "None") == "None":
                  field._default = default
              if not data.get(field):
                  update_data[name] = field._default()
          if update_data:
              data.update(update_data)
              kwargs["data"] = data
          super().__init__(*args, **kwargs)
  
  
  class UserFilterSet(DefaultFilter, FilterSet):
      # search field: role
      role = filters.CharFilter(label="role", field_name="user_roles__roles__code", method="filter__role")
      # search field: role_id
      role_id = filters.CharFilter(label="role_id", field_name="user_roles__roles__id")
      role_id__in = filters.BaseInFilter(label="role_id", field_name="user_roles__roles__id", lookup_expr="in")
      
      mode_choices = (
          ("month", "上个月"),
          ("quarter", "上季度"),
          ("year", "去年")
      )
      # search field: mode
      mode = filters.ChoiceFilter(choices=mode_choices)
  
      # search field: time, default=当前月, 初一
      time = filters.DateFilter(
          input_formats=("%Y-%m", "%Y-%m-%d"),
          default=lambda: datetime.now().replace(day=1).strftime("%Y-%m"),
          help_text="使用月份进行查询(示例: 2024-02, 默认为当前月)"
      )
  
      class Meta:
          model = models.Users
          fields = {
              "id": ["exact", "in"],
              "name": ["exact", "in", "icontains"],
              "username": ["exact", "in", "icontains"],
              "last_login": ["isnull"],
          }
         
      @property
      def qs(self):
          qs = super().qs
          return qs
  
      def filter__role(self, qs, name, value):
          return qs.filter(user_roles__roles__code=value)
  ```

* 引入到视图`views.py`中

  ```python
  # views.py
  class UsersViewSet(viewsets.ModelViewSet):
  
      ...
      filter_backends = (DjangoFilterBackend, SearchFilter)
      filterset_class = filters.UserFilterSet
      search_fields = ("name", "username")
  ```

* 注册路由`urls.py`

  ```python
  # urls.py
  from django.urls import include, path, re_path
  
  urlpatterns = []
  routes = DefaultRouter()
  routes.register("users", viewset=views.UsersViewSet, basename="users")
  urlpatterns += routes.urls
  ```

  


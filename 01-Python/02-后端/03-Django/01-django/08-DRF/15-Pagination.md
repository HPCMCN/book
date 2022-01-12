# 1. 全局

* django-settings

  目前仅支持这两个字段

  ```python
  INSTALLED_APPS = [
      "rest_framework",
  ]
  
  REST_FRAMEWORK = {
      "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
      "PAGE_SIZE": PAGE_SIZE
  }
  ```

# 2. 自定义

* 自定义内容如下

  ```python
  from django.conf import settings
  from rest_framework.pagination import PageNumberPagination as BasePageNumberPagination
  
  
  class PageNumberPagination(BasePageNumberPagination):
      page_size = settings.PAGE_SIZE
      max_page_size = settings.MAX_PAGE_SIZE
      page_query_param = "page"
      page_size_query_description = "size"
  
  ```

* 视图引用

  ```python
  from . import models, serializers
  from utils.login import JSONWebTokenAuthentication
  from utils.pagination import PageNumberPagination
  
  
  # Create your views here.
  class UsersViewSet(viewsets.ModelViewSet):
      pagination_class = PageNumberPagination
  ```

  


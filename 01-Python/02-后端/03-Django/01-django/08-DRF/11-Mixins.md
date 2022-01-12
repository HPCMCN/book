# 3. Mixin

利用多继承特性, 来接入不同功能

## 3.1 ListModelMixin

提供list api的主要功能, 实现过滤, 分页功能

### 3.1.1 源码

```python
class ListModelMixin(object):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
```

### 3.1.2 实例

* 视图

  ```python
  from rest_framework.generics import GenericAPIView
  from rest_framework.mixins import ListModelMixin
  
  
  from . import models, serializer
  
  
  class Many1View(GenericAPIView, ListModelMixin):
      """xxx"""
      serializer_class = serializer.Many1Serializer
      queryset = models.Many1.objects.all()
  
      def get(self, *args, **kwargs):
          return self.list(*args, **kwargs)
  ```

  

* 路由

  ```python
  from django.urls import path
  
  from users import views
  
  urlpatterns = [
      path(r"test/", views.Many1View.as_view()),
  ]
  
  ```

## 3.2 CreateModelMixin

用于创建对象的功能

### 3.2.1 源码

```python
class CreateModelMixin(object):
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
```

### 3.2.2 实例

* 视图

  ```python
  from rest_framework.generics import GenericAPIView
  from rest_framework.mixins import ListModelMixin, CreateModelMixin
  
  
  from . import models, serializer
  
  
  class Many1View(GenericAPIView, ListModelMixin, CreateModelMixin):
      """xxx"""
      serializer_class = serializer.Many1Serializer
      queryset = models.Many1.objects.all()
  
      def get(self, *args, **kwargs):
          return self.list(*args, **kwargs)
  
      def post(self, *args, **kwargs):
          return self.create(*args, **kwargs)
  ```

  

* 路由

  ```python
  from django.urls import path
  
  from users import views
  
  urlpatterns = [
      path(r"test/", views.Many1View.as_view()),
  ]
  ```

## 3.3 RetrieveModelMixin

详情信息功能

### 3.3.1 源码

```python
class RetrieveModelMixin:
    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
```



### 3.3.2 实例

* 视图

  ```python
  from rest_framework.generics import GenericAPIView
  from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
  
  from . import models, serializer
  
  
  class Many1View(GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
      """xxx"""
      serializer_class = serializer.Many1Serializer
      queryset = models.Many1.objects.all()
  
      def get(self, request, pk=None, *args, **kwargs):
          print(pk)
          print(args, kwargs)
          if pk is None:
              return self.list(request, *args, **kwargs)
          else:
              return self.retrieve(request, pk, *args, **kwargs)
  
      def post(self, *args, **kwargs):
          return self.create(*args, **kwargs)
  ```

  

* 路由

  ```python
  from django.urls import re_path
  
  from users import views
  
  urlpatterns = [
      re_path(r"test/(?:(?P<pk>\d+)/)?", views.Many1View.as_view()),
  ]
  
  ```

## 3.4 UpdateModelMixin

更新视图相关

### 3.4.1 源码

```python
class UpdateModelMixin:
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
```



### 2.4.2 示例

* 视图

  ```python
  from rest_framework.generics import GenericAPIView
  from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
  
  from . import models, serializer
  
  
  class Many1View(GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
      """xxx"""
      serializer_class = serializer.Many1Serializer
      queryset = models.Many1.objects.all()
  
      def get(self, request, pk=None, *args, **kwargs):
          print(pk)
          print(args, kwargs)
          if pk is None:
              return self.list(request, *args, **kwargs)
          else:
              return self.retrieve(request, pk, *args, **kwargs)
  
      def post(self, *args, **kwargs):
          return self.create(*args, **kwargs)
  
      def put(self, *args, **kwargs):
          return self.update(*args, **kwargs)
  ```

  

* 路由

  ```python
  from django.urls import re_path
  
  from users import views
  
  urlpatterns = [
      re_path(r"test/(?:(?P<pk>\d+)/)?", views.Many1View.as_view()),
  ]
  ```

  

## 3.5 DestroyModelMinxin

删除相关

### 3.5.1 源码

```python
class DestroyModelMixin:
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

```

### 3.5.2 示例

* 视图

  ```python
  from rest_framework.generics import GenericAPIView
  from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
      DestroyModelMixin
  
  from . import models, serializer
  
  
  class Many1View(GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                  DestroyModelMixin):
      """xxx"""
      serializer_class = serializer.Many1Serializer
      queryset = models.Many1.objects.all()
  
      def get(self, request, pk=None, *args, **kwargs):
          print(pk)
          print(args, kwargs)
          if pk is None:
              return self.list(request, *args, **kwargs)
          else:
              return self.retrieve(request, pk, *args, **kwargs)
  
      def post(self, *args, **kwargs):
          return self.create(*args, **kwargs)
  
      def put(self, *args, **kwargs):
          return self.update(*args, **kwargs)
  
      def delete(self, *args, **kwargs):
          return self.destroy(*args, **kwargs)
  ```

  

* 路由

  ```python
  from django.urls import re_path
  
  from users import views
  
  urlpatterns = [
      re_path(r"test/(?:(?P<pk>\d+)/)?", views.Many1View.as_view()),
  ]
  ```


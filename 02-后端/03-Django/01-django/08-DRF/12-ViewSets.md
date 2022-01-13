# 5. 视图集

视图集, 将GET/POST等动词利用mapping + url等方式映射为`list`, `retrieve`, `create`, `update`, `destory`

所以定义ViewSet需要使用:

* list
* retrieve
* create
* update
* destroy

不能使用GET等动词, 每次用户访问, 我们都可以通过`self.action`来确定是以上动词的哪个

```python
create_request = True if self.action == 'create' else False
```

## 5.1 GenericViewSet

继承`GenericAPIView, ViewSetMinxin`

* `ViewSetMinxin`主要用于GET等动词转换
* `GenericAPIView` 主要用于请求分发等操作

## 5.2 ViewSet

### 5.2.1 常规使用方法

继承于`ViewSetMixin, views.APIView`, 增加了身份验证, 权限校验, 流量管理等. 视图集基类不提供action方法, 需要自己实现

* 视图

  ```python
  class Many2ViewSet(ViewSet, GenericViewSet):
      """xxx"""
      queryset = models.Many2.objects.all()
  
      serializer_class = serializer.Many1Serializer
  
      def list(self, request, *args, **kwargs):
          queryset = self.filter_queryset(self.get_queryset())
  
          page = self.paginate_queryset(queryset)
          if page is not None:
              serializer = self.get_serializer(page, many=True)
              return self.get_paginated_response(serializer.data)
  
          serializer = self.get_serializer(queryset, many=True)
          return Response(serializer.data)
      
      def post(self, *args, **kwargs):
          pass
      ...
  ```

* 路由

  ```python
  from rest_framework.routers import DefaultRouter
  
  from users import views
  
  urlpatterns = [
  ]
  
  router = DefaultRouter()
  router.register(prefix=r"tests", viewset=views.Many2ViewSet)
  urlpatterns += router.urls
  ```


### 5.2.2 拓展action

* 视图函数

  ```bash
  class Many1ViewSet(ModelViewSet):
      """xxx"""
      serializer_class = serializer.Many1Serializer
      queryset = models.Many1.objects.all()
      # authentication_classes = (SessionAuthentication, BasicAuthentication)
  
      @action(methods=["GET"], detail=True)  # 只允许get请求, 访问详情页面
      def aaa(self, request, pk):
          print(pk)
          return JsonResponse({"aaa": "aaa"})
  
      @action(methods=["GET"], detail=False)  # 只允许get请求, 访问list页面
      def bbb(self, request):
          return JsonResponse({"bbb": "bbb"})
  ```

* 路由

  ```bash
  from rest_framework.routers import DefaultRouter
  
  from users import views
  
  urlpatterns = [
  ]
  
  router1 = DefaultRouter()
  router1.register(prefix=r"test", viewset=views.Many1ViewSet)
  urlpatterns = urlpatterns + router1.urls
  
  ```

* 页面效果

  url1: /users/test/1/aaa/

  url2: /users/test/bbb/ 

  ![image-20200722233030857](.image\17-REST-Views\image-20200722233030857.png)

## 5.3 常用视图集

### 5.3.1 视图集

以下视图集均继承与GenericViewSet, ViewSetMinxin

| 视图集               | 支持action                 |
| -------------------- | -------------------------- |
| ReadOnlyModelViewSet | 支持list/单个查询          |
| ModelViewSet         | 创建/查询(单/多)/更新/删除 |

### 5.3.2 路由配置

#### 5.3.2.1 SimpleRouter

| URL                           | 请求方式             | Action                                 | url-name              |
| ----------------------------- | -------------------- | -------------------------------------- | --------------------- |
| {prefix}/                     | GET/POST             | list/create                            | {basename}-list       |
| {prefix}/{url_path}/          | 指定方法             | 指定action                             | {basename}-{url_path} |
| {prefix}/{lookup}/            | GET/PUT/PATCH/DELETE | retrieve/update/partial_update/destroy | {basename}-detail     |
| {prefix}/{lookup}/{url_path}/ | 指定方法             | 指定action                             | {basename}-{url_path} |



#### 5.3.2.2 DefaultRouter

DefaultRouter会多附带一个默认的API根视图，返回一个包含所有列表视图的超链接响应数据。

| URL                                    | 请求方式             | Action                                 | url-name              |
| -------------------------------------- | -------------------- | -------------------------------------- | --------------------- |
| {.format}/                             | GET                  | 自动生成的root-view                    | api-root              |
| {prefix}/{.format}                     | GET/POST             | list/create                            | {basename}-list       |
| {prefix}/{url_path}/{.format}          | 指定方法             | 指定action                             | {basename}-{url_path} |
| {prefix}/{lookup}/{.format}            | GET/PUT/PATCH/DELETE | retrieve/update/partial_update/destroy | {basename}-detail     |
| {prefix}/{lookup}/{url_path}/{.format} | 指定方法             | 指定action                             | {basename}-{url_path} |

**api-root示例**

![image-20200709232035352](.image\17-REST-Views\image-20200709232035352.png)

### 5.3.3 实例

* 视图

  ```python
  from rest_framework.viewsets import ModelViewSet
  
  from . import models, serializer
  
  class Many1ViewSet(ModelViewSet):
      """xxx"""
      serializer_class = serializer.Many1Serializer
      queryset = models.Many1.objects.all()
  ```

* 路由

  ```python
  router = DefaultRouter()
  router.register(prefix=r"test", viewset=views.Many1ViewSet)
  urlpatterns = router.urls
  ```

* 效果

  1. /test/

     ![image-20200709224707703](.image\17-REST-Views\image-20200709224707703.png)

  2. /test/1

     ![image-20200709224734925](.image\17-REST-Views\image-20200709224734925.png)

# 6. rest-framework继承关系图

![View_serializer](image/17-REST-Views/View_serializer.png)
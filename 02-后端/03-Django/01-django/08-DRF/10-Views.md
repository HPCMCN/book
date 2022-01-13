# 1. APIView

继承于`django.view`

## 1.1 新增方法

增加方法(限制方法见`REST-Limiter`):

* authentication_classes: list/tuple, 身份验证类
* permission_classes: list/tuple, 权限验证类
* throttle_classes: list/tuple, 流量控制类

## 1.2 Request

`rest-framework.view`中的`request`是经过封装后的, 所以参数如下

| 参数         | 数据类型 | 功能                                                         |
| ------------ | -------- | ------------------------------------------------------------ |
| data         | dict     | 1. 原django的`request`中的POST/FILES数据<br>2. POST/PUT/PATCH请求数据<br>3. JSON数据 |
| query_params | dict     | 和原`request`中的GET相同                                     |
|              |          |                                                              |



## 1.3 Response

`rest-framework.response`中只提供了一个响应对象. 使用之前需要配置前端渲染器, 来指定渲染类型

### 1.3.1 配置渲染器

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (  # 默认响应渲染类
        'rest_framework.renderers.JSONRenderer',  # json渲染器
        'rest_framework.renderers.BrowsableAPIRenderer',  # 浏览API渲染器
    )
}
```

### 1.3.2 响应对象

```python
def __init__(self, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None)
```

* data:

  Python内建数据类型, 需要传入的数据

* status:

  int, 响应码

* template_name:

  str, 模板名称

* headers:

  dict, 响应头部信息

* exception:

  bool, 出现异常是否当场抛出

* content_type:

  str, 响应信息中的`Content-Type`字段, 一般不用填, 框架会自动进行填写
  

常用参数

| 参数        | 类型               | 说明               |
| ----------- | ------------------ | ------------------ |
| data        | Python内建数据类型 | 传入的data         |
| status_code | int                | 响应码             |
| content     | bytes              | 经过渲染的响应数据 |
|             |                    |                    |
|             |                    |                    |
|             |                    |                    |



## 1.5 响应码

`REST-FrameWork`提供了常用响应码常量

| 响应码                                                       | 说明       |
| ------------------------------------------------------------ | ---------- |
| HTTP_100_CONTINUE<br>HTTP_101_SWITCHING_PROTOCOLS            | 信息告知   |
| HTTP_200_OK<br>HTTP_201_CREATED<br>HTTP_202_ACCEPTED<br>HTTP_203_NON_AUTHORITATIVE_INFORMATION<br>HTTP_204_NO_CONTENT<br>HTTP_205_RESET_CONTENT<br>HTTP_206_PARTIAL_CONTENT<br>HTTP_207_MULTI_STATUS | 处理成功   |
| HTTP_300_MULTIPLE_CHOICES<br>HTTP_301_MOVED_PERMANENTLY<br>HTTP_302_FOUND<br>HTTP_303_SEE_OTHER<br>HTTP_304_NOT_MODIFIED<br>HTTP_305_USE_PROXY<br>HTTP_306_RESERVED<br>HTTP_307_TEMPORARY_REDIRECT | 重定向     |
| HTTP_400_BAD_REQUEST<br>HTTP_401_UNAUTHORIZED<br>HTTP_402_PAYMENT_REQUIRED<br>HTTP_403_FORBIDDEN<br>HTTP_404_NOT_FOUND<br>HTTP_405_METHOD_NOT_ALLOWED<br>HTTP_406_NOT_ACCEPTABLE<br>HTTP_407_PROXY_AUTHENTICATION_REQUIRED<br>HTTP_408_REQUEST_TIMEOUT<br>HTTP_409_CONFLICT<br>HTTP_410_GONE<br>HTTP_411_LENGTH_REQUIRED<br>HTTP_412_PRECONDITION_FAILED<br>HTTP_413_REQUEST_ENTITY_TOO_LARGE<br>HTTP_414_REQUEST_URI_TOO_LONG<br>HTTP_415_UNSUPPORTED_MEDIA_TYPE<br>HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE<br>HTTP_417_EXPECTATION_FAILED<br>HTTP_422_UNPROCESSABLE_ENTITY<br>HTTP_423_LOCKED<br>HTTP_424_FAILED_DEPENDENCY<br>HTTP_428_PRECONDITION_REQUIRED<br>HTTP_429_TOO_MANY_REQUESTS<br>HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE<br>HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS | 处理错误   |
| HTTP_500_INTERNAL_SERVER_ERROR<br>HTTP_501_NOT_IMPLEMENTED<br>HTTP_502_BAD_GATEWAY<br>HTTP_503_SERVICE_UNAVAILABLE<br>HTTP_504_GATEWAY_TIMEOUT<br>HTTP_505_HTTP_VERSION_NOT_SUPPORTED<br>HTTP_507_INSUFFICIENT_STORAGE<br>HTTP_511_NETWORK_AUTHENTICATION_REQUIRED | 服务器异常 |



  

## 1.4 使用实例: 

​	使用方法基本上和`django.view`没什么区别

* 视图

  ```python
  from rest_framework.views import APIView
  from rest_framework.response import Response
  
  
  from . import models, serializer
  
  
  class Many1View(APIView):
      """xxx"""
      def get(self, request):
          m1s = models.Many1.objects.all()
          ser = serializer.Many1Serializer(m1s, many=True)
          return Response(ser.data)
  ```

* 路由

  ```python
  from django.urls import path
  
  from users import views
  
  urlpatterns = [
      path(r"test/", views.Many1View.as_view())
  ]
  ```

  



# 2. GenericAPIView

继承于`rest-framework.APIView`, 增加方法如下

## 2.2 增加方法

* list数据
  * queryset: list, 指定list数据, 查询集
  * get_queryset(self): [object], 获取查询集
* 单一数据
  * lookup_url_kwarg: str, 指定url中提取的关键字参数名称, 默认等于`lookup_field`
  * lookup_field: str, 指定查询字段, 默认`pk`
  * get_object(self): object, 获取pk对应的ORM对象
* 序列化器
  * serializer_class: object, 指定序列化器类
  * get_serializer_class(self): object, 获取序列化器类
  * get_serializer(self, args, *kwargs): object, 获取序列化器对象
  * get_serializer_context(self): dict, 获取请求信息, 视图函数, 序列化执行类
* 查询集过滤器
  * filter_backends: str/object, 指定查询集的过滤器
  * filter_query(self, queryset): list, 获取过滤后的查询集

* 分页管理
  * pagination_class: str/object, 指定分页管理类
  * paginator: object, 获取当前分页对象
  * paginate_queryset(self, queryset): list, 返回当前页面的查询集
  * get_paginated_response(self, data): bytes, 返回一个渲染后发往前端以前的分页数据

## 2.2 使用实例

* 视图

  ```python
  from rest_framework.generics import GenericAPIView
  
  from . import models, serializer
  
  
  class Many1View(GenericAPIView):
      """xxx"""
      serializer_class = serializer.Many1Serializer
      queryset = models.Many1.objects.all()
  
      def get(self, request, pk=None):
          m = self.get_object()
          ser = self.get_serializer(m)
          return Response(ser.data)
  ```

* 路由

  此处要注意, django2.0后, path不能识别正则, 需要使用re_path

  ```python
  from django.urls import path, re_path
  
  urlpatterns = [
      re_path(r"test/(?P<pk>\d+)/", views.Many1View.as_view()),
  ]
  ```

  

# 4. 视图APIView

封装的高级视图函数如下

| 视图类                       | 提供方法                      | 继承关系                                                     |
| ---------------------------- | ----------------------------- | ------------------------------------------------------------ |
| CreateAPIView                | POST                          | GenericAPIView<br>CreateModelMixin                           |
| ListAPIView                  | GET                           | GenericAPIView<br>ListModelMixin                             |
| RetireveAPIView              | GET                           | GenericAPIView<br/>RetrieveModelMixin                        |
| DestoryAPIView               | DELETE                        | GenericAPIView<br/>DestoryModelMixin                         |
| UpdateAPIView                | GET<br>PUT                    | GenericAPIView<br>UpdateModelMixin                           |
| RetrieveUpdateAPIView        | GET<br>PUT<br>PATCH           | GenericAPIView<br>RetrieveModelMixin<br>UpdateModelMixin     |
| RetrieveUpdateDestoryAPIView | GET<br>PUT<br>PATCH<br>DELETE | GenericAPIView<br>RetrieveModelMixin<br>UpdateModelMixin<br>DestoryModelMixin |






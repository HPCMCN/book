1. django2和3区别

   ```shell
   1. url
   2. 协程
   ```

2. django和flask区别

   ```shell
   django的映射关系是: url和视图的map关系
   flask的映射关系是: viewname和业务函数的map关系
   Django特点:
   * ORM开发快速, 可以节约成本. 同时会降低一定的查询效率
   * 并发量不是很高, 大概1w
   Flask:
   * 开发灵活, 三方拓展包也比较丰富
   ```

3. django查询优化

   ```shell
   1. 减少外键使用, 影响插入性能
   2. 使用缓存, 减少数据库的访问
   3. 尽量使用varchar, 而不是text
   4. 查询频繁字段, 创建索引
   5. queryset默认是一个缓存集, 可以重复调用, 被存储在内存的cache里面
   6. 如果一个页面需要连接数据库, 尽量一次查询出来
   7. 如果字段不需要那么多, 可以使用values
   8. 模板里面with标签可以缓存queryset
   9. 分布式操作
   ```

4. REST API

   ```shell
   1. api配置为专有域名, 或者在主域名的根资源下
   2. 版本控制需要放置在url路径中
   3. 每个url都是一种资源, 且是一种名词形式
   4. 需要通过http请求动词方式来区别资源操作的方式
   5. 资源信息较多需要分页访问
   6. 状态码: 
      10x表示资源还待传递
      20x表示服务器处理完成
      30x表示资源需要重新访问
      40x表示请求有问题
      50x表示服务器故障
   ```

5. SCRF攻击

   ```shell
   * 由于浏览器每次请求都会携带对应的cookies信息请求网站
   * 用户信息没有请求, 去访问三方网站页面时, 受到三方页面误导, 点击对应表单
   * 对方将此次请求转接到主体网站, 造成数据在不知情状况下被篡改
   
   解决:
   
   * 开启跨域攻击中间件
   * 增加post表单的scrf_token字段
   * 增加验证码等
   ```

6. django中文件上传时, 修改文件的类型, 要怎样操作?(FileField中upload_to或者django自带的strange)

7. ORM中查询方法有哪些?(注意不常见的聚合)

8. django-restframework框架中, 需要前端传递name1字段, 但是后台数据库保存的为name2字段(中间需要做逻辑处理进行数据解析转换), 请问怎样操作?

   ```shell
   1. 定义serializer时, 需要有name1 required=True, name2, required=False
   2. 在validator中对name1, 进行相应的处理, 然后插入到attrs中, 最终需要pop name1(重点)
   ```

9. 什么是WSGI? 请举例你所知道的此框架有哪些?
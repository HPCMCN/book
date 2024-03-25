1. python2与python3的差异

   * 核心差别

     ```shell
     1. Python3 --> Unicode编码格式    Python2 --> ASCII编码格式(str和unicode)
     2. Python3 优先绝对路径导入import   PYthon2 优先相对路径导入
     3. Python3 类使用新式类(直接继承object)   Python3 采用新式和老式
     ```

   * 语法

     ```shell
     input   raw_input/input
     range   xrange/range
     强制缩进4个空格   一个tab和8个空格等价
     ```

   * 自带包和三方包

     ```shell
     queue	urllib  mysqlclient
     ```


2. Python自带的异步(口述一下怎么用?)和gevent的区别? 两者分别基于什么实现的? 猴子补丁是做什么用的?
3. 请说明一下\__new__是做什么用的? 在项目中都有哪些使用场景?
4. 线程和协程的使用场景?
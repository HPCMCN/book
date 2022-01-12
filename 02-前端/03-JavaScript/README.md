# JavaScript

简称js, 原名livescript

#### 组成

* ECMAscript javascript的语法(变量、函数、循环语句等语法)
* DOM文档对象模型 操作HTML和CSS的方法
* BOM浏览器对象模型 操作浏览器的方法

#### 特点

* 函数预解析: 函数先调用, 后定义(只能用于函数)

  变量预解析: 如果变量调用在定义之间会报返回undefault, 如果后面没有定义, 直接报错

  匿名函数:  没有名字的函数

* "+": 在任何情况下都会执行加法, 自动类型转化, 不能转换的类型直接报错

* 逻辑运算符没有优先级

* 数组在修改时最好用提供的那些方法, 不要强制修改, 有时会不起作用. 注意列表中只有splice/indexOf能进行索引操作

* 用.获取函数中的内容  这种方式叫链式编程

* JS不能链式调用

* 类型转换 parseInt()/parseFloat()  // 整形/浮点型(如果放入的是整形的,原样输出,可以先*100/100解决)

  alert(parseInt("123abc"))   // 123

  alert(parseInt("abc123"))   // NaN

* 入口函数: ID.onclick = function(){xxx}

* 函数定义: function fnResult(a, b){xx}

* 获取类型: typeof()


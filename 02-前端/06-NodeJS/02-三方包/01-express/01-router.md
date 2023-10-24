# 1. 路由

# 2. 拆分

* router-1

  ```js
  # books.js
  const express = require("express");
  
  const router = express.Router();
  
  router.all("/", (req, res)=>{
      res.json({
          list: [{
              "id": 1,
              "name": "xi you ji2"
          }]
      })
  })
  
  module.exports = router
  
  ```

* router-2

  ```js
  # demo.js
  const express = require("express");
  const router = express.Router()
  
  router.all("/", (req, res)=>{
      res.json({
          list: {
              "id": 1,
              "name": "cheshi"
          }
      })
  })
  
  module.exports = router
  
  ```

* router-总路由

  ```js
  # main.js
  const express = require("express")
  
  const app = express();
  const demo = require("./demo")
  const books = require("./books")
  
  app.use("/t1", demo)
  app.use("/t2", books)
  
  
  app.listen(3000, (req, res)=>{
      console.log("服务已启动!")
  })
  
  ```

* 启动服务

  ```shell
  npm start
  ```

# 3. 中间件

## 3.1 app级别

### 3.1.1 内置

* static

  ```js
  const express = require("express");
  
  const app = express();
  
  app.use(express.static("static", {
      extensions: ["html", "htm"]
  }))
  
  app.all("/test", (req, res)=>{
      res.json({message: "test"})
  });
  
  app.listen(3000, "0.0.0.0", (req, res)=>{
      console.log("启动成功!")
  });
  ```

### 3.1.2 自定义

* 方式一

  ```js
  const express = require("express");
  
  const app = express();
  
  function foo_middleware(req, res, next){
      console.log("请求: ", req.url);
      next();
  }
  app.use(foo_middleware);
  
  app.all("/test", (req, res)=>{
      res.json({message: "test"})
  });
  
  app.listen(3000, "0.0.0.0", (req, res)=>{
      console.log("启动成功!")
  });
  ```
  
* 方式二

  ```js
  const express = require("express");
  
  const app = express();
  
  
  // 中间件的结构
  // 1. 函数
  // 2. 接受 req, res, next(function, 交给下个中间件或者函数继续执行)
  
  function foo_middleware(req, res, next){
      let {name} = req.query;
      if (!name || !name.length){
          res.json({
              message: "缺少name参数!",
          });
      }else{
          next();
      }
  }
  
  app.all("*", foo_middleware);
  app.all("/test", (req, res)=>{
      res.json({message: "test"})
  });
  
  app.listen(3000, "0.0.0.0", (req, res)=>{
      console.log("启动成功!")
  });
  ```

## 3.2 路由级别

```js
const express = require("express");

const app = express();

// 在定义路由时, 第二个参数表示中间件, 支持多个
app.all("/test", [function (req, res, next) {
    console.log("请求成功");
    next();
}], (req, res)=>{
    res.json({message: "test"})
});

app.listen(3000, "0.0.0.0", (req, res)=>{
    console.log("启动成功!")
});
```




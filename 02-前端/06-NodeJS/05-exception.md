# 异常捕获

```js
const express = require("express");

const app = express();

function exception_handler_middleware(err, req, res, next){
    if (err){
        res.status(500).json({
            message: "服务器异常"
        })
    }else{

    }
};

// 在定义路由时, 第二个参数表示中间件
app.all("/test", (req, res)=>{
    throw new Error("服务器异常")
});
// 异常处理必须要放到最后, 表示上层中间件无法处理时, 最后才处理
app.use(exception_handler_middleware);

app.listen(3000, "0.0.0.0", (req, res)=>{
    console.log("启动成功!")
});

```


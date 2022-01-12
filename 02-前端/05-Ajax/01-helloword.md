```js
$.ajax({
    url: "myJson.json",
    type:"GET",
    dataType:"json",
    success:function(){
        alert("成功")
        }
    error: function(){
        alert("失败")
    }
})

$.ajax({
    url:"myJson.json"
    type:"GET",
    dataType:"json",  跨域通信使用jsonp
    // jsonpCallback:"aa"   获取url中的aa函数, 需要获取这个函数时用
    
    .done(function(data){      // 成功之后
        alert(data.name)
        }
    .fail(function(){          // 失败之后
        alert("读取失败!")
    }
})
```


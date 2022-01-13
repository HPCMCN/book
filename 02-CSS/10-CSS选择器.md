### 选择器

```html
标签选择器:   div{xxx}

类选择器:    .name{xxx}

层级选择器:  .d p{xxx}

组选择器:    标签1,标签2...{xxx}

id选择器:    #d

伪类选择器/伪元素选择器:
        a{ color: red;font-size: 30px;}
        a:hover{color:green;}              // 鼠标触摸修改css样式
        a::before/after{content: xxxxxxx;} // 文字前/后加字, 不可复制
```





### 匹配

```html
各行换色:        div: nth-child(2n+1){background: green}    // 不是别子元素类型
                    div: nth-type-of(2n+1){background: green}  // 只识别div类型的
    最后一个:        div: last-child{}
    第一个:          div: first-child{}
    所有div空子集:   div: empty{}
    div中没有s元素:  div: not(s)
                表单选择
    表单失效:        input: disabled{}
    表单启用:        input: enabled{}
    表单选中:        input: checked{}
    选中表单时, 让for连接ID的lable字体变色: input: checked+label{color: red}

E:nth-child(n)：匹配元素类型为E且是父元素的第n个子元素
E:nth-last-child(n)：匹配元素类型为E且是父元素的倒数第n个子元素（与上一项顺序相反）
E:first-child：匹配元素类型为E且是父元素的第一个子元素
E:last-child：匹配元素类型为E且是父元素的最后一个子元素
E:only-child：匹配元素类型为E且是父元素中唯一的子元素
E:nth-of-type(n)：匹配父元素的第n个类型为E的子元素
E:nth-last-of-type(n)：匹配父元素的倒数第n个类型为E的子元素（与上一项顺序相反）
E:first-of-type：匹配父元素的第一个类型为E的子元素
E:last-of-type：匹配父元素的最后一个类型为E的子元素
E:only-of-type：匹配父元素中唯一子元素是E的子元素
E:empty 选择一个空的元素
E:enabled 可用的表单控件
E:disabled 失效的表单控件
E:checked 选中的checkbox
E:not(s) 不包含某元素
E:target 对应锚点的样式
E > F E元素下面第一层子集
E ~ F E元素后面的兄弟元素
E + F 紧挨着的兄弟元素
E[data-attr] 含有data-attr属性的元素
E[data-attr='ok'] 含有data-attr属性的元素且它的值为“ok”
E[data-attr^='ok'] 含有data-attr属性的元素且它的值的开头含有“ok”
E[data-attr$='ok'] 含有data-attr属性的元素且它的值的结尾含有“ok”
E[data-attr*='ok'] 含有data-attr属性的元素且它的值中含有“ok”
```

示例

```html
<style type="text/css">
        div[data-attr='ok']{
            color:red;
        }
</style>
<div data-attr="ok">这是一个div元素</div>
```

#### 雪碧图

```html
雪碧图(图像精灵): 一张图片使用不同部位(Image sprites)
    7.1 图像精灵是放入一张图片放入多个部分
    7.2 包含大量图像的网页需要更长时间, 可以减少图片量下载时间
    7.3 减少服务器访问量, 减少宽带占用率
```


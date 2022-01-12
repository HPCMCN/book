#  [JQuery](https://code.jquery.com/)

javascript和jQuery对比:   比原生的更快

* JavaScript

  ```js
  window.onload = function(){xxx}  (文档加载完成后执行   比jQ慢)
  ```

* JQuery

  ```js
  $(document).ready(function(){xx}) ==> $().ready(function(){xx}) ==> $(function(){xx})(文档加载完成执行  比js快)
  ```

常见使用方法

```js
$(window).xxx()		// 检测当前窗口
$(document).xxx()	// 检测当前文档DOM
$("div").xxx()		// 检测当前标签
```


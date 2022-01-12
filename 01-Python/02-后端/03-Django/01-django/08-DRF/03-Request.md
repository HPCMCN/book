# 1. Request

REST Framework 使用Parser解析器将数据按照Content-Type类型进行解析, 然后保存到Request对象中用于调度

其中Request方法对应如下

| 方法                   | 类型 | 说明                                              |
| ---------------------- | ---- | ------------------------------------------------- |
| `request.data`         | dict | 包含files, form, json(post, put, patch请求)的数据 |
| `request.query_params` | dict | get请求的url参数                                  |
|                        |      |                                                   |
|                        |      |                                                   |
|                        |      |                                                   |
|                        |      |                                                   |
|                        |      |                                                   |


# package.json

## 1. 编写包配置

* version

  当前编写包的版本

* name

  编写包的名称

* author

  作者信息

  ```js
  {
  	"author": "xxx"
  }
  ```

  或者

  ```js
  {
  	"author": {
  		"name": "xx",
  		"email": "xx",
  		"url": "xxx"
  	}
  }
  ```

  

* contributors

  贡献者, 使用方式同author

* description

  便携包的描述信息

* main

  入口位置

* homepage

  设置软件包的主页

* license

  指定软件包的许可协议

* keywords

  npm网站提交后, 用关键字可以查询到本项目

  ```js
  {
      "keywords": [
          "email"
      ]
  }
  ```

* bugs

  连接问题提交地址, github insure

* repository

  仓库所在的位置

  ```js
  {
      "repository": "github:nodejscn/node-api-cn"
  }
  ```

  或者

  ```js
  "repository": {
    "type": "git",
    "url": "https://github.com/nodejscn/node-api-cn.git"
  }
  ```

## 2. 环境配置

* dependencies

  正式环境依赖的包

* devDependencies

  开发环境依赖的包

* engines

  nodejs 环境的版本配置

  ```js
  "engines": {
    "node": ">= 6.0.0",
    "npm": ">= 3.0.0",
    "yarn": "^0.13.0"
  }
  ```

* browserslist

  支持的浏览器版本

  ```js
  {
      "browserslist": [
    		"> 1%",
    		"last 2 versions",
    		"not ie <= 8"
  	]
  }
  ```

### scripts

自定义运行命令

```shell
{
    "scripts": {
    	"xx": "node src/helloworld.js"
    }
}
```

运行指定命令

```shell
node run xx
```
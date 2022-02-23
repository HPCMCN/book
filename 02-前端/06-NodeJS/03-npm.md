# npm

* -g: 全局安装, 利用`npm root -g`可以查看全局安装的位置
* -D: dev环境安装
* -S:  生产环境安装

注意: 虚拟机中安装包时, 需要先禁用链接, 否则会报错

```shell
[appgess@master01 03-routers]$ npm install express@4.17.3 --save
npm ERR! code ENOTSUP
npm ERR! syscall symlink
npm ERR! path ../mime/cli.js
```

禁用链接

```shell
npm config set bin-links false
```

### install

```shell
npm install gitbook --save
```

* --save: `package.json`中的`dependencies`, 表示生产中使用的库

* --save-dev: `package.json`中的`devDependencies`, 表示测试环境中的使用库

  ```shell
  npm install gitbook --save
  ```

  * --save: `package.json`中的`dependencies`, 表示生产中使用的库
  * --save-dev: `package.json`中的`devDependencies`, 表示测试环境中的使用库

### update

```shell
npm update gitbook
```


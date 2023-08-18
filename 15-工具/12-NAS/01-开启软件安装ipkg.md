1. 下载bootstrap

   ```shell
   wget http://ipkg.nslu2-linux.org/feeds/optware/syno-i686/cross/unstable/syno-i686-bootstrap_1.2-7_i686.xsh
   wget http://ipkg.nslu2-linux.org/optware-ng/bootstrap/buildroot-x86_64-bootstrap.sh
   ```

2. 安装

   ```shell
   sh syno-i686-bootstrap_1.2-7_i686.xsh
   sh buildroot-x86_64-bootstrap.sh
   ```

3. 更新源

   ```shell
   ipkg update
   ```

4. 安装 gettext 

   用来修复 wget命令的ssl异常

   ```shell
   ipkg install gettext
   ```

5. 修复wget

   ```shell
   ipkg install wget-ssl
   ```

6. 测试wget命令

   ```shell
   wget https://www.baidu.com
   ```

   


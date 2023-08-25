1. 安装依赖

   ```shell
   ipkg install make gcc gcc-c++ flex bison file libtool libtool-libs autoconf kernel-dev libjpeg  libpng libpng-dev gd freetype  libxml2 zlib glib2  bzip2  libevent ncurses  curl  e2fsprogs e2fsprogs-dev krb5-dev libidn libidn-dev openssl gettext gettext-dev ncurses-dev unzip libcap pcre-dev openssl-dev zlib-dev
   ```

   注: 如果出现卡顿, 可以直接复制download地址, 使用浏览器下载好, 然后执行:

   ```shell
   ipkg install ./zlib-dev_1.2.11-2_x86_64.ipk
   ```

2. 下载nginx

   ```shell
   cd /opt
   wget https://nginx.org/download/nginx-1.24.0.tar.gz
   
   tar -zxf nginx-1.24.0.tar.gz
   cd nginx-1.24.0
   ```

3. 编译安装

   ```shell
   ./configure --prefix=/usr/local/nginx   --user=nginx --group=nginx --with-http_ssl_module --with-http_realip_module  --with-http_gzip_static_module  --with-http_dav_module  --with-http_stub_status_module  --with-http_addition_module --with-http_sub_module  --with-http_flv_module  --with-http_mp4_module  --with-pcre --with-stream
   ```

4. 安装

   ```shell
   make -j4 && make install
   ```

5. 替换原有的nginx

   ```shell
   mv /bin/nginx /bin/nginx_bak
   ln -s /usr/local/nginx/sbin/nginx /bin/nginx
   ```

6. 检查确认

   ```shell
   nginx -V
   ```

   


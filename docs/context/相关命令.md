## docker

###  docker安装mysql

```shell
docker run -d \
    --name mysql \
    -p 3306:3306 \
    -e TZ=Asia/Shanghai \
    -e MYSQL_ROOT_PASSWORD=123 \
    mysql
```

`docker run`:创建并运行一个容器，`-d`是让容器在后台运行

`-p 3306:3306`:设置端口映射，前为宿主机端口

`-e`:设置环境变量 

```shell
docker run -d \
    --name nginx \
    -p 80:80 \
    nginx
```

格式化展示内容

```shell
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}\t{{.Status}}"
```



**启动容器**

```shell
docker start 容器名
```

**docker start** :启动一个或多个已经被停止的容器

**docker stop** :停止一个运行中的容器

**docker restart** :重启容器



### 进入容器

```shell
docker exec -it mysql bash
```

**docker inspect :** 获取容器/镜像的元数据。

```shell
docker inspect mysql
```

![image-20240114212423816](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401142124933.png)



```shell
docker run -dit \
-v $PWD/ql/config:/ql/config \
-v $PWD/ql/log:/ql/log \
-v $PWD/ql/db:/ql/db \
-p 5700:5600 \
--name qinglong \
--hostname qinglong \
--restart always \
whyour/qinglong:latest
```



```dockerfile
from openjdk:11.0-jre-buste
```

## docker部署TTRSS 

```yaml
version: "3"
services:
  service.rss:
    image: wangqiru/ttrss:latest
    container_name: ttrss
    ports:
      - 11201:80 # 按需修改
    environment:
      - SELF_URL_PATH=https://my.kingone.website/ # 按需修改
      - DB_PASS=rss2024 # 按需修改。与下面的密码对应
      - PUID=1000
      - PGID=1000
      - ALLOW_PORTS=11200,3000  # 加入这个配置,才能访问rsshub和huginn默认的1200,3000端口
    volumes:
      - ./feed-icons:/var/www/feed-icons/
    networks:
      - public_access
      - service_only
      - database_only
    stdin_open: true
    tty: true
    restart: always

  service.mercury:
    image: wangqiru/mercury-parser-api:latest
    container_name: mercury
    networks:
      - public_access
      - service_only
    restart: always

  service.opencc:
    image: wangqiru/opencc-api-server:latest
    container_name: opencc
    environment:
      - NODE_ENV=production
    networks:
      - service_only
    restart: always

  database.postgres:
    image: postgres:13-alpine
    container_name: postgres
    environment:
      - POSTGRES_PASSWORD=rss2024 # 按需修改。与上面的密码对应
    volumes:
      - ./db/:/var/lib/postgresql/data
    networks:
      - database_only
    restart: always

networks:
  public_access: 
  service_only: 
    internal: true
  database_only: 
    internal: true
```

上线服务：

```shell
docker-compose up -d
```

可以通过这个命令查看日志：

```shell
docker-compose logs -f
```

改变文件夹的权限。这一步一定要做，否则TTRSS无法成功启用。

```shell
sudo chmod 777 feed-icons
```

重启应用：

```shell
docker-compose restart
```





### 已生成的 Container

#### 1. 永久设定环境变量

修改 `/etc/profile` 或者 `~/.bashrc` 文件，在其中加入

```shell
export http_proxy="http://192.168.3.100:7890"
export https_proxy="https://192.168.3.100:7890"
```



#### 2. 临时设定

在进入镜像后手动设置环境变量：

```shell
export http_proxy="http://192.168.3.100:7890"
export https_proxy="https://192.168.3.100:7890"
```

或者配合 VSCode 的 Remote-Container 插件配置后可以实现每次**自动设置**，具体方式请移步 [Docker 配合 VSC 开发最佳实践](https://anthonysun256.github.io/docker-with-vsc_best-practice/)





qinglong密码

20240114

centos密码

20240106

```text
pt_token=AAJlo-0gADAT_o6cBtv7DYQfh43SABQENrjingBXPD2mtGq8Rt-kUtuySsYOR8E-jeKpic7UoqU;pt_pin=wduaWYelLTIjTq;
```

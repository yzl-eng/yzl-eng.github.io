![image-20230601170729722](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922326.png)

## MySQL集群版安装环境配置

**MySQL集群版安装过程的所有操作步骤都需要使用root用户进行。**

**本项步骤需要在集群中所有主机上进行操作。**

```shell
mkdir setups
```

![image-20230601164506237](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922327.png)

首先，我们把相关软件包上传到root用户家目录的新建`setup`目录下。

![image-20230601164722483](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922328.png)

命令:

```shell
rpm -qa | grep mysql
#匹配mysql关键字查询包
yum list installed | grep mysql
#列出本机yum方式安装的MySQL软件
```

![image-20230601164913360](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922329.png)

```shell
rpm -e --nodeps 软件包名
#将已经安装的MySQL软件删除，源码安装删除方法
yum -y remove mysql
#将已经安装的MySQL软件删除，yum源安装删除方法
```





```shell
rpm -qa | grep mariadb
```

检查是否已经安装了`MariaDB`软件，该数据库软件是`CentOS 7.2`默认自带的数据库，会与`MySQL`软件的数据库内核产生冲突，在安装`MySQL`数据库之前需要将其删除

![image-20230601165030878](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922330.png)

```shell
rpm -e --nodeps mariadb-libs-5.5.56-2.el7.x86_64
```

将已经安装的`MariaDB`软件删除，`rpm`源码安装删除方法

![image-20230601165212800](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922331.png)

```shell
rpm -qa | grep libaio
#检查本机是否yum方式安装了libaio软件，
yum list installed | grep libaio
#MySQL数据库的安装需要依赖于该软件。
```

![image-20230601165419928](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922332.png)

若该软件还没有安装，则使用此命令进行安装。`libaio-0.3.109-13.el7.x86_64.rpm`我们已存放于用户家目录的`setup`目录下。

```shell
rpm -ivh 软件包路径
```





```shell
cat /etc/group | grep mysql 
#检查mysql用户组是否存在，
groupadd mysql
#若不存在则使用此命令创建mysql用户组。
cat /etc/passwd | grep mysql
#检查mysql用户是否存在，
useradd -r -g mysql mysql
#若不存在则使用此命令创建mysql用户并加入到mysql用户组中，选项“-r”表示该用户是内部用户，不允许外部登录。
```

![image-20230601165652983](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922333.png)

若`mysql`用户存在但不属于`mysql`用户组，则使用此命令修改`mysql`用户其所属的用户组为`mysql`。

```shell
usermod -g mysql
```



```shell
sestatus -v
```

查看当前系统中SELinux服务的运行状态，需要进行永久关闭。

![image-20230601165847258](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922334.png)

```shell
vi /etc/selinux/config
```

找到配置项`SELINUX`所在行，将其改为以下内容:

> SELINUX=disabled

![image-20230601170025061](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922335.png)

```shell
reboot
```



## MySQL集群版基本安装配置

**以下步骤需要在集群中所有主机上进行操作。**

`MySQL Cluster`软件包`mysql-cluster-gpl-7.5.7-linux-glibc2.12-x86_64.tar.gz`我们已提前上传于用户家目录的`setup`目录下。

![image-20230601170305065](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922336.png)

命令:

```shell
mkdir /mysql
#创建用于存放MySQL相关文件的目录
cd /mysql
#进入该目录
tar -xzf ~/setups/mysql-cluster-gpl-7.5.7-linux-glibc2.12-x86_64.tar.gz
#将软件包解压到mysql目录下
```

![image-20230601172009593](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922337.png)

![image-20230601171948428](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922338.png)

```shell
cd /usr/local
#进入系统的“/usr/locl目录
ln -s /mysql/mysql-cluster-gpl-7.5.7-linux-glibc2.12-x86_64 mysql
#在该目录下创建一个名为“ mysql”的链接指向MySQL Cluster所在的目录，MySQL源路径以MySQL Cluster软件包实际解压解包的路径为准。
cd mysql
#进入链接的mysql目录
mkdir data
#创建存放MySQL数据库数据的目录
chmod 770 data
#更改该数据目录的权限设置
chown -R mysql .
#更改当前“mysq目录的所属用户和所属组
chgrp -R mysql .
```

![image-20230601172704235](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922339.png)

```shell
vi /etc/profile
#配置MySQL相关的环境变量，修改系统的配置文件
```

在文件末尾添加以下内容:

```shell
#mysql-cluster environment
MYSQL_CLUSTER_HOME=/usr/local/mysql
#确保此项输入正确，否则可能会导致所有命令无法使用。
PATH=$MYSQL_CLUSTER_HOME/bin:$PATH
export MYSQL_CLUSTER_HOME PATH 
#必须按照前面的定义顺序书写。
```

![image-20230601173301171](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922340.png)

```shell
source /etc/profile
#使新配置的环境变量立即生效
echo $MYSQL_CLUSTER_HOME
#查看新添加和修改的环境变量是否设置成功，以及环境变量的值是否正确。
echo $PATH
```

![image-20230601173536528](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922341.png)

![image-20230601173556401](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922342.png)

![image-20230601173614923](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922343.png)



## 配置管理节点Cluster-01

**以下步骤需要在集群中所有管理节点主机(一号机)上进行操作。**



```shell
cd /usr/local/mysql
#进入MySQL Cluster软件所在目录
mkdir mysql-cluster
#创建存放MySQL Cluster数据的目录
chown -R mysql mysql-cluster
#更改“ mysql-cluster目录的所属用户和所属组
chgrp -R mysql mysql-cluster
```

![image-20230601174245887](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922344.png)

```shell
mkdir etc
#创建用于存放MySQL Cluster管理节点配置文件的目录
cd etc
#进入该目录
touch config.ini
#创建MySQL Cluster管理节点的配置文件
vi config.ini
#对配置文件进行修改
```

在其中添加如下内容:

```shell
[NDB_MGMD DEFAULT]
DataDir=/usr/local/mysql/data
[NDBD DEFAULT]
NoOfReplicas=2
DataMemory=512M
IndexMemory=32M
DataDir=/usr/local/mysql/data

[NDB_MGMD]
NodeId=1
HostName=LZY-01

[NDBD]
NodeId=2
HostName=LZY-02

[NDBD]
NodeId=3
HostName=LZY-03

[MYSQLD]
NodeId=4
HostName=LZY-04

[MYSQLD]
NodeId=5
HostName=LZY-05
```

![image-20230601175721551](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922345.png)

```shell
chown -R mysql .
#更改当前etc目录的所属用户和所属组
chgrp -R mysql .
ndb_mgmd -f /usr/local/mysql/etc/config.ini --initial
#启动MySQL Cluster的管理节点
```

![image-20230601175810793](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922346.png)

首次启动或配置修改之后启动需要添加参数`--
initial`，正常启动时不需要添加参数`--initial`。

```shell
ndb_mgmd -f /usr/local/mysql/etc/config.ini
```



```shell
ps -ef | grep ndb_mgmd
#查看系统进程信息，若存在信息中包含“ndb_mgmd关键字的进程则表示MySQL Cluster的管理节点启动成功。
```

![image-20230601180048097](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922347.png)

```shell
ndb_mgm
#进入MySQL Cluster管理节点的控制台
```

![image-20230601180111776](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922348.png)

```shell
#在控制台中使用命令show可以查看节点状况。
show
exit
#在控制台中使用命令exit可以退出控制
```

![image-20230601180140140](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922349.png)



## 配置数据服务节点Cluster-02 Cluster-03

**以下步骤需要在集群中所有数据服务节点(2,3号机)主机上进行操作**

```shell
cd /etc
#进入系统配置文件所在目录
touch my.cnf
#创建MySQL Cluster数据服务节点的配置文件
vi my.cnf
#对配置文件进行修改
```

在其中添加如下内容:

```shell
[MYSQLD]
ndbcluster               #运行NDB存储引擎
ndb-connectstring=LZY-01 #指定管理节点地址

[MYSQL_CLUSTER]
ndb-connectstring=LZY-01
```

![image-20230601181125130](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922350.png)

```shell
ndbd --initial
#启动数据服务节点
```

首次启动或配置修改之后启动需要添加参数`--initial` , 正常启动时不需要添加参数`--initial`

```shell
ndbd
```

![image-20230601181241428](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922351.png)

![image-20230601181255641](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922352.png)

```shell
ps -ef | grep ndbd
```

查看系统进程信息，若存在信息中包含`ndbd`关键字的进程则表示`MySQL Cluster`的**数据服务节点**启动成功。

![image-20230601181357488](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922353.png)

![image-20230601181407919](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922354.png)

```shell
ndb_mgm
#在管理节点主机上使用命令“ndb_mgm”进入MySQL Cluster管理节点的控制台。
```

![image-20230601181526463](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922355.png)

![image-20230601181537757](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922356.png)

```shell
show
#在控制台中使用命令“show”可以查看节点状况，若有相应数据服务节点的连接信息
exit
```

![image-20230601181608735](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922357.png)



## 配置SQL服务节点Cluster-04、Cluster-05

**以下步骤需要在集群中所有SQL服务节点(4,5号机)主机上进行操作**

```shell
cd /etc
#进入系统配置文件所在目录
touch my.cnf
#创建MySQL Cluster数据服务节点的配置文件
vi my.cnf
#对配置文件进行修改
```

在其中添加如下内容:

```shell
[MYSQLD]
basedir=/usr/local/mysql
datadir=/usr/local/mysql/data
ndbcluster
#运行NDB存储引擎
ndb-connectstring=LZY-01
#指定管理节点地址
[MYSQL_CLUSTER]
ndb-connectstring=LZY-01
```

![image-20230601184129117](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922358.png)

```shell
mysqld --initialize --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data
```

对MySQL数据库的安装进行初始化，执行该命令后会有一些提示信息，特别注意最后一行的`[Note]`相关信息，信息内容如下:
`[Note] A temporary password isgenerated for root@localhost:XXXXXXXXXXXXXX`
信息末尾的`XxXXXXXXXXXXXX`安装程序随机生成的**初始密码**，在首次以root用户登录数据库时需要使用，**非常重要，一定要记下。**

![image-20230601182649159](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922359.png)

m5dle8Os(V*J

![image-20230601182731813](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922360.png)

y!j)-fRp!4e#

```shell
cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysql
#将MySQL加入到系统的可控制启动服务目录内，并将服务名命名为“mysql 。
service mysql start
#启动SQL服务节点
ps -ef | grep mysql
#查看系统进程信息，若存在信息中包含“mysq关键字的进程则表示MySQLCluster的SQL服务节点启动成功。
```

![image-20230601182843068](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922361.png)

![image-20230601182858807](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922362.png)



在**管理节点(1号机)**主机上使用命令`ndb _mgm`

```shell
ndb_mgm
```

进入MySQL Cluster管理节点的控制台

```shell
show
#在控制台中使用命令“show 可以查看节点状况，若有相应SQL服务节点的连接信息，则表示SQL服务节点启动并连接成功。
exit
```

![image-20230601184302600](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922363.png)

注意:只有本步骤的验证是在集群中管理节点主机上进行操作，之后的操作仍然是在SQL服务节点主机继续操作。



```shell
mysql -u root -p
```

登录MySQL数据库，会提示输入密码，该密码为之前进行安装初始化时所显示的**初始密码**,正确输入密码成功登录MySQL数据库之后会进入MySQL的控制台。

```shell
SET PASSWORD=PASSWORD('123456');
```

在MySQL控制台使用此命令，重新设置数据库的“root用户的登录密码，其中`123456`部分为自定义的新密码。
多个SQL服务节点的root用户密码不需要设置为相同密码。

![image-20230601185126148](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922364.png)

```shell
USE mysql;
#在MySQL控制台使用命令USE mysql;切换到mysql数据库。
UPDATE user SET host='%' WHERE user='root';
#在MySQL控制台使用此命令，修改数据库的root用户所接收请求来源的范围。允许远程登录。
select host from user where user = 'root';
#查看数据库的host信息
FLUSH PRIVILEGES;
#在MySQL控制台使用此命令，刷新数据库的权限信息使新配置的权限生效。
exit
```

![image-20230601185303541](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922365.png)



```shell
systemctl start firewalld
firewall-cmd --zone=public --add-port=3306/tcp --permanent
#添加系统防火墙的端口策略，对外开启MySQL所使用的端口“3306。
firewall-cmd --reload
#重启系统防火墙服务，使新添加的端口策略生效。
```

![image-20230601185533226](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922366.png)



## MySQL集群版验证

在任意一台**SQL服务节点主机**上使用命令`mysql -u root -p`登录到MySQL数据库，会提示输入密码，正确输入密码成功登录MySQL数据库之后会进入MySQL的控制台。

```shell
mysql -u root -p
```

```shell
CREATE DATABASE test;
#在MySQL控制台使用命令CREATEDATABASE test;创建数据库test。
```

![image-20230601200746983](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922368.png)

```shell
mysql -u root -p
```

在任意一台其它SQL服务节点主机上使用命令`mysql -u root -p`登录到MySQL数据库，会提示输入密码，正确输入密码成功登录MySQL数据库之后会进入MySQL的控制台。

```shell
SHOW DATABASES;
```

在MySQL控制台使用命令`SHOW DATABASES;`显示数据库列表，若存在名为`test`的数据库，则表示集群同步数据成功。

![image-20230601200758509](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922369.png)

可以使用命令`ssh目标主机名P地址`远程登录到集群中其它sQL服务节点主机进行操作，完成所有操作后使用命令`logout`退出当前登录。



### 查看mysql集群状态

在任意一台集群主机上执行:

```shell
ndb_mgm -e show
```



### 启动顺序

1. 先启动管理节点
2. 再启动两个数据服务节点
3. 最后启动SQL节点

```shell
ndb_mgmd -f /usr/local/mysql/etc/config.ini
ndbd
service mysql start
```



### 关闭

关闭顺序:
SQL节点->数据节点->管理节点

在SQL服务节点执行:

```shell
service mysql stop
```

在管理节点执行:

```shell
ndb_mgm -e shutdown
```



## MySQL集群测试

### 测试一
现在我们在其中一个SQL节点上进行相关数据库的创建,然后到另外一个SQL节点上看看数据是否同步。
在SQL节点1上执行:

```shell
/usr/local/mysql/bin/mysql -u root -p 
show databases;
create database aa;
use aa;
CREATE TABLE ctest2 (i INT) ENGINE=NDB;
#这里必须指定数据库表的引擎为NDB,否则同步失败
INSERT INTO ctest2 () VALUES (1);
SELECT * FROM ctest2;
```

![image-20230601201008225](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922370.png)

然后在SQL节点2上看数据是否同步过来了

![image-20230601201120491](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922371.png)

### 测试二
关闭一个数据节点，在另外一个节点写输入，开启关闭的节点，看数据是否同步过来。
首先把数据节点1重启，然后在节点2上添加数据

在SQL节点2上操作如下:

```shell
create database bb;
use bb;
CREATE TABLE ctest3 (i INT) ENGINE=NDB;
use aa;
INSERT INTO ctest2 () VALUES (3333);
SELECT * FROM ctest2;
```

![image-20230601201516007](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922372.png)

等数据节点1启动完毕，启动数据节点1的服务

```shell
/usr/local/mysql/bin/ndbd --initial
service mysqld start
```


然后登录进去查看数据

```shell
/usr/local/mysql/bin/mysql -u root —p
```

可以看到数据已经同步过来了，说明数据可以双向同步了。

![image-20230601201756938](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922373.png)
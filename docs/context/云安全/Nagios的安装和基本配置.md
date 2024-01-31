## centos7配置本地yum源



### 手动配置

步骤一：在centos虚拟机中挂载光盘

1.创建挂载点目录

```shell
mkdir /media/cdrom/
# df /media/cdrom
```

![image-20230511181703206](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909710.png)

2.挂载光盘

![image-20230516172241223](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909711.png)



```shell
mount /dev/cdrom /media/cdrom
```

![image-20230516172149082](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909712.png)

3.查看挂载记录

```shell
df -hT /media/cdrom
```

![image-20230516172212198](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909713.png)

4. 备份原本地源

   ```shell
   cp -rf /etc/yum.repos.d  /etc/yum.repos.d_$(date '+%Y%m%d_%H%M%S')
   ```

5. 删除默认原本地源

   ```shell
   rm -rf /etc/yum.repos.d/*
   ```

6. 配置本地源，创建Media.repo文件

   ```shell
   vi /etc/yum.repos.d/Media.repo
   ```

7. 配置如下内容：

   ```shell
   [iso]
   name=Media
   baseurl=file:///media/cdrom/
   gpgcheck=0
   enabled=1
   ```

8. 加载本地yum源&测试

   ```shell
   # 清除yum缓存
   yum clean all
   # 缓存本地yum源
   yum makecache
   # 测试yum本地源 
   yum list
   ```

   

### 自动配置yum

```shell
vi /root/auto_source.sh
```

```shell
#!/bin/bash
# 创建本地源文件夹
mkdir -p /media/cdrom/
# 挂载镜像文件至指定的目录
mount /dev/cdrom /media/cdrom
# 备份原本地源
cp -rf /etc/yum.repos.d  /etc/yum.repos.d_$(date '+%Y%m%d_%H%M%S')
# 删除默认原本地源
rm -rf /etc/yum.repos.d/*
# 配置本地源,创建Media.repo文件,并配置如下内容
cd /etc/yum.repos.d/
>Media.repo
echo '[iso]'                            >> Media.repo
echo 'name=Media'                       >> Media.repo
echo 'baseurl=file:///media/cdrom/'    >> Media.repo
echo 'gpgcheck=0'                       >> Media.repo
echo 'enabled=1'                        >> Media.repo
# 清除yum缓存
yum clean all
# 缓存本地yum源
yum makecache
```

1. 赋予脚本可执行的权限

```shell
chmod +x /root/auto_source.sh
```

2. 执行脚本文件，即可

```shell
/root/auto_source.sh
```







## Nagios-server环境配置

[步骤参考](https://blog.csdn.net/weixin_43853006/article/details/90580575)

**关闭防火墙**

```shell
#查看防火墙状态
firewall-cmd --state
#停止firewall
systemctl stop firewalld.service
#禁止firewall开机启动
systemctl disable firewalld.service
#重启防火墙
firewall-cmd --reloadl
```



检查依赖环境

```shell
yum -y install gcc glibc glibc-common php php-gd perl httpd gd gd-devel openssl openssl-devel
```

![image-20230516173529008](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909714.png)

创建ngaios用户和组

```shell
useradd nagios -s /sbin/nologin
#(创建nagios用户并指定该用户不能登录系统)
groupadd nagcmd
usermod -a -G nagcmd nagios
usermod -a -G nagcmd apache
```

传入文件到指定目录

![image-20230516174054361](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909715.png)

安装Nagios

```shell
cd /root/software
tar zxvf nagios-4.3.1.tar.gz
cd nagios-4.3.1
```

![image-20230516174139486](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909716.png)



### 源码配置

```shell
#cd nagios-4.3.1
./configure --with-command-group=nagcmd
```

![image-20230516174345089](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909717.png)

编译安装

```shell
#cd nagios-4.3.1
make all
make install
```

![image-20230516174508599](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909718.png)

```shell
make install-init
```

![image-20230516174558045](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909719.png)

```shell
make install-config
```

![image-20230516174637772](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909720.png)

```shell
make install-commandmode
```

![image-20230516175059942](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909721.png)

```shell
make install-webconf
```

![image-20230516175117396](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909722.png)

```shell
ll /usr/local/nagios/
```

![image-20230516175134256](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909723.png)



### 安装邮件服务

```shell
yum -y install sendmail mailx
```

![image-20230516175505163](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909724.png)

启动服务

```shell
systemctl restart sendmail.service
systemctl status sendmail.service
```

![image-20230516175641201](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909725.png)

发送邮件测试(输入完成后按`Ctrl+D`退出并发送)

```shell
mail -s lzcu-test 1819757699@qq.com
```



指定接受警告信息的邮件地址

```shell
vi /usr/local/nagios/etc/objects/contacts.cfg 
#(修改参数email )
```



### 修改web界面登录验证信息

```shell
htpasswd -c /usr/local/nagios/etc/htpasswd.users nagios
```

![image-20230516180808126](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909726.png)

修改nagios用户权限（因为系统默认用户为nagiosadmin )配置完成后需重启http服务

```shell
sed -i 's#nagiosadmin#nagios#g' /usr/local/nagios/etc/cgi.cfg
grep nagios /usr/local/nagios/etc/cgi.cfg
```

![image-20230516180959813](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909727.png)



```shell
systemctl restart httpd.service 
#重启
```



检测主配置文件是否有语法错误

```shell
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
```

如下无警告无错误即为成功

![image-20230516181025717](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909728.png)



### 安装nagios插件

注意指令输入是所在的路径

![image-20230516183507517](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909729.png)

```shell
tar zxvf nagios-plugins-2.2.1.tar.gz
cd nagios-plugins-2.2.1
#配置
./configure --with-nagios-user=nagios --with-nagios-group=nagcmd
#编译并安装
make && make install
#查看已安装的插件数量
ls /usr/local/nagios/libexec/| wc -l
```

![image-20230516181645177](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909730.png)



### 启动验证服务

```shell
chkconfig --add nagios
chkconfig nagios on
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
```

![image-20230516181812820](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909731.png)

如果防火墙没有安装会影响后续的验证

```shell
yum -y install firewall*
systemctl start firewalld
systemctl status firewalld
```

![image-20230516181915918](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909732.png)

添加防火墙规则（开放http端口)

```shell
firewall-cmd --add-service=http
firewall-cmd --permanent --add-service=http
#重启防火墙
firewall-cmd -reload
#重启nagios服务
/usr/local/nagios/bin/nagios -d /usr/local/nagios/etc/nagios.cfg
```

打开nagios的web页面验证:`192.168.10.121:/nagios`

![image-20230516182219461](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909733.png)

### 主页

![image-20230516182312115](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909734.png)

查看本机验证信息

![image-20230516182453328](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909735.png)

查看本机服务信息

![image-20230516182553065](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909736.png)

### 安装nrpe

注意指令输入是所在的路径

![image-20230516183507517](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909729.png)

```shell
cd /root/software
tar zxvf nrpe-3.2.1.tar.gz
cd nrpe-3.2.1
./configure 
--with-nrpe-user= nagios \
--with-nrpe-group=nagios \
--with-nagios-user=nagios \
--with-nagios-group=nagios \
--enable-command-args \
--enable-ssl
```



![image-20230516183349947](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909737.png)

```shell
make all
```

![image-20230516183718603](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909738.png)

```shell
make install-plugin
make install-daemon
make install-config
#检查/usr/local/nagios/libexec目录下是否已经安装了check_nrpe插件
cd /usr/local/nagios/libexec/
ls | grep check_nrpe
```

![image-20230516184112654](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909739.png)





## Nagios-client配置安装

**先配置好yum源**



关闭防火墙和selinux

```shell
systemctl stop firewalld.service
systemctl disable firewalld.service
vi /etc/selinux/config
```

修改参数:`SELINUX=disabled`   

**重启服务器**

![image-20230516184348684](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909740.png)

配置环境

```shell
yum install gcc glibc glibc-common -y
yum install gd gd-devel openssl openssl-devel -y
yum install php php-gd perl net-tools -y
```

![image-20230516190754908](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909741.png)



传入文件

![image-20230516191106666](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909742.png)安装nagios-plugin添加nagios用户

```shell
cd /root/software/
useradd -s /sbin/nologin nagios
#解压安装
tar zxvf nagios-plugins-2.2.1.tar.gz
cd nagios-plugins-2.2.1
./configure --with-nagios-user=nagios --with-nagios-group=nagios
make && make install
```

![image-20230518214134846](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909743.png)

安装nrpe

```shell
cd /root/software/
tar zxvf nrpe-3.2.1.tar.gz
cd nrpe-3.2.1
./configure --with-nrpe-user=nagios \
--with-nrpe-group=nagios \
--with-nagios-user=nagios \
--with-nagios-group=nagios \
--enable-command-args \
--enable-ssl
```

![image-20230518212820267](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909744.png)

```shell
make all
make install-plugin
make install-daemon
#make install-daemon-config
make install-config
/usr/bin/install -c -m 775 -o nagios -g nagios -d /usr/local/nagios/etc
/usr/bin/install -c -m 644 -o nagios -g nagios sample-config/nrpe.cfg /usr/local/nagios/etc

ls /usr/local/nagios/libexec/ |grep check_nrpe
```

![image-20230518214257364](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909745.png)

![image-20230519114604824](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909746.png)

### 启动nrpe

```shell
/usr/local/nagios/bin/nrpe -d -c /usr/local/nagios/etc/nrpe.cfg
```



如果需要重启则先需要关闭相关进程，再查看端口5666是否关闭，最后使用启动命令

```shell
pkill nrpe
netstat -lntp
```



![image-20230519112043083](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909747.png)

### 排错

![image-20230518215521948](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909748.png)



##  调试验证

### 验证连通性

在`/usr/local/nagios/etc/nrpe.cfg`文件中server的ip地址

```shell
vi /usr/local/nagios/etc/nrpe.cfg
```

![image-20230518220330453](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909749.png)

重启nrpe

```shell
pkill nrpe
netstat -lntp
/usr/local/nagios/bin/nrpe -d -c /usr/local/nagios/etc/nrpe.cfg
```

### 在server主机做验证

```shell
cd /usr/local/nagios/libexec/
./check_nrpe -H 192.168.10.122
```

![image-20230518220406708](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909750.png)

```shell
echo "/usr/local/nagios/bin/nrpe -d -c /usr/local/nagios/etc/nrpe.cfg" >> /etc/rc.local
chmod +x /etc/rc.d/rc.local
netstat -Input | grep 5666
/usr/local/nagios/libexec/check_nrpe -H localhost
```

![image-20230519115153558](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909751.png)

再client端做同样的验证

![image-20230519115318616](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909752.png)

```shell
cd /usr/local/nagios/etc
ls
vi nrpe.cfg
```

注释nrpe.cfg中的一下几行

![image-20230519115737203](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909753.png)



 #### 创建监控脚本

**在client端操作**

在nrpe.cfg文件末尾增加下面几行内容︰

```shell
# my custom monitor items
command[check_users]=/usr/local/nagios/libexec/check_users -w 5 -c 10
command[check_load]=/usr/local/nagios/libexec/check_load -r -w .15,.10,.05 -c .30,.25,.20
command[check_disk]=/usr/local/nagios/libexec/check_disk -w 20% -c 10% -p /
command[check_mem]=/usr/local/nagios/libexec/check_mem.pl -w 90% -c 95%
command[check_swap]=/usr/local/nagios/libexec/check_swap -w 20% -c 10%
```

![image-20230519120618109](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909754.png)

创建一个监控内存的perl脚本

将`check_mem.pl`文件从software移到`/usr/local/nagios/libexec`

![image-20230519121253236](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909755.png)

![image-20230519121444578](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909756.png)

```shell
vi /usr/local/nagios/libexec/check_mem.pl
```

![image-20230519121604618](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909757.png)

修改脚本权限

```shell
chmod 755 /usr/local/nagios/libexec/check_mem.pl
```

重启nrpe服务

```shell
pkill nrpe
netstat -lntp
/usr/local/nagios/bin/nrpe -d -c /usr/local/nagios/etc/nrpe.cfg
```

在本机验证脚本效果

```shell
/usr/local/nagios/libexec/check_nrpe -H localhost -c check_mem
```

![image-20230519122600588](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909758.png)



#### 在server端进行脚本验证

```shell
/usr/local/nagios/libexec/check_nrpe -H 192.168.10.122
/usr/local/nagios/libexec/check_nrpe -H 192.168.10.122 -c check_disk
```

![image-20230519122852657](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909759.png)



修改nagios.cfg配置文件

```shell
vi /usr/local/nagios/etc/nagios.cfg
```

注释掉这行

![image-20230519123403821](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909760.png)

添加下面两行内容

```shell
cfg_file=/usr/local/nagios/etc/objects/services.cfg
cfg_file=/usr/local/nagios/etc/objects/hosts.cfg
```

![image-20230519123545320](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909761.png)

在`/usr/local/nagios/etc/objects`路径下创建`hosts.cfg`和`services.cfg`文件

```shell
cd /usr/local/nagios/etc/objects
touch services.cfg
head -51 localhost.cfg > hosts.cfg
chown -R nagios.nagios *
```

![image-20230519124047401](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909763.png)

修改`commands.cfg`文件，在末尾添加内容

```shell
cd /usr/local/nagios/etc/objects
vi commands.cfg
```



```shell
# "check_nrpe' command definition
define command{
command_name check_nrpe
command_line $USER1$/check_nrpe -H $HOSTADDRESS$ -c $ARG1$
}

#'check_ping' command definition
 define command{
command_name check-ping
command_line $USER1$/check_ping -H $HOSTADDRESS$ -w 100.0,20% -c 200.0,50% -p 3 -t 2
}

# "check_http' command definition
define command{
command_name  check-weburl
command_line $USER1$/check_http -H $HOSTADDRESS$ $ARG1$ -w 5 -c 10}

# 'check_tcp' command definition
define command{
command_name check-tcp
command_line $USER1$/check_tcp -H $HOSTADDRESS$ -p $ARG1$ -w 0.02 -c 0.1}
```

![image-20230519124731732](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909764.png)

#### 主机模板配置

删除`hosts.cfg`文件的下列内容

```shell
cd /usr/local/nagios/etc/objects
vi hosts.cfg +21
```

![image-20230519125044063](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909765.png)

添加如下内容

```shell
# Define some hosts
#########192.168.10.121##########
define host {
    use linux-server
    host_name nagios-server
    alias nagios-server
    address 192.168.10.121
    check_command check-host-alive
    max_check_attempts 3
    normal_check_interval 2
    retry_check_interval 2
    check_period 24x7
    notification_interval 300
    notification_period 24x7
    notification_options d,u,r
    contact_groups admins
    process_perf_data 1
}
############192.168.10.122#############
define host {
    use linux-server
    host_name nagios-client
    alias nagios-client
    address 192.168.10.122
    check_command check-host-alive
    max_check_attempts 3
    normal_check_interval 2
    retry_check_interval 2
    check_period 24x7 
    notification_interval 300
    notification_period 24x7
    notification_options d,u,r
    contact_groups admins
    process_perf_data 1
}
```

![image-20230519125725874](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909766.png)



将监控的主机添加到主机组里

```shell
vi hosts.cfg +76
```



```shell
define hostgroup{
    hostgroup_name linux-servers; The name of the hostgroup
	alias Linux Servers; Long name of the group
	members nagios,nagios-client; Comma separated list of hosts that belong to this grourp
}
```

![image-20230523152320187](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909767.png)

服务模板配置

```shell
vi services.cfg
```

写入以下内容

```shell
###########192.168.10.121##################
define service{
use generic-service
host_name nagios-server
service_description Load
check_command check_nrpe!check_load
}

define service{
use generic-service
host_name nagios-server
service_description Disk
check_command check_nrpe!check_disk
}

define service{
use generic-service
host_name nagios-server
service_description memory
check_command check_nrpe!check_mem
}

define service{
use generic-service
host_name nagios-server
service_description Ping
check_command check-ping!192.168.10.121
}

define service{
use generic-service
host_name nagios-server
service_description port_3306
check_command check-tcp!3306
}



##########192.168.10.122###############
define service{
use generic-service
host_name nagios-client
service_description Load
check_command check_nrpe!check_load
}

define service{
use generic-service
host_name nagios-client
service_description Disk
check_command check_nrpe!check_disk
}

define service{
use generic-service
host_name nagios-client
service_description memory
check_command check_nrpe!check_mem
}

define service{
use generic-service
host_name nagios-client 
service_description Ping
check_command check-ping!192.168.10.122
}

define service{
use generic-service
host_name nagios-client
service_description port_3306
check_command check-tcp!3306
}
```



重启nagios服务

```shell
systemctl daemon-reload
/etc/init.d/nagios restart
```

![image-20230523152357626](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909768.png)

![image-20230523163623348](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311909769.png)





```shell
systemctl restart httpd.service 
/usr/local/nagios/bin/nrpe -d -c /usr/local/nagios/etc/nrpe.cfg
```


## HBase基本安装配置

首先，HBase软件包`hbase-1.2.3-bin.tar.gz`我们已经上传到用户家目录的`setups`目录下。然后进行解压和环境变量设置。

命令:

```shell
mkdir ~/hbase
#创建用于存放Hbase相关文件的目录
cd ~/hbase
#进入该目录
tar -xzf ~/setups/hbase-1.2.3-bin.tar.gz
#将软件包解压到hbase目录
```

![image-20230507214231838](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918579.png)




```shell
vi ~/.bash_profile
#配置HBase相关的环境变量
```

![image-20230507214538793](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918580.png)

在文件末尾添加以下内容:

```shell
#hbase environment
# 该路径以HBase软件包实际解压解包的路径为准
HBASE_HOME=/home/admin/hbase/hbase-1.2.3
#确保此项输入正确，否则可能会导致所有命令无法使用
PATH=$HBASE_HOME/bin:$PATH
export HBASE_HOME PATH
#必须按照前面的定义顺序书写
```

![image-20230507214700789](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918581.png)

```shell
source ~/.bash_profile
#使新配置的环境变量立即生效
echo $HBASE_HOME
#查看新添加和修改的环境变量是否设置成功，以及环境变量的值是否正确
echo $PATH
#验证Hbas的安装配置是否成功
hbase version
```

![image-20230507214845236](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918582.png)

## HBase高可用完全分布模式配置

命令:

```shell
cd ~/hbase
#进入Hbase相关文件的目录
mkdir tmp logs
#分别创建HBase的元数据文件目录“tmp和HDFS的日志文件目录“logs 。
cd ~/hbase/hbase-1.2.3/conf
#进入Hbase的配置文件所在目录
ls
```

![image-20230507215027780](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918583.png)



```shell
vi hbase-env.sh
#对配置文件进行修改
```



找到配置项`JAVA_HOME`，将其值改为以下内容:（去掉注释`#`，注意顶格）

```shell
export JAVA_HOME=/home/admin/java/jdk1.8.0_131
```

该路径以JDK软件包实际解压解包的路径为准

![image-20230507215219153](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918584.png)

找到配置项`HBASE_CLASSPATH`，该项用于指定Hadoop的配置文件所在的路径，将其值改为以下内容:

```shell
export HBASE_CLASSPATH=/home/admin/hadoop/hadoop-2.7.3/etc/hadoop
```

![image-20230507215355280](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918585.png)

找到配置项`HBASE_LOG_DIR`，该项用于指定HBase的日志文件的本地存放路径，将其值改为以下内容:

```shell
export HBASE_LOG_DIR=/home/admin/hbase/logs
```

![image-20230507215516159](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918586.png)

找到配置项`HBASE_MANAGES_ZK`，该项用于关闭HBase自带的Zookeeper组件，将其值改为以下内容:

```shell
export HBASE_MANAGES_ZK=false
```

![image-20230507215615041](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918587.png)

```shell
vi hbase-site.xml
#对配置文件进行修改
```

![image-20230507215716843](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918588.png)

找到标签`<configuration>`所在的位置，在其中添加如下内容:

```xml
<configuration>
    <property>
        <name>hbase.rootdir</name>
        <value>hdfs://LZY-01:9000/user/admin/hbase</value>
        <!--注意修改相应的主机名为自己的姓名-->  
    </property>
    <property>
        <name>hbase.tmp.dir</name>
        <value>/home/admin/hbase/tmp</value>
    </property>
    <property>
        <name>hbase.cluster.distributed</name>
        <value>true</value>
    </property><property>
    <name>hbase.zookeeper.quorum</name>
    <value>LZY-01:2181,LZY-02:2181,LZY-03:2181,LZY-04:2181,LZY-05:2181</value>
    <!--注意修改相应的主机名为自己的姓名--> 
    </property>
    <property>
        <name>hbase.master.maxclockskew</name>
        <value>60000</value>
    </property>
</configuration>
```

![image-20230507215903246](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918589.png)

```shell
vi regionservers
#对配置文件进行修改
```

删除文件中原有的所有内容，然后添加集群中所有**RegionServer**节点的主机名，

每行一个主机的主机名，配置格式如下：

```shell
LZY-03
LZY-04
LZY-05
```

![image-20230507215948429](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918590.png)

```shell
touch backup-masters
#创建配置文件“backup-masters
vi backup-masters
#对配置文件进行修改
```

![image-20230507220050306](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918591.png)

添加集群中所有备用主节点的主机名，每行一个主机的主机名，配置格式如下:

```shell
LZY-02
```

![image-20230507220133767](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918592.png)

## 同步安装配置以及系统时间

将`hbase`目录和`.bash profile`文件发给集群中所有主机，发送目标用户为集群专用用户admin，即当前与登录用户同名的用户，发送目标路径为`/home/admin`即集群专用用户admin的家目录。

```shell
scp -r ~/hbase ~/.bash_profile admin@LZY-02:/home/admin
scp -r ~/hbase ~/.bash_profile admin@LZY-03:/home/admin
scp -r ~/hbase ~/.bash_profile admin@LZY-04:/home/admin
scp -r ~/hbase ~/.bash_profile admin@LZY-05:/home/admin
```

![image-20230507220416202](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918593.png)

集群中每台主机分别进行以下命令操作:

```shell
source ~/.bash_profile
#使新配置的环境变量立即生效
echo $HBASE_HOME
#查看新添加和修改的环境变量是否设置成功，以及环境变量的值是否正确。
echo $PATH
hbase version
#验证Hbas的安装配置是否成功
```

![image-20230507220541066](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918594.png)

![image-20230507220619948](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918595.png)



**时间同步项的所有操作步骤需要使用root用户进行**

在集群中所有主机上使用命令`date -s 'yyyy-MM-dd HH:mm:ss'`(年-月-日时:分:秒)对系统时间进行设置，并使用命令`hwclock -w`将设置的时间同步到硬件时钟。
该操作尽量在**所有主机上同时进行**，从而保证主机之间的时间误差值在设定的`hbase.master.maxclockske`范围内。

```shell
date -s '2023-5-7 22:10:00'
#对系统时间进行设置，时间为你自己当前时间
hwclock -w
#将设置的时间同步到硬件时钟
```

![image-20230507221037489](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918596.png)



## HBase高可用完全分布模式启动和验证

```shell
zkServer.sh status
#在集群中所有主机上使用命令“zkServer.sh status
```

status查看该节点Zookeeper服务当前的状态，若集群中只有一个`leader`节点，其余的均为`follower`节点，则集群的工作状态正常

```shell
zkServer.sh start
```

如果Zookeeper未启动，则在集群中所有主机上使用命令`zkServer.sh start`启动Zookeeper服务的脚本

```shell
start-all.sh
#主节点命令
yarn-daemon.sh start resourcemanager
#备用主节点命令
```

只需要在主节点执行启动命令

```shell
start-hbase.sh
```

![image-20230507221753111](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918597.png)

```shell
jps
```

![image-20230507223523286](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918598.png)

![image-20230507223551405](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918599.png)



**注意：**

如果主节点**HMaster**未启动，使用如下命令关闭2号机**NameNode**,

```shell
hadoop-daemon.sh stop namenode
```

重启**Hbase**

```shell
start-hbase.sh
```



进入HBase的控制台

```shell
hbase shell
```

![image-20230507224032112](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918600.png)

```shell
create 'tab', 'id', 'name'
#在控制台中使用命令“create '表名'; '列名1，列名2'..”创建表。
exit
#在控制台中使用命令“exit’退出控制台返回系统命令界面。
```

![image-20230507224055678](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311918601.png)

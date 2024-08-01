# Hadoop 介绍
Hadoop 是一个提供分布式存储和计算的开源软件框架，它具有**无共享**、**高可用（HA）**、**弹性可扩展**的特点，非常适合处理海量数量。

- Hadoop 是一个开源软件框架

- Hadoop 适合处理大规模数据

- Hadoop 被部署在一个可扩展的集群服务器上

  

## Hadoop 三大核心组件
- HDFS（分布式文件系统） ——实现将文件分布式存储在集群服务器上
- MapReduce（分布式运算编程框架 —— 实现在集群服务器上分布式并行运算
- YARN（分布式资源调度系统） —— 帮用户调度大量的 MapReduce 程序，并合理分配运算资源（CPU和内存）

## 优缺点
### 优点

1. 高容错性
   - 数据自动保存多个副本。它通过增加副本的形式，提高容错性
   - 某一个副本丢失以后，它可以自动恢复
2. 适合处理大数据
   - 数据规模：能够处理数据规模达到 GB 、 TB 、甚至 PB 级别的数据
   - 文件规模：能够处理百万规模以上的文件数量，数量相当之大
3. 可构建在廉价机器上，通过多副本机制，提高可靠性

### 缺点

1. 不适合低延时数据访问，比如毫秒级的存储数据，是做不到的

2. 无法高效的对大量小文件进行存储

   - 存储大量小文件的话，它会占用 NameNode 大量的内存来存储文件目录和块信息。这样是不可取的，因为 NameNode 的内存总是有限的
   - 小文件存储的寻址时间会超过读取时间，它违反了 HDFS 的设计目标

3. 不支持并发写入、文件随机修改

   - 一个文件只能有一个写，不允许多个线程同时写

   - 仅支持数据 append ( 追加 ) ，不支持文件的随机修改

     

# Hadoop基本安装配置

**配置表**

![image-20230414102808249](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916572.png)



首先，Hadoop软件包`hadoop-2.7.3.tar.gz`我们已经上传到用户家目录的`setups`目录下。然后进行解压和环境变量设置。
命令:

``` shell
mkdir ~/hadoop
#创建用于存放Hadoop相关文件的目录
cd ~/hadoop
#进入该目录
```

![image-20230414104248702](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916573.png)

```shell
tar -xzf ~/setups/hadoop-2.7.3.tar.gz
#将软件包解压
vi ~/.bash_profile
#配置Hadoop相关的环境变量
```

![image-20230414104349327](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916574.png)

对配置文件进行修改，在文件末尾添加以下
内容:

```shell
#hadoopnvironment
HADOOP_HOME=/home/admin/hadoop/hadoop-2.7.3
#该路径以Hadoop软件包实际doop-2.7.3解压解包的路径为准

PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
#确保此项输入正确，否则可能会导致所有命令无法使用

export HADOOP_HOME PATH
#必须按照前面的定义顺序书写
```

![image-20230414105032715](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916575.png)

```shell
source ~/.bash_profile
#使新配置的环境变量立即生效
echo $HADOOP_HOME
#查看新添加和修改的环境变量是否
echo $PATH
#设置成功，以及环境变量的值是否正确。
hadoop version
#验证Hadoop的安装配置是否成功
```

![image-20230414105202456](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916576.png)



## Hadoop高可用完全分布模式配置

命令:

```shell 
cd ~/hadoop
```

进入Hadoop相关文件的目录

```shell
mkdir tmp name data journal
```

分别创建Hadoop的**临时文件**目录`tmp`、HDFS的**元数据文件**目录`name` 、HDFS的**数据文件**目录`data`. Journal的**逻辑状态数据**目录`journal`。

![image-20230414115226165](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916577.png)

```shell
cd ~/hadoop/hadoop-2.7.3/etc/hadoop
#进入Hadoop的配置文件所在目录
vi hadoop-env.sh
#对配置文件进行修改
```

![image-20230414115423555](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916578.png)

找到配置项 `JAVA_HOME` 所在行，将其改为以下内容:(去掉注释 `#` )

```shell
export JAVA_HOME=/home/admin/java/jdk1.8.0_131
#该路径以JDK软件包实际解压解包的路径为准
```

![image-20230414115520175](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916579.png)
对配置文件进行修改

```shell
vi core-site.xml
```

找到标签`<configuration>`所在的位置，在其中添加如下内容:
注意修改相应的主机名为自己的姓名

```xml
<configuration>
    <property>
        <!--指定Aadoop的访问路径，需要指定为后面的HA集群配置中定义的命名空间的逻辑名称之一-->
        <name>fs.defaultFS</name>
        <value>hdfs://hadoop-ha</value>
    </property>
    <property>
        <name>hadoop.tmp.dir</name>
        <!--指定Hadoop的临时文件的本地存放路径--> 
        <value>/home/admin/hadoop/tmp</value>
    </property>
    <property>
        <name>ha.zookeeper.quorum</name>
        <!--指定Zookeeper的连接地址,多个用“,”分隔-->
        <value>LZY-01:2181,LZY-02:2181,LZY-03:2181,LZY-04:2181,LZY-05:2181</value>
        <!--注意修改成自己的主机名-->
    </property>
</configuration>
```

![image-20230414115657119](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916580.png)

对配置文件进行修改

```shell
vi hdfs-site.xml
```

![image-20230414115750788](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916581.png)

找到标签`<configuration>`所在的位置，在其中添加如下内容:

```xml
<configuration>
    <property>
        <name>dfs.nameservices</name>
        <value>hadoop-ha</value>
    </property>
    <property>
        <name>dfs.ha.namenodes.hadoop-ha</name>
        <value>name-1,name-2</value>
    </property>
    <property>
        <name>dfs.namenode.rpc-address.hadoop-ha.name-1</name>
        <value>LZY-01:9000</value>
        <!-- 注意改名 -->
    </property>
    <property>
        <name>dfs.namenode.http-address.hadoop-ha.name-1</name>
        <value>LZY-01:50070</value>
        <!-- 注意改名 -->
    </property>
    <property>
        <name>dfs.namenode.rpc-address.hadoop-ha.name-2</name>
        <value>LZY-02:9000</value>
        <!-- 注意改名 -->
    </property>
    <property>
        <name>dfs.namenode.http-address.hadoop-ha.name-2</name>
        <value>LZY-02:50070</value>
        <!-- 注意改名 -->
    </property>
    <property>
        <name>dfs.namenode.shared.edits.dir</name>
        <value>qjournal://LZY-03:8485;LZY-04:8485;LZY-05:8485/hadoop-ha</value>
        <!-- 注意改名 -->
    </property>
    <property>
        <name>dfs.journalnode.edits.dir</name>
        <value>/home/admin/hadoop/journal</value>
    </property>
    <property>
        <name>dfs.ha.automatic-failover.enabled</name>
        <value>true</value>
    </property>
    <property>
       <name>dfs.client.failover.proxy.provider.hadoop-ha</name>
        <value>org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider</value>
    </property>

    <property>
        <name>dfs.ha.fencing.methods</name>
        <value>
            sshfence
            shell(/bin/true)
        </value>
    </property>
    <property>
        <name>dfs.ha.fencing.ssh.private-key-files</name>
        <value>/home/admin/.ssh/id_rsa</value>
    </property>
    <property>
        <name>dfs.ha.fencing.ssh.connect-timeout</name>
        <value>30000</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/home/admin/hadoop/name</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/home/admin/hadoop/data</value>
    </property>
    <property>
        <name>dfs.replication</name>
        <value>3</value>
    </property>
</configuration>
```

![image-20230414115904694](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916582.png)

由模板文件拷贝生成配置文件`mapred-site.xml`

```shell
cp mapred-site.xml.template mapred-site.xml
```

![image-20230414120010774](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916583.png)

对配置文件进行修改

```shell
vi mapred-site.xml
```

找到标签`<configuration>`所在的位置，在其中添加如下内容:

```xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
<!--指定MapReduce所使用的外部管理框架，这里使用Hadoop 2.7.3自带的YARN资源管理器-->
```

![image-20230414120619801](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916584.png)

对配置文件进行修改

```shell
vi yarn-env.sh
```

找到配置项`JAVA_HOME`所在行，将其改为以下内容:(注意取消注释`#`，顶格)

```shell
export JAVA_HOME=/home/admin/java/jdk1.8.0_131
#该路径以JDK软件包实际解压解包的路径为准
```

![image-20230414120815045](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916585.png)

对配置文件进行修改

```shell
vi yarn-site.xml
```

找到标签`<configuration>`所在的位置，在其中添加如下内容:

```xml
<configuration>
    <!--Site
specific YARN congfigurationproerties-->
    <property>
        <name>yarn.resourcemanager.ha.enabled</name>
        <value>true</value>
    </property>
    <property>
        <name>yarn.resourcemanager.cluster-id</name>
        <value>yarn-ha</value>
    </property>
    <property>
        <name>yarn.resourcemanager.ha.rm-ids</name>
        <value>resource-1,resource-2</value>
    </property>
    <property>
        <name>yarn.resourcemanager.hostname.resource-1</name>
        <value>LZY-01</value>
        <!-- 注意改名 -->
    </property>
    <property>
        <name>yarn.resourcemanager.hostname.resource-2</name>
        <value>LZY-02</value>
        <!-- 注意改名 -->
    </property>
    <property>
        <name>yarn.resourcemanager.zk-address</name>
        <value>LZY-01:2181,LZY-02:2181,LZY-03:2181,LZY-04:2181,LZY-05:2181</value>
        <!-- 注意改名 -->
    </property>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
</configuration>

```

![image-20230414121117080](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916586.png)



对配置文件进行修改

```shell
vi slaves
```

删除文件中原有的所有内容，然后添加集群中所有数据节点的主机名，每行一个主机的主机名，

配置格式如下:

```shell
LZY-03
LZY-04
LZY-05
```

![image-20230414121220031](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916587.png)

备注:

如果你要把主节点和主节点备用节点同时作为数据节点使用，也是可以的，这里加上01和02即可。后面配置要一致。



## 同步安装和配置

将`hadoop`目录和`.bash_profile`文件发给集群中所有主机，发送目标用户为集群专用用户`admin`，

发送目标路径为`/home/admin`

即集群专用用户`admin`的家目录。

```shell
scp -r ~/hadoop ~/.bash_profile admin@LZY-02:/home/admin

scp -r ~/hadoop ~/.bash_profile admin@LZY-03:/home/admin

scp -r ~/hadoop ~/.bash_profile admin@LZY-04:/home/admin

scp -r ~/hadoop ~/.bash_profile admin@LZY-05:/home/admin
```

![image-20230415005148072](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916588.png)

![image-20230415005535543](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916589.png)

集群中每台主机分别进行以下命令操作:

```shell
source ~/.bash_profile
#使新配置的环境变量立即生效
echo $HADOOP_HOME
#查看新添加和修改的环境变量是否
echo $PATH
#设置成功，以及环境变量的值是否正确。
hadoop version
#验证Hadoop的安装配置是否成功
```

![image-20230415005358886](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916590.png)



## Hadoop高可用完全分布模式格式化和启动

★注意本节格式化内容不可多次执行(★注意格式化步骤)

```shell
hadoop-daemon.sh start journalnode
```

在**所有同步通信节点**的主机执行，启动同步通信服务，然后使用命令`jps`查看`Java`进程信息，若有名为`JournalNode`的进程，则表示同步通信节点启动成功。
注:本操作只在第一次安装时执行。安装完成后，以及关机重启服务器后不需要再次执行。

![image-20230415013344790](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916591.png)

![image-20230415013433751](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916592.png)

![image-20230415013511890](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916593.png)



在**主节点**使用此命令，对HDFS进行格式化，若格式化过程中没有报错则表示格式化成功。

注:本操作只在**第一次安装**时执行。安装完成后，以及关机重启服务器后不需要再次执行。

**千万不要多次格式化**

```shell
hadoop namenode -format
```

![image-20230415013829517](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916594.png)



格式化完成后将`hadoop`目录下的`name`目录发给集群中所有**备用主节点**的主机，

发送目标用户为集群专用用户`admin`，即当前与登录用户同名的用户

发送目标路径为`/home/admin/hadoop`,即集群专用用户`admin`家目录下的`Hadoop`相关文件的目录。

```shell
scp -r ~/hadoop/name admin@LZY-02:/home/admin/hadoop
```

![image-20230415013939962](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916595.png)



在集群中**所有主机**上使用此命令，查看该节点**Zookeeper**服务当前的状态

若集群中只有一个`leader`节点，其余的均为`follower`节点，则集群的工作状态正常。

```shell
zkServer.sh status
```

如果**Zookeeper**未启动，则在集群中所有主机上使用命令`zkServer.sh start`启动Zookeeper服务的脚本。

```shell
zkServer.sh start
```

![image-20230415014214338](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916596.png)



在**主节点**使用命令,对**Hadoop**集群在**Zookeeper**中的主节点切换控制信息进行格式化，

若格式化过程中没有报错则表示格式化成功。

格式化之前确保集群中各主机Zookeeper开启。

注:本操作只在**第一次安装时执行**。安装完成后，以及关机重启服务器后不需要再次执行。不要重复格式化。

```shell
hdfs zkfc -formatZK
```

![image-20230415014340701](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916597.png)



在**所有同步通信节点**的主机，使用此命令，关闭同步通信服务。

注:本操作只在第一次安装时执行。安装完成后，以及关机重启服务器后不需要再次执行。

```shell
hadoop-daemon.sh stop journalnode
```

![image-20230415014500983](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916598.png)

![image-20230415014536047](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916599.png)

![image-20230415014551426](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916600.png)



在**主节点**使用命令,启动Hadoop集群。

```shell
start-all.sh
```

![image-20230415014705139](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916601.png)



在所有**备用主节点**的主机，使用此命令，启动**YARN**主节点服务。

```shell
yarn-daemon.sh start resourcemanager
```

![image-20230415014750066](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916602.png)

启动命令，每次重启后，在zookeeper动成功的前提下，只需执行此两步即可。



在**主节点**使用命令`jps`查看Java进程信息，若有名为`NameNode`、`ResourceManager`、`DFSZKFailoverController`的三个进程，则表示Hadoop集群的**主节点**启动成功。

```shell
jps
```

![image-20230415155410254](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916603.png)



**ResourceManager**未启动时

```shell
cd /home/admin/hadoop/hadoop-2.7.3/logs
```

查看对应的log文件



可以使用命令`hadoop dfsadmin -report`查看**HDFS**状态。

```shell
hadoop dfsadmin -report
```

![image-20230415162949952](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916604.png)

使用命令`ssh 目标主机名或P地址`远程登录到**所有备用主节点**主机，使用命令`jps`查看Java进程信息

若有名为`NameNode`、`ResourceManager`、`DFSZKFailoverController`的三个进程，则表示Hadoop集群的**备用主节点**启动成功。

![image-20230415155707503](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916605.png)



使用命令`ssh 目标主机名或P地址`远程登录到**所有数据节点**主机，使用命令`jps`查看Java进程信息，

若有名为`DataNode` 、`NodeManager`、`JournalNode`的三个进程，则表示**Hadoop**集群的**数据节点**启动成功。

![image-20230415160131888](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916606.png)

![image-20230415160214194](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916607.png)

![image-20230415160237963](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916608.png)



## Hadoop高可用完全分布模式验证

在**Hadoop**中创建当前登录用户自己的目录

```shell
hadoop fs -mkdir -p /user/admin
```

查看HDFS中的所有文件和目录的结构

```shell
hadoop fs -ls -R /
```

![image-20230415163041295](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916609.png)



```shell
cd ~/hadoop/hadoop-2.7.3/share/hadoop/mapreduce
#进入Hadoop的示例程序包hadoop-mapreduce-examples-2.7.3.jar所在目录
hadoop jar hadoop-mapreduce-examples-2.7.3.jar pi 2 1000
#运行使用蒙地卡罗法计算PI的示例程序
```

![image-20230415163309918](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916611.png)

![image-20230415163327528](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311916612.png)



# HDFS



## 熟悉常用的HDFS操作

![image-20230421112804665](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915286.png)



(1）向HDFS中上传任意文本文件，如果指定的文件在HDFS中已经存在，由用户指定是追加到原有文件末尾还是覆盖原有的文件;（追加文件内容以编程方式进行)
例如:新建文本文件`file1.txt`;第二次重复上传本文件

```shell
hadoop fs -ls /
hadoop fs -touchz file1.txt
```

![image-20230421114122921](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915288.png)

```shell
hadoop fs -appendToFile /home/admin/file1.txt /user/admin/file1.txt
```



(2）从HDFS中下载指定文件，如果本地文件与要下载的文件名称相同，则自动对下载的文件重命名;
例如:从HDFS下载`file1.txt`到本地目录;和本地重名自动重命名

```shell
hadoop fs -get /user/admin/file1.txt /home/admin/
```

![image-20230421114210236](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915289.png)

(3）将HDFS中指定文件的内容输出到终端中;
例如:查看打印HDFS中指定文件`file1.txt`的内容

```shell
hadoop fs -cat /user/admin/file1.txt
hadoop fs -text /user/admin/file1.txt
```

![image-20230421114903407](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915290.png)

(4）显示HDFS中指定的文件的读写权限、大小、创建时间、路径等信息;

例如:查看HDFS中`file1.txt`的读写权限、文件大小、创建时间、路径等。

```shell
hadoop fs -du /user/admin/file1.txt
hadoop fs -du -s /user/admin/file1.txt
hadoop fs -du -h /user/admin/file1.txt
```

![image-20230421115309498](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915291.png)

(5）给定HDFS中某一个目录，输出该目录下的所有文件的读写权限、大小、创建时间、路径等信息，如果该文件是目录，则递归输出该目录下所有文件相关信息;
例如:

新建目录`dir1/dir1/dir2`

新建并上传文件`file2.txt`到`dir1`，`file2.txt`内容为`hello world!` ，

新建并上传文件`file3.txt`到`dir2`，`file3.txt`的内容为`hello hadoop ! `,

然后查看`dir1`目录下的所有文件读写权限,大小等;

递归输出`dir2`目录下所有文件相关信息。

```shell
hadoop fs -mkdir dir1
hadoop fs -mkdir -p dir1
hadoop fs -mkdir -p /user/admin/dir1/dir2
echo 'hello world!'>/home/admin/file2.txt
hadoop fs -put /home/admin/file2.txt /user/admin/dir1/
hadoop fs -cat /user/admin/dir1/file2.txt
hadoop fs -du -h /user/admin/dir1/
echo 'hello hadoop!'>/home/admin/file3.txt
hadoop fs -put /home/admin/file3.txt /user/admin/dir1/dir2/
hadoop fs -ls /user/admin/dir1
hadoop fs -ls -R /user/admin/dir1
```

![image-20230421115748152](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915292.png)

(6）提供一个HDFS内的文件的路径，对该文件进行创建和删除操作。如果文件所在目录不存在，则自动创建目录;
例如:HDFS内的文件`file4.txt`，指定路径为`/dir1/dir3`

```shell
hadoop fs -mkdir /user/admin/dir1/dir3
hadoop fs -touchz /user/admin/dir1/dir3/file4.txt
```

![image-20230421143258494](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915293.png)

(7)提供一个HDFS的目录的路径，对该目录进行创建和删除操作。创建目录时，如果目录文件所在目录不存在则自动创建相应目录;删除目录时，由用户指定当该目录不为空时是否还删除该目录;
例如:HDFS内的目录`dir4`，指定路径为`/dir1/`，在HDFS中`/dir1/dir4`目录下新建文件`file5.txt`

```shell
hadoop fs -mkdir -p /user/admin/dir1/dir4
hadoop fs -touchz /user/admin/dir1/dir4/file5.txt
hadoop fs -rm /user/admin/dir1/dir4
hadoop fs -rm -R /user/admin/dir1/dir4
```

![image-20230421143509597](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915294.png)

(8）向HDFS中指定的文件追加内容，由用户指定内容追加到原有文件的开头或结尾;
例如:向`file5.txt`文件内追加内容`Hello Hadoop!`

```shell
echo 'Hello Hadoop!'>/home/admin/file5.txt
hadoop fs -appendToFile /home/admin/file5.txt /user/admin/dir1/dir4/file5.txt
hadoop fs -cat /user/admin/dir1/dir4/file5.txt
```

![image-20230421144727639](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915295.png)



## MapReduce -WordCount程序练习

### 上传jar包

#### 准备工作

以`admin`普通用户登录主节点操作

**创建本地示例文件**
首先在`/home/admin`目录下创建文件夹`file`

```shell
cd /home/admin/
ls
mkdir ~/file
ls
```

![image-20230421144910202](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915296.png)

接着创建两个文本文件`file1.txt`和`file2.txt`。
使`file1.txt`内容为`Hello World`，而`file2.txt`的内容为`Hello Hadoop`。

```shell
cd file
echo "Hello World"> file1.txt
echo "Hello Hadoop"> file2.txt
ls
cat file1.txt
cat file2.txt
```

![image-20230421145047880](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915297.png)

**在HDFS上创建输入文件夹**

```shell
hadoop fs -mkdir input
```

![image-20230421145133641](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915298.png)

**上传本地file 中文件到集群的input目录下**

```shell
hadoop fs -put ~/file/file*.txt input
hadoop fs -ls input
```

![image-20230421145238881](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915299.png)

#### 上传jar包

先使用**Xftp**工具把**WordCount**的**jar**执行程序包，上传到`~/hadoop/hadoop-2.7.3/share/hadoop/mapreduce`

![image-20230421150523882](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915300.png)

### 示例运行

**在集群上运行WordCount程序**
备注:以input作为输入目录，output目录作为输出目录。

执行命令:

```shell
hadoop jar ~/hadoop/hadoop-2.7.3/share/hadoop/mapreduce/hadoop-0.20.2-examples.jar wordcount input output
```

**MapReduce执行过程显示信息**

![image-20230421145834981](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915301.png)

![image-20230421145847435](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915302.png)



**查看结果**

1. 查看HDFS 上output目录内容

   ```shell 
   hadoop fs -ls output
   ```

![image-20230421150103798](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915303.png)

2. 查看结果输出文件内容

   ```shell
   hadoop fs -cat output/part-r-00000
   ```

![image-20230421150224611](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915304.png)

**完成测试数据统计**
参照前面运行示例，请将测试数据上传至hadoop集群，并启动
**Mapreduce**运行**wordcount**，将统计结果输出至hdfs上以**个人姓名命名**的文件夹中。

备注:以`lzy_in`作为输入目录，`lzy_out`目录作为输出目录。

```shell
hadoop fs -mkdir lzy_in
hadoop fs -put ~/file/wordceshi*.txt lzy_in
hadoop fs -ls lzy_in
hadoop jar ~/hadoop/hadoop-2.7.3/share/hadoop/mapreduce/hadoop-0.20.2-examples.jar wordcount lzy_in lzy_out
```

![image-20230421151405518](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915305.png)

```shell
hadoop fs -ls lzy_out
hadoop fs -cat lzy_out/part-r-00000
```

![image-20230421151430199](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915306.png)

![image-20230421151439161](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915307.png)

![image-20230421151451698](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915308.png)

![image-20230421151510994](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915309.png)

## Hadoop的Web验证练习

**HDFS启动验证、状态验证:**

1. 查看jps进程

![image-20230421151712339](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915310.png)

2. 打开浏览器查看整个集群的HDFS状态:
   http://192.168.10.111:50070/

   http://192.168.10.111:50070/dfshealth.html#tab-overview

   ![image-20230421152015327](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915311.png)

   http://192.168.10.112:50070/

   ![image-20230421152340395](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915312.png)

**ResourceManager状态查看:**

1. 打开浏览器查看集群状态、日志信息等:
   http://192.168.10.111:8088/
   http://192.168.10.111:8088/cluster

   ![image-20230421152444665](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915313.png)



**在从节点上查看NodeManager信息:**

http://192.168.10.113:8042/

![image-20230421152604946](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311915314.png)

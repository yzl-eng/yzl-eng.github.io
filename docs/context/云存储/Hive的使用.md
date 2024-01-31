## 启动

```shell
#在集群中所有主机上使用命令“zkServer.sh
zkServer.sh status
#status查看该节点Zookeeper服务当前的状态，若集群中只有一个“leade节点，其余的均为“followe节点，则集群的工作状态正常。
zkServer.sh start
#如果Zookeeper未启动，则在集群中所有主机上使用命令“zkServer.sh start启动Zookeeper服务的脚本

start-all.sh
#主节点
yarn-daemon.sh start resourcemanager
#备用主节点
jps
#在主节点,查看Java进程信息，若有名为“NameNode、“ResourceManager的两个进程，则表示Hadoop集群的主节点启动成功。在每台数据节点，若有名为“DataNode和“NodeManagér的两个进程，则表示Hadoop集群的数据节点启动成功
start-hbase.sh
#确定Hadoop集群己启动状态，然后在主节点使用此命令,启动HBase集群。
jps
#在集群中所有主机上使用命令“jps”
```

root用户下

1. 先启动管理节点

2. 再启动两个数据服务节点

3. 最后启动SQL节点

   ```shell
   ndb_mgmd -f /usr/local/mysql/etc/config.ini
   ndbd
   service mysql start
   ```

   

## 数据仓库Hive的使用

分桶表属于内部表，关键字**clustered**

```sql
set hive.exec.mode.local.auto=true;
set hive.enforce.bucketing=true;
```

修改参数允许强制分桶，也可以修改`hive_site.xml`文件中的参数改为`true`

```xml
<property>
    <name>hive.enforce.bucketing</name>
    <value>false</value>
    <description>Whether bucketing is enforced. If true, whileinsertinginto the table, bucketing is enforced.</description>
</property>
```

![image-20230621170747158](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920500.png)



### 启动Hive 常用命令

```sql
hive
#启动Hive，启动成功后能够进入Hive的控制台。
show databases;
#查看当前的数据库列表。
create database test1;#创建数据库
show databases;
use test1;
#使用数据库
create table testtable(id int,name string,age int,tel string) row format delimited fields terminated by ',' stored as textfile;
#创建表
show tables;
drop table testtable;
#删除表
drop database test1;
#删除数据库

```

![image-20230621171010064](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920501.png)

### Hive的数据模型_内部表

练习:

```sql
hive
#启动Hive，启动成功后能够进入Hive的控制台。
create database test2;
#创建数据库
use test2;
#使用数据库
create database test3;
#创建数据库
use test3;
#使用数据库

create table t1(tid int, tname string, age int);
create table t2(tid int, tname string, age int) location '/mytable/hive/t2';
create table t3(tid int, tname string, age int) row format delimited fields terminated by ',';
create table t4 as select * from t1;
```

![image-20230621171223178](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920502.png)

```shell
hadoop fs -ls /user/hive/warehouse/
hadoop fs -ls /user/hive/warehouse/test2.db
hadoop fs -ls /user/hive/warehouse/test2.db/t1
hadoop fs -ls /mytable/hive/
```

![image-20230621171439407](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920503.png)

```shell
hive
use test3
desc t1;
alter table t1 add columns(english int);
desc t1;
drop table t1;
```

![image-20230621171641554](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920504.png)

```shell
hdfs dfs -ls /user/hive/warehouse/test2.db
```



### Hive的数据模型_分区表

```shell
hive
create database test4;
use test4;
```

准备数据表:

```shell
create table sampledata (sid int, sname string, gender string, language int,math int, english int) row format delimited fields terminated by ',' stored as textfile;
```

![image-20230621171842819](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920505.png)

准备文本数据:

在admin用户家目录下新建sampledata.txt内容:

![image-20230621145339382](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920506.png)

将文本数据插入到数据表:

```shell
load data local inpath '/home/admin/sampledata.txt' into table sampledata;
select * from sampledata;
```

![image-20230621172010431](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920507.png)

创建分区表：

```shell
create table partition_table(sid int, sname string) partitioned by (gender string) row format delimited fields terminated by ',';
select * from partition_table;
```

![image-20230621172045345](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920508.png)

向分区表中插入数据：

```shell
insert into table partition_table partition(gender='M') select sid, sname from sampledata where gender='M';
insert into table partition_table partition(gender='F') select sid, sname from sampledata where gender='F';
select * from partition_table;
show partitions partition_table;
```

![image-20230621172321387](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920509.png)

登录http://192.168.10.111:8088/cluster/apps可以查看job执行状态

![image-20230621172242659](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920510.png)

![image-20230621172347019](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920511.png)

### Hive的数据模型_外部表

#### 准备数据：

在admin家目录下分别新建

student1.txt内容：

```shell
1,Tom,M,60,80,96
2,Mary,F,11,22,33
```

student2.txt

```shell
3,Jerry,M,90,11,23
```

student3.txt内容：

```shell
4,Rose,M,78,77,76
5,Mike,F,99,98,98
```

![image-20230621172606186](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920512.png)

```shell
hdfs dfs -ls /
hdfs dfs -mkdir /input
```

将文件放入HDFS文件系统语法：

hdfs dfs -put localFileName hdfsFileDir

```shell
hdfs dfs -put student1.txt /input
hdfs dfs -put student2.txt /input
hdfs dfs -put student3.txt /input
```

![image-20230621172655849](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920513.png)

```shell
hive
create database test5;
use test5;
```

#### 创建外部表

```shell
create table external_student (sid int, sname string, gender string, language int, math int, english int) row format delimited fields terminated by ',' location '/input';
```

#### 查询外部表

```shell
select * from external_student;
```

![image-20230621172838393](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920514.png)

删除HDFS上的student1.txt

```shell
exit;
hdfs dfs -rm /input/student1.txt
```

![image-20230621172936721](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920515.png)

查询外部表

```shell
hive
use test5;
select * from external_student;
```

![image-20230621173038866](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920516.png)

将student1.txt 重新放入HDFS input目录下

```shell
exit;
hdfs dfs -put student1.txt /input
```

查询外部表

```shell
hive
use test5;
select * from external_student;
```

![image-20230621173149489](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920517.png)

### Hive的数据模型_桶表

对数据进行HASH运算，放在不同文件中，降低热块，提高查询速度。例如：根据sname进行hash运算存入5个桶中。

```shell
hive
create database test6;
use test6;
create table users (sid int, sname string, age int) row format delimited fields terminated by ',';
```

准备文本数据：

在admin用户家目录下新建users.txt内容：

```shell
1,Bear,18
2,Cherry,23
3,Lucky,33
4,Dino,26
5,Janel,28
```



```shell
#将文本数据插入到非桶数据表
load data local inpath '/home/admin/users.txt' into table users;
select * from users;
create table bucket_table(sid int, sname string, age int) clustered by (sname) into 5 buckets row format delimited fields terminated by ',';
select * from bucket_table;
insert overwrite table bucket_table SELECT * FROM users;
```

![image-20230621173625450](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920518.png)

```shell
exit;
hadoop fs -ls /user/hive/warehouse/test6.db/bucket_table/ 
```

![image-20230621173823156](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920519.png)

![image-20230621173854437](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920520.png)

### Hive的数据模型_视图

```shell
hive
create database test7;
use test7;
```

创建一个测试表：

```shell
create table test01 (id int, name string) row format delimited fields terminated by ',';
desc test01;
```

![image-20230621173947595](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920521.png)

```shell
exit;
vi data1.txt
1,tom
2,jack
```

![image-20230621174034994](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920522.png)

```shell
hive
use test7;
load data local inpath '/home/admin/data1.txt' overwrite into table test01;
select * from test01;
```

![image-20230621174248963](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920523.png)

创建一个View之前，使用explain命令查看创建View的命令是如何被Hive解释执行的：

```shell
explain create view test_view (id, name_length) as  select id, length(name) from test01;
```

![image-20230621174309138](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920524.png)

实际创建一个View：

```shell
create view test_view (id, name_length) as  select id, length(name) from test01;
```

执行View之前，先explain查看实际被翻译后的执行过程：

```shell
explain select sum(name_length) from test_view;
explain extended select sum(name_length) from test_view;
```

![image-20230621174336537](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920525.png)

![image-20230621174356059](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920526.png)

最后，对View执行一次查询，显示Stage-1阶段对原始表test进行了MapReduce过程：

```shell
select sum(name_length) from test_view;
```

![image-20230621174552431](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311920527.png)

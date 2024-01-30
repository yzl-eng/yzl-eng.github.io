```shell
zkServer.sh start
#如果Zookeeper未启动，则在集群中所有主机上使用命令“zkServer.sh start启动Zookeeper服务的脚本

start-all.sh
#主节点
yarn-daemon.sh start resourcemanager
#备用主节点
jps
#在主节点,查看Java进程信息，若有名为“NameNode、“ResourceManager的两个进程，则表示Hadoop集群的主节点启动成功。在每台数据节点，若有名为“DataNode和“NodeManagér的两个进程，则表示Hadoop集群的数据节点启动成功
```



## 启动集群



项目中修改`hdfs-site.xml`，`core-site.xml`文件

![image-20231117101711348](Hbase.assets/image-20231117101711348.png)

![image-20231117101918556](Hbase.assets/image-20231117101918556.png)



```shell
hadoop fs -ls webhdfs://192.168.10.112:50070/user
```

错误提示

![image-20231117104035323](Hbase.assets/image-20231117104035323.png)

在Hadoop集群的`namenode`运行`httpfs.sh start`

![image-20231117102230691](Hbase.assets/image-20231117102230691.png)



```shell
 hadoop fs -ls webhdfs://192.168.10.112:50070/user
```

![image-20231117103657604](Hbase.assets/image-20231117103657604.png)



```shell
http://192.168.10.111:50070/webhdfs/v1/user?op=LISTSTATUS
```

![image-20231117104148086](Hbase.assets/image-20231117104148086.png)



检查`yarn-site.xml`

![image-20231117104501041](Hbase.assets/image-20231117104501041.png)



`ResourceManager`高可用机制转换

```shell
yarn rmadmin -getServiceState resource-1
yarn rmadmin -getServiceState resource-2
```

![image-20231117104725832](Hbase.assets/image-20231117104725832.png)



`ResourceManager`机制切换

![image-20231117105156198](Hbase.assets/image-20231117105156198.png)



```shell
start-hbase.sh
#在主节点使用此命令,启动HBase集群
jps
```

![image-20231117100852642](Hbase.assets/image-20231117100852642.png)

![image-20231117100915341](Hbase.assets/image-20231117100915341.png)



## HBASE SHELL常用命令

```shell
hbase shell
create 'tempTable','fl','f2' ,'f3'
list
put 'tempTable','r1','f1:c1','hello,dblab'
get 'tempTable','r1',{COLUMN=>'f1:c1'}
get 'tempTable','r1',{COLUMN=>'f1:c3'}
disable 'tempTable'
drop 'tempTable'
list
```

![image-20231117110506104](Hbase.assets/image-20231117110506104.png)



![image-20231117110941348](Hbase.assets/image-20231117110941348.png)



添加host文件

![image-20231117112413598](Hbase.assets/image-20231117112413598.png)

添加`hbase-site.xml`

![image-20231117112448665](Hbase.assets/image-20231117112448665.png)



## HBASE测试连接

![image-20231117113908391](Hbase.assets/image-20231117113908391.png)



### 创建scores1

![image-20231117114629022](Hbase.assets/image-20231117114629022.png)

![image-20231117114641479](Hbase.assets/image-20231117114641479.png)

![image-20231117114654407](Hbase.assets/image-20231117114654407.png)

![image-20231117114824288](Hbase.assets/image-20231117114824288.png)

![image-20231117114842120](Hbase.assets/image-20231117114842120.png)

## PUT类方法

![image-20231117115111960](Hbase.assets/image-20231117115111960.png)





## GET类方法

![image-20231117120315440](Hbase.assets/image-20231117120315440.png)

## SCAN

![image-20231117120222900](Hbase.assets/image-20231117120222900.png)
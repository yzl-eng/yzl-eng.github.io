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

![image-20231117101711348](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925932.png)

![image-20231117101918556](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925933.png)



```shell
hadoop fs -ls webhdfs://192.168.10.112:50070/user
```

错误提示

![image-20231117104035323](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925934.png)

在Hadoop集群的`namenode`运行`httpfs.sh start`

![image-20231117102230691](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925935.png)



```shell
 hadoop fs -ls webhdfs://192.168.10.112:50070/user
```

![image-20231117103657604](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925936.png)



```shell
http://192.168.10.111:50070/webhdfs/v1/user?op=LISTSTATUS
```

![image-20231117104148086](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925937.png)



检查`yarn-site.xml`

![image-20231117104501041](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925938.png)



`ResourceManager`高可用机制转换

```shell
yarn rmadmin -getServiceState resource-1
yarn rmadmin -getServiceState resource-2
```

![image-20231117104725832](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925939.png)



`ResourceManager`机制切换

![image-20231117105156198](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925940.png)



```shell
start-hbase.sh
#在主节点使用此命令,启动HBase集群
jps
```

![image-20231117100852642](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925941.png)

![image-20231117100915341](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925942.png)



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

![image-20231117110506104](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925943.png)



![image-20231117110941348](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925944.png)



添加host文件

![image-20231117112413598](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925945.png)

添加`hbase-site.xml`

![image-20231117112448665](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925946.png)



## HBASE测试连接

![image-20231117113908391](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925947.png)



### 创建scores1

![image-20231117114629022](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925948.png)

![image-20231117114641479](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925949.png)

![image-20231117114654407](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925950.png)

![image-20231117114824288](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925951.png)

![image-20231117114842120](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925952.png)

## PUT类方法

![image-20231117115111960](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925953.png)





## GET类方法

![image-20231117120315440](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925954.png)

## SCAN

![image-20231117120222900](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311925955.png)
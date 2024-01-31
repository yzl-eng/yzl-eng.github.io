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



## WordCount应用

创建好项目引入依赖

![image-20231011150052651](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926320.png)

导入hadoop配置文件

![image-20231011150106958](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926321.png)

相关代码

![image-20231013105327292](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926322.png)

运行结果

![image-20231013105310105](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926323.png)

![image-20231013105428925](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926324.png)

![image-20231013105542249](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926325.png)



## Partitoner

1.编写map函数的方法

![image-20231019234537555](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926326.png)

2.编写reduce函数的方法

![image-20231019234613830](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926327.png)

3.编写MyPartitioner方法

![image-20231019234709091](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926328.png)

4.main函数的调用创建Job类

![image-20231019234740695](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926329.png)

上传测试文件

![image-20231020105337901](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926330.png)

![image-20231020110755762](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926331.png)

运行上传jar包

```shell
hadoop jar /home/admin/hadoop/hadoop-2.7.3/share/hadoop/mapreduce/MapReduce-1.0-SNAPSHOT.jar com.soft.mapreduce.partitioner.PartitionerApp
```

![image-20231020111746475](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926332.png)

运行结果

```shell
hadoop fs -ls /LZYoutputpartitioner
```

![image-20231020111842183](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926333.png)

```shell
hadoop fs -text /LZYoutputpartitioner/part-r-00000
```

![image-20231020111934261](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926334.png)

```shell
hadoop fs -text /LZYoutputpartitioner/part-r-00001
```

![image-20231020112156634](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926335.png)





## Recordreader

相关代码

![image-20231023143417052](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926336.png)

![image-20231023143452369](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926337.png)

![image-20231023143504241](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926338.png)

上传测试文件

```shell
hadoop fs -mkdir /recordreader 
hadoop fs -put /home/admin/file/recordreader.txt /recordreader
hadoop fs -ls /recordreader 
```

![image-20231020112658254](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926339.png)



运行结果

```shell
hadoop jar /home/admin/hadoop/hadoop-2.7.3/share/hadoop/mapreduce/MapReduce-1.0-SNAPSHOT.jar com.soft.mapreduce.recordreader.RecordReaderApp 
```

![image-20231020112953027](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926340.png)

```shell
hadoop fs -ls /LZYoutputrecordreader
```

![image-20231020113043617](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926341.png)

```shell
hadoop fs -text /LZYoutputrecordreader/part-r-00000
hadoop fs -text /LZYoutputrecordreader/part-r-00001
```

![image-20231020113132774](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926342.png)



## ReduceJoin

相关代码

![image-20231023143542159](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926343.png)

![image-20231023143557435](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926344.png)

![image-20231023143617798](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926345.png)

上传测试文件

```shell
hadoop fs -mkdir /inputjoin
hadoop fs -put /home/admin/file/emp.txt /home/admin/file/dept.txt /inputjoin 
hadoop fs -ls /inputjoin
```

![image-20231020113702363](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926346.png)

运行jar包代码

```shell
hadoop jar /home/admin/hadoop/hadoop-2.7.3/share/hadoop/mapreduce/MapReduce-1.0-SNAPSHOT.jar com.soft.mapreduce.reducejoin.EmpJoinApp
```

![image-20231020125615066](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926347.png)

```shell
hadoop fs -text /LZYoutputmapjoin/part* 
```





## sort

![image-20231023143650731](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926348.png)

![image-20231023143705370](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926349.png)

![image-20231023143723872](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926350.png)

上传测试文件

```shell
hadoop fs -mkdir /sort 
hadoop fs -put /home/admin/file/sort.txt /sort
hadoop fs -ls /sort
```

![image-20231020115432689](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926351.png)

```shell
hadoop jar /home/admin/hadoop/hadoop-2.7.3/share/hadoop/mapreduce/MapReduce-1.0-SNAPSHOT.jar com.soft.mapreduce.sort.SortApp 
```

运行结果

![image-20231020115523214](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926352.png)

```shell
hadoop fs -text /LZYoutputsort/part* 
```

![image-20231020115606421](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926354.png)



## 二次排序

相关代码

![image-20231023143806743](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926355.png)

上传测试文件

```shell
hadoop fs -mkdir /secondsort 
hadoop fs -put /home/admin/file/secondsort.txt /secondsort 
hadoop fs -ls /secondsort
```

![image-20231020115806002](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926356.png)

```shell
hadoop jar /home/admin/hadoop/hadoop-2.7.3/share/hadoop/mapreduce/MapReduce-1.0-SNAPSHOT.jar com.soft.mapreduce.secondsort.SecondarySortApp  
```

运行结果

![image-20231020120420278](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926357.png)

```shell
hadoop fs -text /LZYoutputsecondsort/part*
```

![image-20231020120518253](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926358.png)



## 合并小文件

相关代码

![image-20231023143833199](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926359.png)

上传测试文件

```shell
hadoop fs -mkdir /inputmerge 
hadoop fs -put /home/admin/file/secondsort.txt /inputmerge 
hadoop fs -ls /secondsort
```

![image-20231020121525101](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926360.png)

运行jar包代码

```shell
hadoop jar /home/admin/hadoop/hadoop-2.7.3/share/hadoop/mapreduce/MapReduce-1.0-SNAPSHOT.jar com.soft.mapreduce.MergeApp  
```

运行结果

![image-20231020121843738](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926361.png)

```shell
hadoop fs -ls /LZYoutputmerge
```

![image-20231020121902489](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311926362.png)



```shell
hadoop fs -rm -r -skipTrash
```


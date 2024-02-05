

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
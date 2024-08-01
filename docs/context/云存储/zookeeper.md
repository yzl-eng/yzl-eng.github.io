# ZooKeeper介绍

## 背景	

Zookeeper是一个开源的分布式协调服务框架，最初由Yahoo!开发，目前由Apache基金会维护。Zookeeper主要提供的功能包括分布式锁、协调、命名等服务，为分布式应用程序提供了强大的支持。

Zookeeper的研究背景主要是随着互联网的快速发展和云计算、物联网等新兴技术的兴起，应用程序的规模和复杂性不断增强，需要依赖分布式系统进行支持。然而，分布式系统的设计和实现本身面临着许多挑战和问题，例如节点失效、网络延迟、系统复杂度等等。Zookeeper的研究和设计便是为了解决这些挑战和问题。

Zookeeper在实际应用中具有重要的意义。首先，Zookeeper提供了一组完整而强大的API，为应用开发人员提供了分布式应用程序的构建块。其次，Zookeeper可以帮助应用程序来协调和管理各个节点，确保分布式应用程序的高可用性、一致性和可靠性。最后，Zookeeper的设计和原理也为分布式系统的设计提供了很多借鉴和参考。

总的来说，随着分布式系统的不断发展和应用需求的不断增强，Zookeeper作为一种可靠和高效的分布式协调服务框架，将持续发挥着重要的作用。

## 发展历程和现状	

Zookeeper是一个分布式协调服务框架，最初由Yahoo!公司于2006年发起，于2010年成为Apache顶级项目，目前得到了广泛的应用和支持，成为分布式应用程序开发和管理的基础组件之一。以下是Zookeeper的发展历程和现状：

1. 2006年，Yahoo!公司开发了Zookeeper，作为他们的分布式应用程序的协调服务框架。
2. 2008年，Zookeeper开始在Apache中开发，并于同年正式成为Apache的子项目，并获得了良好的反响和用户反馈。
3. 2010年，Zookeeper成为Apache的顶级项目，这意味着它已经得到了Apache基金会的认可，并将为今后的发展提供更好的支持。
4. 随着时间的推移，Zookeeper逐渐得到了广泛的应用和推广。越来越多的分布式应用程序依赖Zookeeper来实现集群管理、分布式锁等功能。
5. 目前，Zookeeper已经成为分布式系统的常用组件之一，被广泛应用于OpenStack、Hadoop、Kafka、Storm等分布式大数据领域、云计算领域、物联网等各个领域。
6. 目前，Zookeeper的开发社区非常活跃，定期发布新版本，不断更新和完善功能，在应对新的挑战和需求方面取得了很多进展。

总的来说，Zookeeper在分布式协调和管理方面有着广泛的应用和良好的口碑，并且它的发展历史和现状都非常稳定和可持续。Zookeeper的未来仍然充满潜力和挑战，我们相信它将持续为分布式应用程序的开发和管理提供必要的支持和保障。



# Zookeeper应用	

## Zookeeper的概述和原理

ZooKeeper是一个分布式协调服务，主要用于协调和管理分布式系统中的配置信息、命名服务、分布式锁等。ZooKeeper采用分层架构，并提供高可用性、高性能、严格顺序访问和细粒度访问控制等特性。

**原理**：

好的，以下是更为详细的解释：

1. 分布式数据结构
   Zookeeper的数据存储是基于ZooKeeper Tree这个分布式数据结构的。ZooKeeper Tree是一棵树状结构，每个节点都可以存储数据及其相关的元数据。每个节点都有一个路径名，类似于Unix文件系统中的路径名，便于定位和访问。每个路径对应的节点可以保存一个字节数组，即节点的值，同时还可以存储版本信息和节点状态等元数据。在ZooKeeper Tree上，路径名必须是唯一的，例如，节点A的路径名“/a”，节点B的路径名“/b”。

2. 分布式协议
   Zookeeper采用了一种名为Zab（Zookeeper Atomic Broadcast）的分布式协议，用于确保数据的一致性。Zab协议是一种基于复制日志的共识算法，用于实现高可用性和容错性。Zab协议将分布式事务的处理过程分为两个阶段：广播和提交。

   -  广播阶段：在广播阶段，每个服务器都将客户端请求和Zookeeper自身产生的请求广播到其他服务器上，并等待大多数服务器响应结束。在广播阶段，Zookeeper使用了基于Paxos算法的一个变种，即使在一些服务器出现故障的情况下也能够保证一致性。

   -  提交阶段：在广播阶段完成后，服务器会开始提交阶段。在提交阶段，Zookeeper会将广播阶段收到的请求转换成一个全局唯一且不可变的序列。每个事务被分配一个全局唯一的64位数字，称为“zxid”。

3. 高可用性和故障恢复
   在分布式系统中，节点故障成为了一个很大的问题。为了解决这个问题，Zookeeper设计了一套复杂的机制来保障高可用性和故障恢复能力。

   - 主从复制机制：Zookeeper使用主从复制机制来实现冗余和故障恢复。在Zookeeper中，主节点负责处理客户端请求，并将客户端提交的事务广播给所有的从节点。所有的从节点都将复制主节点的数据，保持与主节点的数据同步。当主节点发生故障时，从节点会被动切换至仍存活的主节点。

   - 选举机制：在Zookeeper首页中，每个服务器都会参与到一个严格的选举过程中。选举过程通常基于服务器间产生的“通讯”，因此Zookeeper通过实现一个简单的协议来确保每个服务器的选举顺序。

   - 观察器（Watcher）机制：Zookeeper提供了一种名为观察器（Watcher）的机制，可以观察节点状态的变化。当发生节点状态变化时，Zookeeper将通知节点的watcher客户端，以便客户端可以采取相应的操作。观察器机制有助于实现分布式锁和协作等功能。

4. 分布式锁机制
   Zookeeper提供了一套完整的分布式锁机制，能够在不同节点上实现分布式锁，以协调多个节点的同时访问。Zookeeper提供了两种锁的实现方式：短暂（Ephemeral）锁和顺序（Sequential）锁。此外，Zookeeper还提供了两种加锁/解锁方式：同步和异步。

   - 短暂锁：短暂锁是基于Zookeeper节点的生命周期实现的，当锁持有者节点失效的时候，短暂锁会自动被删除，从而释放锁。这种锁在会话结束时自动释放，在锁的访问者出现故障或网络中断时也会被删除。

   - 顺序锁：顺序锁指每次获取锁时，Zookeeper都会为新的锁节点创建一个序号，以帮助客户端识别新加入的访问者节点的顺序。这种方式可以避免一定程度上的死锁和活锁。

   - 同步加锁/解锁：同步方式是指在锁定/解锁操作完成之前，调用者都将被阻塞。同步方式适用于获取锁的请求非常频繁的情况。

   - 异步加锁/解锁：异步方式则是指调用者在发送请求后继续执行程序。当Zookeeper锁操作完成时，Zookeeper将通过回调函数来通知调用者。异步方式适用于请求量比较大的情况，可以提高系统的并发性能。

​	

## Zookeeper在分布式应用中的特点和作用	

1. 分布式协调

   Zookeeper可以用来协调在多个节点之间共享的信息，比如实现分布式应用中的一致性信息、数据同步、元数据管理、分布式锁等功能。

2. 高可用性

   Zookeeper本身就是一个高可用的分布式系统，具有自动故障切换和数据备份等特性。在Zookeeper集群中，每个节点都可以同步其他节点的状态信息，因此如果某个节点出现问题，其他节点可以很快地接管任务。

3. 数据一致性

   Zookeeper通过处理数据一致性问题，确保在分布式应用中的数据的正确性，从而保证了整个应用的稳定性。当一个znode被更新时，Zookeeper将确保所有的客户端能够及时获知这一更新，并保证节点上的数据是一致的。

4. 可扩展性

   Zookeeper是一个高度可扩展的分布式系统，可以根据需要配置集群规模和节点数目。由于节点之间的通信使用的是TCP协议，因此可以保证通信的可靠性和数据传输的保密性。

5. 高性能

   Zookeeper的核心算法和协议都是基于Paxos算法和ZAB（Zookeeper Atomic Broadcast）协议，因此它具有高度的性能和性能可扩展性。例如，斯克龙根据Zookeeper提供的CAS（Compare-And-Swap）特性，实现了高性能的分布式计数器，用于记录各种计数器信息。

## Hadoop集群中的Zookeeper应用


 在Hadoop集群中，Zookeeper主要用于以下三个方面：

1. Namenode和ResourceManager的高可用性
   Hadoop的Namenode和ResourceManager是集群中的重要组件，如果其中一个节点出现故障，则整个集群都会出现问题。为了解决这个问题，Hadoop引入了Zookeeper，使用Zookeeper来选择新的Namenode和ResourceManager，以实现对集群的高可用性保障。
2. 分布式锁与协调
   在Hadoop集群中，Zookeeper也用于实现分布式锁、协调和同步等任务，例如，多个task节点需要读取同一个文件，需要使用一个锁来防止并发读取，同时保证数据的一致性性。
3. HBase的分布式协调
   HBase是另一个流行的Hadoop项目。它是一个分布式的、面向列的数据库。HBase也使用Zookeeper来管理集群状态和协调一些节点之间的操作。例如，HBase使用Zookeeper控制RegionServer的failover、Balancer管理和Zookeeper Watcher这些功能。



# 总结和展望	

## zookeeper技术和生态系统的特点和优势

Zookeeper是一个开源的分布式协调服务框架，具有以下技术和生态系统的特点和优势：

1. 高可用性和可靠性
   Zookeeper通过设计多个节点来提高可用性和可靠性，其中客户端可以连接到任何一个可用的Zookeeper节点，这些节点之间会同步数据，当一个节点失效时，其他节点会自动接管任务，以确保服务的持续可用性和可靠性。
2. 一致性和强一致性保证
   为了保证高一致性的服务，Zookeeper采用具有强一致性保障的ZAB协议，这个协议是一个由Zookeeper自己定义的协议，实现了整个系统的一致。Zookeeper还使用版本号来保障数据一致性。
3. 低延迟查询和高并发读写
   Zookeeper通过内存映射技术来实现快速的内存访问和高效的数据交换。同时，Zookeeper使用非阻塞式的读写操作和异步的事件操作，实现了低延迟查询和高并发读写。
4. 多语言支持和易用性
   Zookeeper提供了多种编程语言的API，如Java、C、C++、Python等等。同时，Zookeeper的API设计简单，易于使用，支持客户端实现。
5. 开源和生态系统
   Zookeeper具有社区开发和维护的特点，有广泛的生态系统。Zookeeper已经被大量应用于大型的分布式系统，如Hadoop、Kafka等，同时还有多个开源软件集成了Zookeeper的功能，如Dubbo、ZKClient等。

总的来说，Zookeeper作为一个可靠、高性能、低延迟、易用的分布式协调服务框架，能够为分布式系统提供重要的支持和保障。Zookeeper在多语言支持、易用性、生态系统等方面具有优势，可以帮助开发者快速构建分布式应用程序，并实现协调、命名、分布式锁等常见功能，因此得到了广泛的应用和推广。	



## zookeeper未来发展趋势和研究方向

随着云计算、大数据、人工智能等新兴技术的不断发展和应用，分布式系统的规模和复杂性正在不断增强。作为分布式协调服务框架的代表，Zookeeper在未来的发展中也需要不断地适应和应对这些变化和挑战，以下是Zookeeper未来发展趋势和研究方向：

1. 支持更多的分布式场景以及数据类型
   Zookeeper需要支持更多的分布式场景和数据类型，并对各种性能和安全挑战进行优化。例如，支持更丰富的数据访问模型以及更高效的分布式事务处理。
2. 构建可扩展的高性能分布式系统
   Zookeeper需要特别关注在支持更大规模和更深度的分布式系统，以应对系统性能和可扩展需求。例如，设计更好的负载均衡和资源调度策略等。
3. 提升可操作性与管理功能
   Zookeeper应该往更简单方向发展，以便更好地进行配置、部署等操作。同时，需要提供更好的可视化界面，帮助管理员更好地管理它们的分布式系统。
4. 优化Zookeeper经典特性和算法
   Zookeeper可以继续挖掘现有的算法和技术，提出更好的优化方案，使得Zookeeper适应更多的分布式系统场景，并提高性能和可靠性。
5. 与云原生技术的整合
   Zookeeper需要在面对云原生架构时采用适应性的方法，例如发现自己在Kubernetes原生环境下的位置和角色，并融合容器化和微服务基础设施。

总的来看，Zookeeper在未来的发展方向上需要继续关注分布式场景下需要解决的业务问题，与时俱进地采用更高效的技术选择，以更好地适应分布式协调服务的发展需求。	



# Zookeeper使用

## Zookeeper基本安装配置

首先，Zookeeper软件包`zookeeper-3.4.9.tar.gz`我们上节课已经上传到用户家目录的`setups`目录下。然后进行解压和环境变量设置。命令:

```shell
mkdir ~/zookeeper
#创建用于存放Zookeeper相关文件的目录
cd ~/zookeeper
#进入该目录
tar -xzf ~/setups/zookeeper-3.4.9.tar.gz
#将软件包解压
```


![image-20230331114940196](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923609.png)



```shell
vi ~/.bash_profile
#配置Zookeeper相关的环境变量
```

![image-20230331115516317](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923610.png)



对配置文件进行修改，在文件末尾添加以下内容:

```shell
#zookeeper environment
#该路径以Zookeeper软件包实际解压解包的路径为准
ZOOKEEPER_HOME=/home/admin/zookeeper/zookeeper-3.4.9

#确保此项输入正确，否则可能会导致所有命令无法使用
PATH=$ZOOKEEPER_HOME/bin:$PATH

export ZOOKEEPER_HOME PATH
#必须按照前面的定义顺序书写
```



![image-20230331115739586](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923611.png)



```shell
source ~/.bash_profile
#使新配置的环境变量立即生效
echo $ZOOKEEPER_HOME
#查看新添加和修改的环境变量是否
echo $PATH
#设置成功，以及环境变量的值是否正确。
```

![image-20230331120016430](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923612.png)



## Zookeeper完全分布模式配置

```shell
cd ~/zookeeper
#进入Zookeeper相关文件的目录
mkdir data logs
#分别创建用于存放数据文件的目录“data”和用于存放日志文件的目录“logs”。
cd ~/zookeeper/zookeeper-3.4.9/conf
#进入Zookeeper的配置文件所在目录
cp zoo_sample.cfg zoo.cfg
#考贝生成Zookeeper的配置文件
```

![image-20230331172021564](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923613.png)

![image-20230331172132709](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923614.png)



```shell
vi zoo.cfg
#对配置文件进行修改
```

![image-20230331172504252](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923615.png)

```shell
#以下配置项若已经存在则修改其对应值，若不存在则在配置文件末尾进行添加:
dataDir=/home/admin/zookeeper/data
dataLogDir=/home/admin/zookeeper/logs
server.1=LZY-01:2888:3888
server.2=LZY-02:2888:3888
server.3=LZY-03:2888:3888
server.4=LZY-04:2888:3888
server.5=LZY-05:2888:3888
```

![image-20230331172618507](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923616.png)





## 同步安装和配置

将`zookeeper`目录和`.bash_profile`文件发给集群中所有主机

发送目标用户为集群专用用户**admin**

发送目标路径为`/home/admin`，即集群专用用户**admin**的家目录

```shell
scp -r ~/zookeeper ~/.bash_profile admin@LZY-02:/home/admin
scp -r ~/zookeeper ~/.bash_profile admin@LZY-03:/home/admin
scp -r ~/zookeeper ~/.bash_profile admin@LZY-04:/home/admin
scp -r ~/zookeeper ~/.bash_profile admin@LZY-05:/home/admin
```

![image-20230331173750394](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923617.png)

![image-20230331173818498](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923618.png)

![image-20230331173937705](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923619.png)

![image-20230331174028859](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923620.png)



然后每台执行`source ~/.bash_profile`使环境变量生效

```she
source ~/.bash_profile
```

![image-20230331174059864](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923621.png)

![image-20230331174230180](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923622.png)

![image-20230331174241249](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923623.png)

![image-20230331174207939](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923624.png)



在每台主机或虚拟机上，使用命令
`echo $ZOOKEEPER_HOME、echo $PATH`查看新添加和修改的环境变量是否设置成功，以及环境变量的值是否正确。

```shell
echo $ZOOKEEPER_HOME
echo $PATH
```

![image-20230331174505687](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923625.png)

![image-20230331174644313](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923626.png)

![image-20230331174741901](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923627.png)

![image-20230331174759145](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923628.png)

![image-20230331174814785](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923629.png)



## 配置Zookeeper节点标识文件

在集群中所有主机上使用命令`echo '*' > ~/zookeeper/data/myid`创建**Zookeeper**的节点标识文件，其中 ` *` 为节点的编号，与配置文件`server.*=LZY-01:2888:3888`中`server.*`中的 `*` 相对应。
命令:

```shell
echo '1' > ~/zookeeper/data/myid

echo '2' > ~/zookeeper/data/myid

echo '3' > ~/zookeeper/data/myid

echo '4' > ~/zookeeper/data/myid

echo '5' > ~/zookeeper/data/myid
 #注意这里的单引号格式
```


![image-20230331175507245](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923630.png)


## Zookeeper完全分布模式启动和验证

进行操作前，先关闭防火墙（**root**用户下):

```shell
 systemctl stop firewalld.service
 systemctl disable firewalld.service
```

![image-20230331180050585](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923631.png)





在集群中所有主机上使用命令`zkServer.sh start`启动**Zookeeper**服务的脚本，若启动过程没有报错，并且显示`STARTED`则表示启动成功。

```shell
zkServer.sh start
```

![image-20230331180300828](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923632.png)

![image-20230331180332293](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923633.png)

![image-20230331180359709](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923634.png)

![image-20230331180427883](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923636.png)

![image-20230331180441807](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923637.png)



在集群中所有主机上使用命令`jps`查看**Java**进程信息，若存在一个名为`QuorumPeerMain`的进程，则表示**Zookeeper**服务启动成功。

```shell 
jps
```

![image-20230331180722988](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923638.png)

![image-20230331180739940](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923639.png)

![image-20230331180751901](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923640.png)

![image-20230331180805958](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923641.png)

![image-20230331182427314](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923642.png)



在集群中所有主机上使用命令`zkServer.sh status`查看该节点**Zookeeper**服务当前的状态，若集群中只有一个**“leader”**节点，其余的均为**“follower”**节点，则集群的工作状态正常。防火墙必须关掉。如果防火墙未关闭，状态是**Error contacting service. It is probablynot running.**。

```shell
zkServer.sh status
```

![image-20230331182500377](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923643.png)
![image-20230331182528616](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923644.png)

![image-20230331190427657](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923645.png)

![image-20230331182554379](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923646.png)

![image-20230331190406362](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923647.png)



使用命令`zkCli.sh -server LZY-*:2181`利用**Zookeeper**的命令行工具连接**Zookeeper**集群，其中 `*` 为集群中节点的编号，可以选择连接集群中的任意一个节点，若显示“**CONNECTED”**则表示连接正常，命令行工具可以正常使用，在命令行工具中使用命令**“quit”**可以退出工具程序。

```shell
zkCli.sh -server LZY-01:2181

zkCli.sh -server LZY-02:2181

zkCli.sh -server LZY-03:2181

zkCli.sh -server LZY-04:2181

zkCli.sh -server LZY-05:2181
```

![image-20230331190720851](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923648.png)

![image-20230331190828261](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311923649.png)

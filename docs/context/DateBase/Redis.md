Redis全称为Remote Dictionary Server（远程数据服务），是一个由 Salvatore Sanfilippo 写的开源的基于**内存**的**key-value**存储系统，是跨平台的**非关系型**数据库，其主要被用作**高性能缓存服务器**使用，当然也可以作为消息中间件和Session共享等。Redis独特的键值对模型使之支持丰富的数据结构类型，即它的值可以是**字符串String**、**哈希Hash**、**列表List**、**集合Set**、**有序集合Sorted Set**，而不像Memcached要求的键和值都是字符串，它是一个基于内存的**数据结构**存储系统，可以用作数据库、缓存和消息代理。同时由于Redis是基于内存的方式，免去了磁盘I/O速度的影响，因此其读写性能极高。



Redis 主要由有两个程序组成：

- Redis 客户端 redis-cli
- Redis 服务器 redis-server

客户端、服务器可以位于同一台计算机或两台不同的计算机中。



远程连接到Redis

```shell
redis-cli -h 127.0.0.1 -p 6379 -a password
```









### 字符串

String 是一组字节。在 Redis 数据库中，字符串是二进制安全的。这意味着它们具有已知长度，并且不受任何特殊终止字符的影响。可以在一个字符串中存储最多 512 MB的内容。

```sql
SET mystr "hello world!" //设置字符串类型
GET mystr //读取字符串类型
```



```sql
SET bike:1 "Process 134"
GET bike:1
```

`bike`部分通常被视为键的**命名空间**或**前缀**



### 哈希

```sql
HSET bike:3 model Deimos brand Ergonom type 'Enduro bikes' price 4972
HGET bike:3 model
HGET bike:3 price
HGETALL bike:3
```



### 列表

Redis 列表定义为字符串列表，按插入顺序排序。可以将元素添加到 Redis 列表的头部或尾部。
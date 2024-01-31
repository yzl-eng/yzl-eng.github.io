## 相关操作

### 查看mysql集群状态

在任意一台集群主机上执行:

```shell
ndb_mgm -e show
```



### 启动顺序

1. 先启动管理节点
2. 再启动两个数据服务节点
3. 最后启动SQL节点

```shell
ndb_mgmd -f /usr/local/mysql/etc/config.ini
ndbd
service mysql start
```



### 关闭

关闭顺序:
SQL节点->数据节点->管理节点

在SQL服务节点执行:

```shell
service mysql stop
```

在管理节点执行:

```shell
ndb_mgm -e shutdown
```



## 练习一 表的创建、插入数据

**登录数据库**

``` mysql
mysql -u root -p
```



1、创建一个数据库testDB

代码:

```mysql
create database testDB;
use testDB;
```

![image-20230602110330849](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922924.png)

2、创建一个mytable表

代码:

```mysql
create table mytable (name varchar(20),sex char(1),birth date,birthaddr varchar(20));
```

注释:这个表中包含的数据为员工信息统计，有:姓名，性别，出生日期，出生地。由于`name`、`birthaddr`的列值是变化的，因此选择`VARCHAR`，其长度不一定是20。可以选择从1到255的任何长度，如果以后需要改变它的字长，可以使用`ALTER TABLE` 语句。性别只需一个字符就可以表示:`m`或`f`，因此选用`CHAR(1)`,`birth`列则使用`DATE`数据类型。

![image-20230602110426555](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922925.png)

3、显示表结构

代码:

```mysql
describe mytable;
```

![image-20230602110455551](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922926.png)

4、向表中插入一条记录

代码:

```mysql
insert into mytable values('abc','f','1988-07-07','china');
```

5、查找表中已存在的数据

代码：

```sql
select * from mytable;
```

![image-20230602110549026](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922927.png)



## 练习二 将txt文件导入表中

![image-20230602113236321](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922928.png)

![image-20230602111134061](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922929.png)

代码:

```shell
load data local infile "mysql.txt" into table mytable fields terminated by ',' lines terminated by '\r\n';
```

![image-20230602113256041](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922930.png)



## 练习三 SQL查询语句

```sql
#1.查看表结构
DESC mytable;
#2.查询所有列
SELECT * FROM mytable;
#3.查询指定列
SELECT name,sex,birth FROM mytable;
SELECT DISTINCT sex FROM mytable;
#只显示结果不同的项
#4.查询指定行
SELECT* FROM mytable WHERE sex='f';
```

![image-20230602113326877](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922931.png)

![image-20230602113355592](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922932.png)



### sql工具使用

![image-20230602113648864](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922933.png)

![image-20230602113551429](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922934.png)



## 作业一

根据下列表格中所提供的关系型数据库的数据模型和数据，在MySQL数据库中创建和添加相应的数据库、表、数据。

![image-20230602105729490](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922935.png)

```sql
create table book_info (title varchar(20),borrower varchar(20),sex char(1),number varchar(20),lendingdate date,returndate date);
insert into book_info values('yuncunchu','zhansan','f','20230001','2023-02-09','2023-03-09');
insert into book_info values('shujuku','lisi','m','20230002','2023-03-09','2023-04-09');
insert into book_info values('xunihuajishu','wanger','f','20230003','2023-04-09','2023-05-09');
insert into book_info values('javakaifa','lzy','m','20230004','2023-06-02','2023-06-03');
```

![image-20230602115251778](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922936.png)

![image-20230602115242960](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922937.png)

## 作业二

将作业一创建的数据库及其中的数据导出为SQL脚本文件

导出数据库中指定表`mysql dump -u 用户名 -p 数据库名 表名 >导出到路径和导出的文件名`。

**需退出mysql操作**

```shell
mysqldump -u root -p testDB book_info > /root/mysql.sql;
```

![image-20230602120021251](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922938.png)

![image-20230602120145830](https://raw.githubusercontent.com/yzl-eng/blogImage/main/img/202401311922939.png)